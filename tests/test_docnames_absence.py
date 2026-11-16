# this_file: tests/test_docnames_absence.py
"""Documentation aliases preserve captured absence instead of inventing APIs."""

import ast

from fontlab_echopy.tooling.docnames import export_docnames


def test_optional_module_when_absent_then_note_survives_in_native_namespace(tmp_path):
    source = tmp_path / "source"
    source.mkdir()
    (source / "fontlabpr.pyi").write_text(
        '"""This optional module was absent from the captured host."""\n__all__ = []\n'
    )
    output = tmp_path / "docnames"
    report = export_docnames(output, source=source)
    doc = ast.get_docstring(ast.parse((output / "fontlabpr.py").read_text()))
    assert "absent from the captured host" in doc
    assert report["modules"]["fontlabpr"]["declared_names"] == []
