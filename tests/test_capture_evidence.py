# this_file: tests/test_capture_evidence.py
"""Retain inspected legacy evidence without executing owned native stand-ins."""

import ast
import copy
import json
import sys
from types import ModuleType, SimpleNamespace

import pytest

from fontlab_echopy.tooling import capture, chunked
from fontlab_echopy.tooling.generate import generate, module_source
from fontlab_echopy.tooling.merge import merge


class NativeCallable:
    __signature__ = "not an inspect.Signature"

    def __call__(self):
        raise AssertionError("Metadata capture must never invoke a callable")


@pytest.mark.parametrize("error", [TypeError, ValueError])
def test_text_signature_when_inspection_fails_then_literal_evidence_is_used(monkeypatch, error):
    value = NativeCallable()
    value.__text_signature__ = "(value, /, *, label='a,b', enabled=True)"

    def inspect_failure(value):
        raise error("No inspect signature")

    monkeypatch.setattr(capture.inspect, "signature", inspect_failure)
    info = capture.callable_info("native", value)
    assert info["signature"] == value.__text_signature__
    assert info["text_signature"] == value.__text_signature__
    assert info["signature_source"] == "__text_signature__"


@pytest.mark.parametrize("text", ["($module, value=<unknown>)", "(value=unsafe())", "(value=owned.attr)", "(value", "(value)\npass\ndef other()", "(value, value)", "(value):\n pass\nresult = 1 #"])
def test_text_signature_when_malformed_or_nonliteral_then_keeps_unresolved_evidence(text):
    value = NativeCallable()
    value.__text_signature__ = text
    info = capture.callable_info("native", value)
    assert info["signature"] == "(...)"
    assert info["text_signature"] == text
    assert info["signature_source"] == "unresolved __text_signature__"


@pytest.mark.parametrize("text", [None, "", 42])
def test_text_signature_when_missing_then_retains_conservative_fallback(text):
    value = NativeCallable()
    value.__text_signature__ = text
    info = capture.callable_info("native", value)
    assert info["signature"] == "(...)"
    assert "text_signature" not in info


def test_callable_when_inspect_succeeds_then_records_its_provenance():
    def owned(value, /, *, label=None):
        raise AssertionError("Do not call")

    info = capture.callable_info("owned", owned)
    assert info["signature"] == "(value, /, *, label=None)"
    assert info["signature_source"] == "inspect.signature"
    assert "text_signature" not in info


@pytest.mark.parametrize("error", [TimeoutError, KeyboardInterrupt, SystemExit])
def test_callable_when_inspection_cancelled_then_propagates(monkeypatch, error):
    def cancelled(value):
        raise error("Owned cancellation")

    monkeypatch.setattr(capture.inspect, "signature", cancelled)
    with pytest.raises(error, match="Owned cancellation"):
        capture.callable_info("native", NativeCallable())


def test_class_when_allocator_inherited_then_keeps_init_allocation_and_mro_separate():
    class Base:
        def __new__(cls, value):
            """Owned allocation documentation."""
            raise AssertionError("Do not construct")

    class Native(Base):
        def __init__(receiver, *, label=None):
            """Owned initializer documentation."""
            raise AssertionError("Do not initialise")

    info = capture.class_info(Native, "Native")
    assert info["mro"] == ["Native", "Base", "object"]
    assert info["bases"] == ["Base"]
    assert [c["name"] for c in info["constructors"]] == ["__init__"]
    assert info["constructors"][0]["signature"] == "(receiver, *, label=None)"
    assert info["allocation_constructor"]["signature"] == "(cls, value)"
    assert info["allocation_constructor"]["binding"] == "staticmethod"
    assert info["allocation_constructor"]["signature_source"] == "inspect.signature"
    original = copy.deepcopy(info)
    source = module_source("owned_absent_native", {"classes": [info]}, True)
    node = next(n for n in ast.parse(source).body if isinstance(n, ast.ClassDef))
    doc = ast.get_docstring(node)
    assert "Captured native MRO: Native, Base, object" in doc
    assert "Native __new__ allocation evidence" in doc
    assert "Owned allocation documentation." in doc
    init = next(n for n in node.body if isinstance(n, ast.FunctionDef))
    assert init.name == "__init__" and not init.args.vararg
    assert ast.get_docstring(init) == "Owned initializer documentation."
    assert info == original, "Rendering must preserve capture evidence"
    assert "allocation_constructor" not in capture.class_info(object, "object")


