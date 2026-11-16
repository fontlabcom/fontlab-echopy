# this_file: tests/test_module_attribute_contracts.py
"""Owned end-to-end native value dispatch and annotation documentation cases."""

import ast
import json
import sys
from types import ModuleType

import pytest
from griffe import visit

from fontlab_echopy.tooling.capture import namespace
from fontlab_echopy.tooling.generate import generate, source_name
from fontlab_echopy.tooling.merge import merge

NATIVE = "owned_attribute_contract_native"


def load_value(tmp_path, monkeypatch, name, stage, *, native=True):
    """Generate an actual raw/merged facade without importing host bindings."""
    scope = {"attributes": [{"name": name, "type": "int"}]}
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    generate({"modules": {NATIVE: {"namespace": scope}}}, raw)
    merge(raw, merged, [])
    target = ModuleType(NATIVE) if native else None
    if native:
        setattr(target, name, object())
        monkeypatch.setitem(sys.modules, NATIVE, target)
    else:
        monkeypatch.delitem(sys.modules, NATIVE, raising=False)
    path = (raw if stage == "raw" else merged) / (NATIVE + ".py")
    facade = ModuleType("owned_attribute_contract_facade")
    facade.__file__ = str(path)
    monkeypatch.setitem(sys.modules, facade.__name__, facade)
    exec(compile(path.read_text(), str(path), "exec"), facade.__dict__)
    return facade, target


@pytest.mark.parametrize("stage", ["raw", "merged"])
@pytest.mark.parametrize("route", ["native", "alias"])
@pytest.mark.parametrize("name", [
    "value", "value-with-dash", "_echopy_value", "_echopy-value",
    "_echopy_value-with-dash", "_echopy_builtins",
])
def test_allowed_module_value_when_written_then_all_routes_share_current_identity(
    tmp_path, monkeypatch, name, route, stage,
):
    facade, native = load_value(tmp_path, monkeypatch, name, stage)
    alias = source_name(name)
    state = {key: facade.__dict__[key] for key in (
        "_echopy_native", "_echopy_name", "_echopy_aliases",
    )}
    first = getattr(native, name)
    assert getattr(facade, name) is getattr(facade, alias) is first
    replacement = object()
    spelling = name if route == "native" else alias
    setattr(facade, spelling, replacement)
    assert getattr(native, name) is replacement, "Write must reach the native owner"
    assert getattr(facade, alias) is getattr(facade, name) is replacement
    assert all(facade.__dict__[key] is value for key, value in state.items())
    assert name in dir(facade) and alias in dir(facade)
    delattr(facade, spelling)
    assert not hasattr(native, name)
    assert not hasattr(facade, name) and not hasattr(facade, alias)
    assert name not in dir(facade) and alias not in dir(facade)
    with pytest.raises(AttributeError):
        delattr(facade, spelling)
    setattr(facade, spelling, first)
    assert getattr(native, name) is getattr(facade, alias) is first


@pytest.mark.parametrize("stage", ["raw", "merged"])
def test_annotation_only_prefix_value_when_offline_then_it_stays_absent(
    tmp_path, monkeypatch, stage,
):
    facade, native = load_value(
        tmp_path, monkeypatch, "_echopy-value", stage, native=False,
    )
    assert native is None and "_echopy_value" in facade.__annotations__
    assert not hasattr(facade, "_echopy-value")
    assert not hasattr(facade, "_echopy_value")


@pytest.mark.parametrize("stage", ["raw", "merged"])
@pytest.mark.parametrize("route", ["native", "alias"])
def test_native_write_rejection_when_aliased_then_error_and_original_value_survive(
    tmp_path, monkeypatch, stage, route,
):
    name = "_echopy-value"
    facade, native = load_value(tmp_path, monkeypatch, name, stage)
    original = getattr(native, name)

    class ReadOnly(ModuleType):
        def __setattr__(self, field, value):
            if field == name:
                raise RuntimeError("Owned native value is read-only")
            super().__setattr__(field, value)

    native.__class__ = ReadOnly
    spelling = name if route == "native" else source_name(name)
    rejected = object()
    with pytest.raises(RuntimeError, match="read-only"):
        setattr(facade, spelling, rejected)
    assert getattr(native, name) is getattr(facade, spelling) is original
    assert facade.__dict__.get(spelling) is not rejected


