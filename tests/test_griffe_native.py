# this_file: tests/test_griffe_native.py
"""An actual native class must not become an empty documentation module."""

import griffe

from fontlab_echopy.tooling.docnames import export_docnames
from fontlab_echopy.tooling.griffe_native import NativeNamespaceExtension


def test_source_when_class_has_empty_namespace_facet_then_class_docs_survive(tmp_path):
    root = tmp_path / "input" / "fontlab_echopy"
    qt = root / "PythonQt"
    qt.mkdir(parents=True)
    (root / "__init__.py").write_text('"""Canonical package."""\n')
    (qt / "__init__.py").write_text('"""Runtime facade."""\n')
    (qt / "__init__.pyi").write_text('''from __future__ import annotations
from typing import Any
class BoolResult:
    """Result for bool pointer arguments."""
    def __init__(self, value: bool):
        """Initialize the captured native type."""
        ...
''')
    (qt / "BoolResult.pyi").write_text('"""Empty pseudo-namespace."""\n__all__ = []\n')
    output = tmp_path / "docnames"
    report = export_docnames(output, source=root)
    assert "PythonQt.BoolResult" in report["modules"], (
        "pseudo-namespace source evidence must remain"
    )
    assert not (output / "PythonQt/BoolResult.py").exists(), (
        "an empty namespace must not shadow the captured class"
    )
    loader = griffe.GriffeLoader(
        search_paths=[output, root.parent],
        allow_inspection=False,
        prefer_stubs_docs=True,
        extensions=griffe.load_extensions(NativeNamespaceExtension),
    )
    canonical = loader.load("fontlab_echopy")
    native = loader.load("PythonQt")
    loader.resolve_aliases(external=False)
    assert canonical.get_member("PythonQt.BoolResult").is_class
    result = native.get_member("BoolResult")
    assert result.is_class and result.path == "PythonQt.BoolResult"
    assert "bool pointer arguments" in result.docstring.value
    assert "Initialize" in result.get_member("__init__").docstring.value
