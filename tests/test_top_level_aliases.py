# this_file: tests/test_top_level_aliases.py
"""Owned modules exercise raw and merged aliases without native providers."""

import ast
import hashlib
import inspect
import json
import sys
from pathlib import Path
from types import ModuleType

import pytest

from fontlab_echopy._runtime import NativeModule, NativeUnavailable, populate
from fontlab_echopy.tooling.generate import generate, source_name
from fontlab_echopy.tooling.merge import documented_outputs, merge

NATIVE = "owned_top_level_alias_native"


def _scope(kind, name):
    item = {"name": name}
    if kind == "functions":
        item.update(signature="(value=7, /)", doc="Owned callable evidence.")
    elif kind != "classes":
        item["type"] = "int"
    return {"names": [name], kind: [item]}


def _load(tmp_path, monkeypatch, scope, stage):
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    report = generate({"modules": {NATIVE: {"namespace": scope}}}, raw)
    merge(raw, merged, [])
    path = (raw if stage == "raw" else merged) / (NATIVE + ".py")
    facade = ModuleType("owned_top_level_alias_facade")
    facade.__file__ = str(path)
    monkeypatch.setitem(sys.modules, facade.__name__, facade)
    exec(compile(path.read_text(), str(path), "exec"), facade.__dict__)
    return facade, report, merged / (NATIVE + ".pyi")


@pytest.mark.parametrize("stage", ["raw", "merged"])
@pytest.mark.parametrize(
    "kind", ["classes", "functions", "attributes", "constants", "modules"]
)
@pytest.mark.parametrize("name", ["raise", "A-B"])
def test_offline_aliases_preserve_declarations_and_absence(
    tmp_path, monkeypatch, stage, kind, name
):
    monkeypatch.delitem(sys.modules, NATIVE, raising=False)
    facade, report, stub = _load(tmp_path, monkeypatch, _scope(kind, name), stage)
    alias = source_name(name)
    assert report["modules"][NATIVE]["missing_names"] == []
    assert report["modules"][NATIVE]["source_aliases"] == {name: alias}
    assert name in facade.__all__
    if kind in {"classes", "functions"}:
        value = getattr(facade, name)
        assert value is getattr(facade, alias)
        if kind == "functions":
            assert inspect.getdoc(value).startswith("Owned callable evidence.")
            assert inspect.signature(value).parameters["value"].default == 7
        with pytest.raises(NativeUnavailable):
            value()
    else:
        assert alias in facade.__annotations__
        assert not hasattr(facade, alias)
        assert not hasattr(facade, name)
        assert any(
            isinstance(n, ast.AnnAssign) and n.target.id == alias
            for n in ast.parse(stub.read_text()).body
        )


@pytest.mark.parametrize("stage", ["raw", "merged"])
@pytest.mark.parametrize(
    "kind", ["classes", "functions", "attributes", "constants", "modules"]
)
@pytest.mark.parametrize("name", ["raise", "A-B"])
def test_live_aliases_follow_original_identity_and_lifecycle(
    tmp_path, monkeypatch, stage, kind, name
):
    native = ModuleType(NATIVE)
    first = object()
    setattr(native, name, first)
    monkeypatch.setitem(sys.modules, NATIVE, native)
    facade, _, _ = _load(tmp_path, monkeypatch, _scope(kind, name), stage)
    alias = source_name(name)
    assert getattr(facade, alias) is getattr(facade, name) is first
    second = object()
    setattr(native, name, second)
    assert getattr(facade, alias) is getattr(facade, name) is second
    delattr(native, name)
    assert not hasattr(facade, alias) and not hasattr(facade, name)
    assert alias not in dir(facade) and name not in dir(facade)
    replacement = object()
    setattr(facade, alias, replacement)
    assert getattr(native, name) is replacement
    assert alias in dir(facade) and name in dir(facade)
    assert not hasattr(native, alias)
    delattr(facade, alias)
    assert not hasattr(native, name)
    assert not hasattr(facade, alias) and not hasattr(facade, name)
    with pytest.raises(AttributeError):
        delattr(facade, alias)
    setattr(facade, name, first)
    assert getattr(facade, alias) is first
    delattr(facade, name)
    assert not hasattr(facade, alias)
    facade.ordinary = second
    assert native.ordinary is second
    del facade.ordinary
    assert not hasattr(native, "ordinary")
    child = NativeModule("owned_child")
    child._echopy_native = None
    facade.child = child
    assert facade.child is child and not hasattr(native, "child")


def test_merge_does_not_infer_aliases_from_arbitrary_assignments():
    tree = ast.parse("class A_B: pass\nother['A-B'] = A_B\n")
    facade, _ = documented_outputs(tree, Path("owned.py"))
    assert "'A-B'" not in facade


def test_historical_class_marker_still_merges():
    tree = ast.parse("class A_B: pass\nglobals()['A-B'] = A_B\n")
    facade, _ = documented_outputs(tree, Path("owned.py"))
    assert "{'A-B': 'A_B'}" in facade


