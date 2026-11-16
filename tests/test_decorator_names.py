# this_file: tests/test_decorator_names.py
"""Owned captures keep descriptor identity despite captured builtin names."""
import ast
import builtins
import inspect
import types

import pytest

from fontlab_echopy.tooling.capture import namespace
from fontlab_echopy.tooling.generate import function, generate, module_source
from fontlab_echopy.tooling.merge import merge


@pytest.mark.parametrize("binding", ["staticmethod", "classmethod"])
@pytest.mark.parametrize("location", ["module", "class", "none"])
@pytest.mark.parametrize("stage", ["raw", "merged"])
def test_captured_decorator_names_preserve_descriptors(binding, location, stage, tmp_path):
    def inert(receiver, value=3, /, *, label="a,b"):
        raise AssertionError("Owned methods must never run")

    kind = getattr(builtins, binding)
    members = {"zz_target": kind(inert), "__init__": kind(inert)}
    if location == "class":
        members[binding] = inert
    widget = type("zzWidget", (), members)
    exports = {"zzWidget": widget}
    if location == "module":
        exports[binding] = type(binding, (), {})
    name = "absent_owned_decorator_fixture"
    captured = namespace(types.SimpleNamespace(**exports), name)
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    report = generate({"modules": {name: {"namespace": captured}}}, raw)
    assert not report["modules"][name]["missing_names"]
    assert not report["modules"][name]["missing_class_members"]
    merge(raw, merged, [])
    path = raw / (name + ".py") if stage == "raw" else merged / (name + ".pyi")
    values = {"__name__": "owned_decorator_execution"}
    exec(compile(path.read_text(), str(path), "exec"), values)
    emitted = values["zzWidget"]
    for member in ("zz_target", "__init__"):
        descriptor = inspect.getattr_static(emitted, member)
        assert type(descriptor) is kind, "Use the builtin descriptor, not a captured shadow"
        assert list(inspect.signature(descriptor.__func__).parameters) == ["receiver", "value", "label"]
    if location == "module":
        assert values[binding].__name__ == binding, "Preserve the captured public spelling"
    elif location == "class":
        assert inspect.isfunction(inspect.getattr_static(emitted, binding))
    assert set(values["__all__"]) == set(exports), "Private imports must not enter exports"
    facade = (merged / (name + ".py")).read_text()
    assert "import builtins" not in facade and "class zzWidget" not in facade


@pytest.mark.parametrize("location", ["module", "class"])
@pytest.mark.parametrize("inventory", [False, True])
@pytest.mark.parametrize("normalized", [False, True])
def test_private_builtin_reference_avoids_all_captured_names(location, inventory, normalized):
    occupied = "_echopy_builtins"
    native = occupied.replace("_", "-", 1) if normalized else occupied
    cls = {"name": "Widget", "methods": [{"name": "target", "binding": "staticmethod"}]}
    scope = {"classes": [cls]}
    owner = scope if location == "module" else cls
    owner["names" if inventory else "constants"] = [native] if inventory else [{"name": native}]
    source = module_source("absent_private_reference_fixture", scope, True)
    assert source == module_source("absent_private_reference_fixture", scope, True)
    imports = [node for node in ast.parse(source).body if isinstance(node, ast.Import)]
    aliases = [alias.asname for node in imports for alias in node.names if alias.name == "builtins"]
    assert len(aliases) == 1 and aliases[0] != occupied, "Avoid normalized declarations and inventory names"
    values = {"__name__": "owned_private_reference_execution"}
    exec(source, values)
    assert type(inspect.getattr_static(values["Widget"], "target")) is staticmethod


def test_function_direct_call_retains_bare_decorator_contract():
    source = function({"name": "target", "binding": "staticmethod"}, "owned", True)
    assert source.startswith("    @staticmethod\n")


@pytest.mark.parametrize("stage", ["raw", "merged"])
def test_builtin_reference_skips_repeated_shadows_across_classes(stage, tmp_path):
    def inert(receiver):
        raise AssertionError("Owned methods must never run")

    widget = type("zzWidget", (), {
        "_echopy_builtins_": inert,
        "zz_static": staticmethod(inert),
        "zz_class": classmethod(inert),
    })
    sibling = type("EarlierWidget", (), {"_echopy_builtins__": inert})
    exports = {"_echopy_builtins": type("Shadow", (), {}), "zzWidget": widget, "EarlierWidget": sibling}
    name = "absent_repeated_builtin_fixture"
    captured = namespace(types.SimpleNamespace(**exports), name)
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    report = generate({"modules": {name: {"namespace": captured}}}, raw)
    assert report["modules"][name]["declared_names"] == len(exports)
    merge(raw, merged, [])
    path = raw / (name + ".py") if stage == "raw" else merged / (name + ".pyi")
    source = path.read_text()
    assert "import builtins as _echopy_builtins___" in source
    values = {"__name__": "owned_repeated_builtin_execution"}
    exec(compile(source, str(path), "exec"), values)
    assert type(inspect.getattr_static(values["zzWidget"], "zz_static")) is staticmethod
    assert type(inspect.getattr_static(values["zzWidget"], "zz_class")) is classmethod
    assert set(values["__all__"]) == set(exports)
