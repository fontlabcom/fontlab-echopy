# this_file: tests/test_generation_reserved_names.py
"""Captured top-level names must not replace generated helper bindings."""
import pytest
from fontlab_echopy.tooling.generate import generate


@pytest.mark.parametrize("name", ["_bind", "_unavailable", "globals", "Any", "_echopy_native", "_echopy_name", "_echopy_aliases", "_echopy_unavailable", "-bind"])
@pytest.mark.parametrize("kind", ["classes", "functions", "attributes", "constants", "modules", "inventory"])
def test_reserved_module_name_refused_before_any_output_changes(tmp_path, name, kind):
    previous = tmp_path / "prior.py"
    previous.write_bytes(b"# Retain previous generated output\n")
    scope = {"names": [name]} if kind == "inventory" else {kind: [{"name": name}]}
    capture = {"modules": {"a_safe": {"namespace": {}}, "z_conflict": {"namespace": scope}}}
    with pytest.raises(ValueError, match="Reserved source name.*z_conflict"):
        generate(capture, tmp_path)
    assert list(tmp_path.iterdir()) == [previous]
    assert previous.read_bytes() == b"# Retain previous generated output\n"


def test_reserved_spellings_in_class_members_do_not_shadow_module_helpers(tmp_path):
    scope = {"classes": [{"name": "Fixture", "methods": [{"name": "_bind"}, {"name": "globals"}]}]}
    report = generate({"modules": {"owned": {"namespace": scope}}}, tmp_path)
    assert report["modules"]["owned"]["missing_names"] == []
