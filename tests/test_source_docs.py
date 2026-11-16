# this_file: tests/test_source_docs.py
"""Verify the public source API with the documentation consumer used by mkdocstrings."""
import ast
import json
import sys
import types
from pathlib import Path

import griffe
import pytest

from fontlab_echopy._runtime import NativeUnavailable, populate


def test_griffe_resolves_canonical_sidecars_without_runtime_inspection():
    root = Path(__file__).parents[1]
    package = griffe.load(
        "fontlab_echopy", search_paths=[root / "src"],
        allow_inspection=False, prefer_stubs_docs=True, store_source=False,
    )
    node = package.get_member("fontlab.flNode")
    assert node.path == "fontlab_echopy.fontlab.flNode"
    assert "Constructors:" in node.docstring.value
    assert "A contour node" in node.docstring.value
    resize = package.get_member("PythonQt.QtGui.QWidget.resize")
    assert "Qt 5 reference" in resize.docstring.value
    assert "Upstream PySide2 reference signatures" in resize.docstring.value
    point_x = package.get_member("PythonQt.QtCore.QPointF.x")
    assert str(point_x.returns) == "float"
    assert "Returns the x coordinate" in point_x.docstring.value
    coverage = json.loads((root / "reports/native-coverage.json").read_text())
    for name, scope in coverage["modules"].items():
        module = package.get_member(name)
        path = root / "src/fontlab_echopy" / Path(*name.split("."))
        path = path / "__init__.pyi" if path.is_dir() else path.with_suffix(".pyi")
        class_names = [node.name for node in ast.parse(path.read_text()).body if isinstance(node, ast.ClassDef)]
        # PythonQt.BoolResult is both a native class and a pseudo-namespace.
        # Griffe represents that public path as its child module (zero members).
        classes = [module.members[name] for name in class_names]
        assert len(classes) == scope.get("classes", 0), name
        assert all(cls.is_class or cls.is_module for cls in classes), name
        members = sum(len([key for key, value in cls.members.items() if not key.startswith("__") and not value.is_alias]) for cls in classes)
        assert members >= scope.get("class_members", 0), name


def test_native_populate_never_reads_documentation_source(monkeypatch):
    native = types.ModuleType("echopy_test_native")
    native.answer = 42
    monkeypatch.setitem(sys.modules, native.__name__, native)
    facade = types.ModuleType("echopy_test_facade")
    facade.__file__ = "nonexistent-documentation-sidecar.py"
    monkeypatch.setitem(sys.modules, facade.__name__, facade)
    populate(facade.__dict__, native.__name__, {})
    assert facade.answer == 42


def test_offline_sidecar_operations_raise_with_documentation_intact():
    from fontlab_echopy import fontlab
    assert "Constructors:" in fontlab.flNode.__doc__
    assert "A contour node" in fontlab.flNode.__doc__
    with pytest.raises(NativeUnavailable, match="angleTo"):
        fontlab.flNode.angleTo(None, None)