def test_legacy_populate_alias_argument_stays_live(monkeypatch):
    native = ModuleType(NATIVE)
    setattr(native, "A-B", object())
    monkeypatch.setitem(sys.modules, NATIVE, native)
    facade = ModuleType("owned_legacy_facade")
    monkeypatch.setitem(sys.modules, facade.__name__, facade)
    populate(facade.__dict__, NATIVE, {"A-B": "A_B"})
    replacement = object()
    setattr(native, "A-B", replacement)
    assert facade.A_B is replacement


@pytest.mark.parametrize("kind", ["functions", "attributes", "constants", "modules"])
def test_alias_collision_is_rejected_before_existing_output_changes(tmp_path, kind):
    sentinel = tmp_path / "prior.py"
    sentinel.write_text("# Generated from earlier input\n")
    scope = _scope(kind, "A-B")
    scope["classes"] = [{"name": "A_B"}]
    with pytest.raises(ValueError, match="Source name collision"):
        generate({"modules": {NATIVE: {"namespace": scope}}}, tmp_path)
    assert list(tmp_path.iterdir()) == [sentinel]
    assert sentinel.read_text() == "# Generated from earlier input\n"


@pytest.mark.parametrize("stage", ["raw", "merged"])
def test_alias_added_after_initial_bind_is_live(tmp_path, monkeypatch, stage):
    native = ModuleType(NATIVE)
    monkeypatch.setitem(sys.modules, NATIVE, native)
    facade, _, _ = _load(tmp_path, monkeypatch, _scope("attributes", "A-B"), stage)
    assert not hasattr(facade, "A_B")
    assert "A_B" not in dir(facade)
    value = object()
    setattr(native, "A-B", value)
    assert facade.A_B is value
    assert "A_B" in dir(facade)


def test_private_native_marker_name_remains_an_ordinary_declaration(
    tmp_path, monkeypatch
):
    name = "_echopy_source_aliases"
    facade, report, _ = _load(tmp_path, monkeypatch, _scope("functions", name), "raw")
    assert callable(getattr(facade, name))
    assert report["modules"][NATIVE]["missing_names"] == []


def test_top_level_dunder_functions_and_annotations_stay_excluded(tmp_path):
    scope = {"functions": [{"name": "__secret"}], "attributes": [{"name": "__value"}]}
    raw = tmp_path / "raw"
    generate({"modules": {NATIVE: {"namespace": scope}}}, raw)
    text = (raw / (NATIVE + ".py")).read_text()
    assert "def native___secret" not in text
    assert "native___value:" not in text


def test_combined_aliases_agree_with_identity_manifest(tmp_path):
    from fontlab_echopy.tooling.identities import derive_identities

    kinds = ["classes", "functions", "attributes", "constants", "modules"]
    names = ["Class-Name", "raise", "value-name", "False", "module-name"]
    scope = {"names": names}
    for kind, name in zip(kinds, names):
        scope[kind] = _scope(kind, name)[kind]
    capture = json.dumps({"modules": {NATIVE: {"namespace": scope}}}).encode()
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    report = generate(
        json.loads(capture), raw, {"sha256": hashlib.sha256(capture).hexdigest()}
    )
    merge(raw, merged, [])
    manifest = derive_identities(capture, merged)
    assert manifest["native_spellings"] == {
        NATIVE + "." + name: NATIVE + "." + source_name(name) for name in names
    }
    assert report["modules"][NATIVE]["missing_names"] == []
    assert report["modules"][NATIVE]["source_aliases"] == {
        name: source_name(name) for name in names
    }


def test_historical_raw_two_argument_bind_imports(monkeypatch):
    monkeypatch.delitem(sys.modules, NATIVE, raising=False)
    facade = ModuleType("owned_historical_raw")
    monkeypatch.setitem(sys.modules, facade.__name__, facade)
    exec(
        "from fontlab_echopy._runtime import bind as _bind\n"
        "class A_B: pass\n"
        "globals()['A-B'] = A_B\n"
        f"_bind(globals(), {NATIVE!r})\n"
        "A_B = globals()['A-B']\n",
        facade.__dict__,
    )
    assert facade.A_B is getattr(facade, "A-B")


@pytest.mark.parametrize("stage", ["raw", "merged"])
@pytest.mark.parametrize(
    "kind", ["classes", "functions", "attributes", "constants", "modules"]
)
@pytest.mark.parametrize("deletion", ["native", "facade"])
def test_ordinary_native_names_do_not_resurrect_cached_values(
    tmp_path, monkeypatch, stage, kind, deletion
):
    native = ModuleType(NATIVE)
    first = object()
    native.ordinary = first
    monkeypatch.setitem(sys.modules, NATIVE, native)
    facade, _, _ = _load(tmp_path, monkeypatch, _scope(kind, "ordinary"), stage)
    assert facade.ordinary is first
    delattr(native if deletion == "native" else facade, "ordinary")
    assert not hasattr(facade, "ordinary"), "Deleted native value leaked from facade cache"
    assert "ordinary" not in dir(facade), "Deleted native name is still advertised"
    with pytest.raises(AttributeError):
        del facade.ordinary
    replacement = object()
    native.ordinary = replacement
    assert facade.ordinary is replacement
    assert "ordinary" in dir(facade)
    facade.ordinary = first
    assert native.ordinary is first