def test_required_seeds_when_present_missing_or_root_absent_then_reported(monkeypatch):
    root = SimpleNamespace(QtCore=SimpleNamespace())
    monkeypatch.setattr(capture, "resolve", lambda name: root)
    monkeypatch.setattr(capture, "_pythonqt_child", lambda root, child, errors: getattr(root, child, None))
    item = capture.capture(["PythonQt"])["modules"]["PythonQt"]
    assert item["required_seeds"] == {"discovered": ["QtCore"], "missing": sorted(set(capture.QT_SEEDS) - {"QtCore"})}
    monkeypatch.setattr(capture, "resolve", lambda name: None)
    item = capture.capture(["PythonQt"])["modules"]["PythonQt"]
    assert item["required_seeds"] == {"discovered": [], "missing": sorted(capture.QT_SEEDS)}


def test_required_seeds_when_getter_fails_then_missing_and_not_retried(monkeypatch):
    calls = []

    class Root(ModuleType):
        def __dir__(self):
            return ["QtCore"]

        def __getattribute__(self, name):
            if name == "QtCore":
                calls.append(name)
                raise ValueError("Owned getter failure")
            return super().__getattribute__(name)

    monkeypatch.setattr(capture, "QT_SEEDS", ("QtCore",))
    monkeypatch.setattr(capture, "resolve", lambda name: Root("PythonQt"))
    item = capture.capture(["PythonQt"])["modules"]["PythonQt"]
    assert item["required_seeds"] == {"discovered": [], "missing": ["QtCore"]}
    assert item["namespace"]["errors"] == [{"name": "QtCore", "error": "ValueError"}]
    assert calls == ["QtCore"]


def test_chunked_when_metadata_roundtrips_then_generation_merge_preserve_evidence(monkeypatch, tmp_path):
    module = ModuleType("owned_absent_native")
    module.native = NativeCallable()
    module.native.__text_signature__ = "(value, /, *, label=None)"

    class Point:
        def __new__(cls, value):
            """Allocation provenance."""
            raise AssertionError("Do not allocate")

    module.Point = Point
    monkeypatch.setitem(sys.modules, module.__name__, module)

    def run(code, **variables):
        scope = dict(variables)
        exec(code, scope)
        return SimpleNamespace(value=json.loads(json.dumps(scope["result"])))

    item = chunked.capture_module(run, module.__name__, (ValueError,))
    assert item["namespace"] == capture.capture([module.__name__])["modules"][module.__name__]["namespace"]
    before = copy.deepcopy(item)
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    generate({"modules": {module.__name__: item}}, raw, {"sha256": "owned-capture"})
    merge(raw, merged, [])
    source = (merged / f"{module.__name__}.pyi").read_text()
    assert "Allocation provenance." in source and "Captured native MRO: Point, object" in source
    native = next(n for n in ast.parse(source).body if isinstance(n, ast.FunctionDef) and n.name == "native")
    assert [a.arg for a in native.args.posonlyargs] == ["value"]
    assert [a.arg for a in native.args.kwonlyargs] == ["label"]
    assert item == before
    assert json.loads((merged / "_provenance.json").read_text())["capture_identity"] == {"sha256": "owned-capture"}


def test_capture_cli_when_owned_qt_present_then_persists_required_seed_diagnostics(monkeypatch, tmp_path):
    from fontlab_echopy.tooling.cli import main

    root = SimpleNamespace(QtCore=SimpleNamespace())
    monkeypatch.setattr(capture, "resolve", lambda name: root if name == "PythonQt" else None)
    monkeypatch.setattr(capture, "_pythonqt_child", lambda root, child, errors: getattr(root, child, None))
    output = tmp_path / "capture.json"
    main(["capture", str(output)])
    item = json.loads(output.read_text())["modules"]["PythonQt"]
    assert item["required_seeds"] == {"discovered": ["QtCore"], "missing": sorted(set(capture.QT_SEEDS) - {"QtCore"})}
