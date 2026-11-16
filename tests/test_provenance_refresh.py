# this_file: tests/test_provenance_refresh.py
"""Regeneration must never ship stale native coverage or overlay identities."""

import hashlib
import json

from fontlab_echopy.tooling.generate import generate
from fontlab_echopy.tooling.merge import merge


def test_merge_when_capture_changes_then_packaged_provenance_refreshes_and_sources_survive(
    tmp_path,
):
    raw, output = tmp_path / "raw", tmp_path / "output"
    output.mkdir()
    original_sources = [
        {"repository": "https://example.com/original", "revision": "original-revision"}
    ]
    (output / "_provenance.json").write_text(
        json.dumps({"sources": original_sources, "native_coverage": {"stale": True}})
    )
    generate(
        {"modules": {"fontlab": {"namespace": {"classes": [{"name": "Node"}]}}}}, raw
    )
    overlay = tmp_path / "manual.json"
    overlay.write_text(
        json.dumps({"fontlab.Node": {"doc": "Readable node documentation."}})
    )
    merge(raw, output, [overlay])
    proof = json.loads((output / "_provenance.json").read_text())
    assert proof["sources"] == original_sources, "migration source history changed"
    assert proof["native_coverage"]["modules"]["fontlab"]["classes"] == 1
    assert (
        proof["overlays"][0]["sha256"]
        == hashlib.sha256(overlay.read_bytes()).hexdigest()
    )
    assert (
        proof["merged_outputs"]["fontlab.pyi"]
        == hashlib.sha256((output / "fontlab.pyi").read_bytes()).hexdigest()
    )
