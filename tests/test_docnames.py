# this_file: tests/test_docnames.py
"""Documentation consumers should resolve native names from enriched source."""

import ast
import json

import griffe
import pytest

from fontlab_echopy.tooling.docnames import export_docnames


def test_export_when_source_available_then_native_names_are_explicit_aliases(tmp_path):
    root = tmp_path / "input" / "fontlab_echopy"
    root.mkdir(parents=True)
    (root / "fontlab.pyi").write_text('''"""Captured and enriched FontLab API."""
class flNode:
    """A contour node."""
    def angleTo(self, other: flNode) -> float:
        """The angle to another node."""
        ...
''')
    (root / "__init__.py").write_text('"""Canonical source."""\n')
    output = tmp_path / "docnames"
    report = export_docnames(output, source=root)
    text = (output / "fontlab.py").read_text()
    imports = [
        node for node in ast.parse(text).body if isinstance(node, ast.ImportFrom)
    ]
    assert [
        (node.module, [(name.name, name.asname) for name in node.names])
        for node in imports
    ] == [("fontlab_echopy.fontlab", [("flNode", "flNode")])], (
        "documentation aliases must point to the actual enriched declaration"
    )
    assert report["modules"]["fontlab"]["declared_names"] == ["flNode"]
    loader = griffe.GriffeLoader(
        search_paths=[output, root.parent],
        allow_inspection=False,
        prefer_stubs_docs=True,
    )
    loader.load("fontlab_echopy")
    native = loader.load("fontlab")
    loader.resolve_aliases(external=False)
    node = native.get_member("flNode")
    assert node.path == "fontlab.flNode", (
        "consumer should present the actual native module"
    )
    assert node.canonical_path == "fontlab_echopy.fontlab.flNode"
    assert node.docstring.value == "A contour node."
    assert str(node.get_member("angleTo").returns) == "float"
    assert "The angle" in node.get_member("angleTo").docstring.value


def test_export_when_output_inside_source_then_no_originals_modified(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    (source / "fontlab.pyi").write_text("class Original: ...\n")
    with pytest.raises(ValueError, match="outside"):
        export_docnames(source / "docs", source=source)
    assert not (source / "docs").exists()


def test_export_when_regenerated_then_bytes_and_manifest_are_deterministic(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    (source / "fontpr.pyi").write_text("def available() -> bool: ...\n")
    output = tmp_path / "output"
    first = export_docnames(output, source=source)
    content = {p.name: p.read_bytes() for p in output.iterdir()}
    second = export_docnames(output, source=source)
    assert first == second
    assert content == {p.name: p.read_bytes() for p in output.iterdir()}
    assert (
        json.loads((output / "docnames-manifest.json").read_text())["schema_version"]
        == 1
    )
    ast.parse((output / "fontpr.py").read_text())


def test_docnames_when_package_carries_shim_marker_then_exported(tmp_path):
    from fontlab_echopy.tooling.docnames import export_docnames

    source = tmp_path / "fontlab_echopy"
    (source / "dynamic_api").mkdir(parents=True)
    (source / "unmarked").mkdir()
    (source / "fontlab.pyi").write_text("class flNode: ...\n")
    (source / "dynamic_api/__init__.pyi").write_text(
        "from typing import Literal\nclass Menu: ...\nActionPath = Literal['A']\n__all__ = ['Menu']\n"
    )
    (source / "dynamic_api/_shim.json").write_text("{}\n")
    (source / "unmarked/__init__.pyi").write_text("class Helper: ...\n")
    report = export_docnames(tmp_path / "out", source=source)
    assert report["modules"]["dynamic_api"]["declared_names"] == ["ActionPath", "Menu"]
    assert "unmarked" not in report["modules"], "only marked shims are documentation namespaces"
    assert "fontlab_echopy.dynamic_api import" in (tmp_path / "out/dynamic_api/__init__.py").read_text()


def test_docnames_when_shim_reexports_then_alias_resolves_through_griffe(tmp_path):
    """R-L5 P1: imported re-exports in a shim's __all__ must reach documentation."""
    import griffe

    from fontlab_echopy.tooling.docnames import export_docnames

    source = tmp_path / "src" / "fontlab_echopy"
    (source / "dynamic_ui").mkdir(parents=True)
    (source / "fontlab.pyi").write_text("class flNode: ...\n")
    (source / "dynamic_ui/__init__.pyi").write_text(
        "from typing import Any\nfrom pkg.ui import Button as Button\n__all__ = ['Button']\n"
    )
    (source / "dynamic_ui/_shim.json").write_text("{}\n")
    (tmp_path / "src/pkg").mkdir()
    (tmp_path / "src/pkg/__init__.py").write_text("")
    (tmp_path / "src/pkg/ui.py").write_text('class Button:\n    """A push button."""\n')
    out = tmp_path / "out"
    report = export_docnames(out, source=source)
    assert report["modules"]["dynamic_ui"]["declared_names"] == ["Button"]
    assert "Any" not in report["modules"]["dynamic_ui"]["declared_names"], "typing imports are not exports"
    loader = griffe.GriffeLoader(search_paths=[out, tmp_path / "src"], allow_inspection=False)
    dynamic_ui = loader.load("dynamic_ui")
    loader.load("pkg")
    loader.resolve_aliases(implicit=True, external=True)
    assert dynamic_ui["Button"].docstring.value == "A push button."
