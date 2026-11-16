# this_file: tests/test_generation_collisions.py
"""Name collisions fail before generated output can be changed."""

from copy import deepcopy

import pytest

from fontlab_echopy.tooling.generate import generate


def _capture(scope):
    return {"modules": {"fontlab": {"namespace": scope}}}


@pytest.mark.parametrize("listed", [False, True])
@pytest.mark.parametrize("member", [False, True])
def test_colliding_declarations_are_rejected_without_creating_output(tmp_path, listed, member):
    if member:
        cls = {"name": "Node", "methods": [{"name": "A-B"}],
               "attributes": [{"name": "A_B", "type": "int"}]}
        if listed:
            cls["names"] = ["A-B"]  # A partial inventory must not hide declarations.
        scope = {"classes": [cls]}
    else:
        scope = {"classes": [{"name": "A-B"}, {"name": "A_B"}]}
        if listed:
            scope["names"] = ["A-B"]
    data = _capture(scope)
    original = deepcopy(data)
    output = tmp_path / "output"
    with pytest.raises(ValueError, match="Source name collision.*A-B.*A_B"):
        generate(data, output)
    assert not output.exists()
    assert data == original


@pytest.mark.parametrize("member", [False, True])
def test_inventory_only_collisions_are_rejected(tmp_path, member):
    scope = {"names": ["A-B", "A_B"]}
    if member:
        scope = {"classes": [{"name": "Node", "names": ["A-B", "A_B"]}]}
    with pytest.raises(ValueError, match="Source name collision"):
        generate(_capture(scope), tmp_path / "output")
    assert not (tmp_path / "output").exists()


def test_later_subpackage_collision_preserves_every_existing_file(tmp_path):
    output = tmp_path / "output"
    output.mkdir()
    for name, body in {"fontlab.py": "prior module\n", "coverage.json": "prior report\n",
                       "stale.pyi": "# Generated from previous capture\n",
                       "support.py": "handwritten support\n"}.items():
        (output / name).write_text(body)
    before = {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
    data = _capture({"classes": [{"name": "Valid"}]})
    data["modules"]["fontlab"]["subpackages"] = {
        "later": {"classes": [{"name": "A-B"}, {"name": "A_B"}]}}
    with pytest.raises(ValueError, match="Source name collision in fontlab.later"):
        generate(data, output)
    assert {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()} == before
    assert sorted(p.name for p in output.iterdir()) == sorted(p.name for p in before)


def test_noncolliding_aliases_remain_valid_across_scopes(tmp_path):
    scope = {"names": ["A-B"], "classes": [{"name": "A-B", "names": ["C-D", "other"],
             "methods": [{"name": "C-D", "signature": "(self)"}],
             "attributes": [{"name": "other", "type": "int"}]}]}
    data = _capture(scope)
    data["modules"]["other"] = {"namespace": deepcopy(scope)}
    report = generate(data, tmp_path)
    for name in ("fontlab", "other"):
        source = (tmp_path / (name + ".py")).read_text()
        assert "class A_B:" in source
        assert "def C_D(" in source
        assert "__echopy_source_aliases__ = {'A-B': 'A_B'}" in source
        assert report["modules"][name]["missing_names"] == []
        assert report["modules"][name]["missing_class_members"] == {}
