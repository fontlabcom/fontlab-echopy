# this_file: tests/test_review_fixes.py
"""Regressions for executable overlays and captured documentation provenance."""
import ast
import importlib.util
import json
import subprocess
import sys
import types
from pathlib import Path

import pytest

from fontlab_echopy.extensions import get_extension, install_extensions
from fontlab_echopy.tooling.generate import generate
from fontlab_echopy.tooling.merge import merge


def test_maintained_extension_runs_after_merge_and_explicit_install(tmp_path, monkeypatch):
    native = types.ModuleType("review_native")
    native.Point = type("Point", (), {})
    monkeypatch.setitem(sys.modules, native.__name__, native)
    data = {"modules": {native.__name__: {"namespace": {"classes": [{"name": "Point", "doc": "Captured constructor: Point(x). Native bases: object."}]}}}}
    generate(data, tmp_path / "raw")
    patch = tmp_path / "patch.json"
    patch.write_text(json.dumps({"review_native.Point": {"extensions": ["def custom(self, value: int = 42) -> int:\n    return value"]}}))
    merge(tmp_path / "raw", tmp_path / "out", [patch])
    spec = importlib.util.spec_from_file_location("review_patches", tmp_path / "out/_patch_extensions.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert not hasattr(native.Point, "custom"), "merge must not mutate native classes"
    assert install_extensions(module.EXTENSIONS) == {"review_native.Point.custom": "installed"}
    assert native.Point().custom() == 42, "merged patch body must execute"
    assert native.Point().custom(7) == 7, "patch parameters must survive generation"
    native.Point.custom = lambda self, value=0: value + 1
    assert install_extensions(module.EXTENSIONS) == {"review_native.Point.custom": "existing"}
    assert native.Point().custom() == 1, "installation must preserve existing native methods"


def test_immutable_extension_has_executable_fallback_and_missing_is_reported(monkeypatch):
    native = types.ModuleType("review_native")
    native.Point = int
    monkeypatch.setitem(sys.modules, native.__name__, native)
    specs = {"review_native.Point.custom": lambda self: int(self) + 1,
             "review_native.Missing.custom": lambda self: 42}
    statuses = install_extensions(specs)
    assert statuses["review_native.Point.custom"].startswith("immutable;")
    assert statuses["review_native.Missing.custom"] == "unavailable"
    assert get_extension("review_native.Point.custom", specs)(4) == 5
    with pytest.raises(KeyError):
        get_extension("missing", specs)


def test_manual_class_docs_preserve_captured_constructor_and_bases(tmp_path):
    doc = "Native constructors: Point(x, y).\n\nNative bases: object"
    generate({"modules": {"review": {"namespace": {"classes": [{"name": "Point", "doc": doc}]}}}}, tmp_path / "raw")
    patch = tmp_path / "patch.json"
    patch.write_text(json.dumps({"review.Point": {"doc": "Supplemental example."}}))
    merge(tmp_path / "raw", tmp_path / "out", [patch])
    tree = ast.parse((tmp_path / "out/review.pyi").read_text())
    point = next(node for node in tree.body if isinstance(node, ast.ClassDef))
    assert doc in ast.get_docstring(point), "captured native evidence must survive enrichment"
    assert "Supplemental example." in ast.get_docstring(point)


def test_offline_boolresult_class_survives_child_import():
    code = """from fontlab_echopy import PythonQt
from fontlab_echopy._runtime import NativeUnavailable
original = PythonQt.BoolResult
import fontlab_echopy.PythonQt.BoolResult
assert PythonQt.BoolResult is original, 'child bookkeeping replaced class'
try:
    PythonQt.BoolResult()
except NativeUnavailable:
    pass
else:
    raise AssertionError('offline native construction succeeded')
"""
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_committed_manual_docs_retain_all_captured_class_documentation():
    root = Path(__file__).parents[1]
    patches = json.loads((root / "patches/manual.json").read_text())
    for module in ("fontlab", "fontgate"):
        native_docs = json.loads((root / "tests/native_manual_docs.json").read_text())[module]
        merged = ast.parse((root / "src/fontlab_echopy" / (module + ".pyi")).read_text())
        docs = {node.name: ast.get_docstring(node) for node in merged.body if isinstance(node, ast.ClassDef)}
        for name, doc in native_docs.items():
            assert doc in docs[name], f"Native documentation lost: {module}.{name}"
    forbidden = {"fontlab.flGlyph": ("unicode (", "unicodes ("),
                 "fontlab.flLayer": ("layer.contours",),
                 "fontgate.fgGlyph": ("glyph.contours[",),
                 "fontgate.fgFont": ("print(font.family)",),
                 "fontgate.fgPoint": ("type (int)",)}
    for target, examples in forbidden.items():
        assert all(example not in patches[target]["doc"] for example in examples), target


def test_attribute_enrichment_preserves_captured_descriptor_doc(tmp_path):
    generate({"modules": {"review": {"namespace": {"classes": [{"name": "Point", "attributes": [{"name": "x", "type": "float", "doc": "Native X coordinate."}]}]}}}}, tmp_path / "raw")
    patch = tmp_path / "patch.json"
    patch.write_text(json.dumps({"review.Point.x": {"doc": "Supplemental coordinate example."}}))
    merge(tmp_path / "raw", tmp_path / "out", [patch])
    tree = ast.parse((tmp_path / "out/review.pyi").read_text())
    point = next(node for node in tree.body if isinstance(node, ast.ClassDef))
    index = next(index for index, node in enumerate(point.body) if isinstance(node, ast.AnnAssign) and node.target.id == "x")
    doc = point.body[index + 1].value.value
    assert "Native X coordinate." in doc
    assert "Supplemental coordinate example." in doc