def adjacent_doc(tree, name):
    for index, node in enumerate(tree.body):
        if isinstance(node, ast.AnnAssign) and node.target.id == name:
            following = tree.body[index + 1] if index + 1 < len(tree.body) else None
            if isinstance(following, ast.Expr) and isinstance(following.value, ast.Constant):
                return following.value.value
    return None


@pytest.mark.parametrize("collection", ["attributes", "constants", "modules"])
@pytest.mark.parametrize("name", ["value", "value-with-dash"])
@pytest.mark.parametrize("captured_doc", [None, "Owned captured value documentation."])
def test_module_annotation_when_enriched_then_doc_type_and_offline_absence_survive(
    tmp_path, monkeypatch, collection, name, captured_doc,
):
    info = {"name": name, "type": "int"}
    if captured_doc:
        info["doc"] = captured_doc
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    generate({"modules": {NATIVE: {"namespace": {collection: [info]}}}}, raw)
    alias = source_name(name)
    before = (raw / (NATIVE + ".py")).read_bytes()
    raw_doc = adjacent_doc(ast.parse(before), alias)
    assert raw_doc == captured_doc, "Raw source must preserve captured attribute docs"
    overlay = tmp_path / "overlay.json"
    supplemental = "Owned maintained value documentation."
    overlay.write_text(json.dumps({NATIVE + "." + alias: {
        "doc": supplemental, "returns": "str", "source": "owned-source",
    }}))
    assert merge(raw, merged, [overlay]) == {"applied": 1, "unmatched": []}
    stub = merged / (NATIVE + ".pyi")
    tree = ast.parse(stub.read_text())
    node = next(item for item in tree.body if isinstance(item, ast.AnnAssign))
    assert ast.unparse(node.annotation) == "str"
    doc = adjacent_doc(tree, alias)
    assert supplemental in doc and "Source: owned-source" in doc
    if captured_doc:
        assert doc.startswith(captured_doc) and doc.count(captured_doc) == 1
    documented = visit("owned", filepath=stub, code=stub.read_text())
    assert documented.members[alias].docstring.value == doc
    assert str(documented.members[alias].annotation) == "str"
    assert (raw / (NATIVE + ".py")).read_bytes() == before
    monkeypatch.delitem(sys.modules, NATIVE, raising=False)
    facade = ModuleType("owned_attribute_doc_facade")
    path = merged / (NATIVE + ".py")
    facade.__file__ = str(path)
    monkeypatch.setitem(sys.modules, facade.__name__, facade)
    exec(compile(path.read_text(), str(path), "exec"), facade.__dict__)
    assert alias in facade.__annotations__ and not hasattr(facade, alias)
    assert not hasattr(facade, name), "Documentation must not invent native values"


def test_value_overlay_when_multiple_inputs_then_maintained_precedence_is_retained(tmp_path):
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    generate({"modules": {NATIVE: {"namespace": {
        "attributes": [{"name": "value", "type": "int", "doc": "Native value."}],
    }}}}, raw)
    overlays = []
    for index, patch in enumerate([
        {"doc": "First overlay.", "returns": "float", "source": "first"},
        {"doc": "Final overlay.", "source": "second"},
    ]):
        path = tmp_path / f"overlay-{index}.json"
        path.write_text(json.dumps({NATIVE + ".value": patch}))
        overlays.append(path)
    assert merge(raw, merged, overlays) == {"applied": 1, "unmatched": []}
    tree = ast.parse((merged / (NATIVE + ".pyi")).read_text())
    doc = adjacent_doc(tree, "value")
    assert doc == "Native value.\n\nSupplemental documentation:\nFinal overlay.\n\nSource: second"
    node = next(item for item in tree.body if isinstance(item, ast.AnnAssign))
    assert ast.unparse(node.annotation) == "float"


def test_owned_capture_when_property_has_docs_then_getter_is_never_called(tmp_path):
    def getter(owner):
        """Owned descriptor documentation from capture."""
        raise AssertionError("Reading capture metadata must not invoke a getter")

    native = ModuleType(NATIVE)
    native.value = property(getter)
    captured = namespace(native, NATIVE)
    before = json.dumps(captured, sort_keys=True)
    assert captured["attributes"][0]["doc"] == getter.__doc__
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    generate({"modules": {NATIVE: {"namespace": captured}}}, raw)
    assert merge(raw, merged, []) == {"applied": 0, "unmatched": []}
    stub = merged / (NATIVE + ".pyi")
    documented = visit("owned", filepath=stub, code=stub.read_text())
    assert documented.members["value"].docstring.value == getter.__doc__
    assert json.dumps(captured, sort_keys=True) == before
