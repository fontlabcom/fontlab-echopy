# this_file: tests/test_pipeline.py
"""Acceptance tests for native fidelity and deterministic source generation."""
import ast
import importlib
import json
import sys
import types
from pathlib import Path

import pytest

from fontlab_echopy._runtime import NativeUnavailable, bind
from fontlab_echopy.tooling.capture import capture
from fontlab_echopy.tooling.generate import generate
from fontlab_echopy.tooling.merge import merge
from fontlab_echopy.tooling.signatures import signature


def test_cpp_signature_preserves_types_and_optional_parameters():
    args, result = signature("void move(double dx, double dy = 0)", "move", True)
    assert args == "self, dx: float, dy: float = 0"
    assert result == "None"
    assert signature("(...)", "move", True) == ("self, *args: Any, **kwargs: Any", "Any")


def test_native_symbols_have_identity_and_transparent_results(monkeypatch):
    native = types.ModuleType("fake_echopy_native")
    class Point:
        def copy(self):
            return self
    native.Point = Point
    native.identity = lambda value: value
    monkeypatch.setitem(sys.modules, native.__name__, native)
    facade = types.ModuleType("facade")
    monkeypatch.setitem(sys.modules, "facade", facade)
    bind(facade.__dict__, native.__name__)
    assert facade.Point is Point
    value = facade.Point()
    assert facade.identity(value) is value.copy()
    native.current = value
    assert facade.current is value
    facade.current = "changed"
    assert native.current == "changed"
    del facade.current
    assert not hasattr(native, "current")


def test_capture_all_names_and_no_method_invocation(monkeypatch):
    module = types.ModuleType("fake_echopy_native")
    class Widget:
        def forbidden(self):
            raise AssertionError("capture called a native method")
    module.Widget = Widget
    module.answer = 42
    monkeypatch.setitem(sys.modules, module.__name__, module)
    data = capture([module.__name__, "missing_echopy_module"])
    scope = data["modules"][module.__name__]["namespace"]
    assert scope["names"] == ["Widget", "answer"]
    assert scope["classes"][0]["methods"][0]["name"] == "forbidden"
    assert not data["modules"]["missing_echopy_module"]["available"]


def test_generation_merge_preserve_inputs_and_documentation(tmp_path):
    data = {"modules": {"sample": {"available": True, "namespace": {
        "classes": [{"name": "Point", "doc": "Native point.", "methods": [
            {"name": "move", "doc": "Move the point.", "signature": "void move(double dx)"}]}],
        "functions": [{"name": "take", "signature": "take(value)", "doc": "Accept a value."}],
        "attributes": [{"name": "current", "type": "object"}],
    }}}}
    raw = tmp_path / "raw"
    generate(data, raw)
    original = (raw / "sample.py").read_bytes()
    patch = tmp_path / "patches.json"
    patch.write_text(json.dumps({"sample.Point": {"doc": "Enriched point."}}))
    merged = tmp_path / "merged"
    merge(raw, merged, [patch])
    tree = ast.parse((merged / "sample.pyi").read_text())
    point = next(n for n in tree.body if isinstance(n, ast.ClassDef))
    assert "Native point." in ast.get_docstring(point)
    assert "Enriched point." in ast.get_docstring(point)
    method = next(n for n in point.body if isinstance(n, ast.FunctionDef) and n.name == "move")
    assert ast.unparse(method.args.args[1].annotation) == "float"
    assert ast.get_docstring(method) == "Move the point."
    assert (raw / "sample.py").read_bytes() == original
    generate(data, raw)
    assert (raw / "sample.py").read_bytes() == original
    assert "Enriched point." in patch.read_text()


def test_documentation_import_fails_clearly_on_operations():
    from fontlab_echopy import fontlab
    with pytest.raises(NativeUnavailable, match="FontLab"):
        fontlab.flNode()


def test_all_generated_modules_compile_and_have_explicit_annotations():
    root = Path(__file__).parents[1] / "src/fontlab_echopy"
    count = 0
    for path in list(root.rglob("*.py")) + list(root.rglob("*.pyi")):
        tree = ast.parse(path.read_text())
        compile(tree, str(path), "exec")
        if not any(line.startswith("# Generated from") for line in path.read_text().splitlines()[:2]):
            continue
        count += 1
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                assert node.returns is not None, (path, node.name)
    assert count >= 16
