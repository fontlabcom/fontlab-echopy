# this_file: tests/test_identities.py
"""The capture identity manifest lets documentation reconcile every native name."""

import hashlib
import json

import pytest

from fontlab_echopy.tooling.cli import main
from fontlab_echopy.tooling.identities import (
    MANIFEST,
    derive_identities,
    verify_identities,
    write_identities,
)

CAPTURE = {
    "schema": 1,
    "modules": {
        "fontlab": {
            "available": True,
            "namespace": {
                "names": ["Box::Inner", "Node", "get_value"],
                "classes": [
                    {
                        "name": "Box::Inner",
                        "names": ["size"],
                        "constructors": [{"name": "__init__"}],
                        "attributes": [{"name": "size", "type": "int"}],
                    },
                    {
                        "name": "Node",
                        "names": ["None", "_private", "raise", "x"],
                        "constructors": [{"name": "__init__"}],
                        "methods": [
                            {"name": "_private", "signature": "(...)"},
                            {"name": "raise", "signature": "(...)"},
                        ],
                        "attributes": [
                            {"name": "None", "type": "int"},
                            {"name": "x", "type": "int"},
                        ],
                    },
                ],
                "functions": [{"name": "get_value", "signature": "() -> int"}],
            },
            "subpackages": {},
        },
        "fontlabpr": {
            "available": False,
            "reason": "native module absent",
            "namespace": {},
        },
    },
}


def _package(tmp_path, capture=CAPTURE, extensions=("fontlab.Node.helper",)):
    """Write a capture and the merged-package files the manifest is derived from."""
    capture_path = tmp_path / "capture.json"
    capture_path.write_text(json.dumps(capture))
    package = tmp_path / "fontlab_echopy"
    package.mkdir()
    provenance = {
        "capture_identity": {
            "sha256": hashlib.sha256(capture_path.read_bytes()).hexdigest()
        },
        "merge": {"applied": 3, "unmatched": []},
        "qt_enrichment": {
            "qt_document_failures": {"QFoo": "HTTP Error 404: Not Found"},
            "unmatched_native_classes": ["ActionBase"],
        },
    }
    (package / "_provenance.json").write_text(json.dumps(provenance))
    registry = "".join(f"    {name!r}: _extension_{i},\n" for i, name in enumerate(extensions))
    (package / "_patch_extensions.py").write_text(
        "def _extension_0(self): ...\nEXTENSIONS = {\n" + registry + "}\n"
    )
    (package / "fontlab.pyi").write_text("class Node: ...\n")
    return capture_path, package


def test_derive_when_names_are_sanitized_then_native_spellings_map_every_identity(
    tmp_path,
):
    capture, package = _package(tmp_path)
    manifest = derive_identities(capture, package)
    spellings = manifest["native_spellings"]
    assert spellings["fontlab.Box::Inner"] == "fontlab.Box__Inner"
    assert spellings["fontlab.Box::Inner.size"] == "fontlab.Box__Inner.size", (
        "members of a renamed class must map to the renamed parent"
    )
    assert spellings["fontlab.Box::Inner.__init__"] == "fontlab.Box__Inner.__init__"
    assert spellings["fontlab.Node.raise"] == "fontlab.Node.raise_"
    assert spellings["fontlab.Node.None"] == "fontlab.Node.None_"
    assert "fontlab.Node._private" not in spellings, "valid private names keep spelling"
    assert "fontlab.Node.x" not in spellings
    node = manifest["scopes"]["fontlab"]["classes"]["Node"]
    assert node["members"] == ["None", "_private", "raise", "x"]
    assert node["constructors"] == ["__init__"]
    assert manifest["capture_sha256"] == hashlib.sha256(capture.read_bytes()).hexdigest()
    assert manifest["maintained_extensions"] == ["fontlab.Node.helper"]
    assert manifest["scopes"]["fontlabpr"] == {
        "available": False,
        "reason": "native module absent",
        "kind": "module",
        "names": [],
        "errors": [],
        "classes": {},
    }
    assert manifest["enrichment_gaps"]["qt_document_failures"] == {
        "QFoo": "HTTP Error 404: Not Found"
    }


def test_derive_when_two_native_names_share_a_source_name_then_rejected(tmp_path):
    capture = json.loads(json.dumps(CAPTURE))
    node = capture["modules"]["fontlab"]["namespace"]["classes"][1]
    node["names"].append("raise_")
    capture_path, package = _package(tmp_path, capture)
    with pytest.raises(ValueError, match="raise_"):
        derive_identities(capture_path, package)


def test_derive_when_capture_differs_from_generation_input_then_rejected(tmp_path):
    capture, package = _package(tmp_path)
    capture.write_text(json.dumps(CAPTURE) + "\n")
    with pytest.raises(ValueError, match="capture"):
        derive_identities(capture, package)


def test_write_when_manifest_derived_then_only_manifest_changes(tmp_path):
    capture, package = _package(tmp_path)
    before = {p.name: p.read_bytes() for p in package.iterdir()}
    write_identities(capture, package)
    after = {p.name: p.read_bytes() for p in package.iterdir()}
    assert set(after) - set(before) == {MANIFEST}
    assert {name: after[name] for name in before} == before, "sidecars were rewritten"


def test_verify_when_manifest_edited_or_capture_missing_then_fails(tmp_path):
    capture, package = _package(tmp_path)
    write_identities(capture, package)
    verify_identities(capture, package)
    path = package / MANIFEST
    data = json.loads(path.read_text())
    data["scopes"]["fontlab"]["classes"]["Node"]["members"].remove("x")
    path.write_text(json.dumps(data))
    with pytest.raises(ValueError, match="differs"):
        verify_identities(capture, package)
    with pytest.raises(FileNotFoundError):
        verify_identities(tmp_path / "missing.json", package)


def test_pipeline_when_run_then_manifest_matches_generated_source(tmp_path):
    capture = tmp_path / "capture.json"
    capture.write_text(json.dumps(CAPTURE))
    output = tmp_path / "merged"
    main(
        [
            "pipeline",
            "--capture",
            str(capture),
            "--raw",
            str(tmp_path / "raw"),
            "--output",
            str(output),
        ]
    )
    manifest = json.loads((output / MANIFEST).read_text())
    stub = (output / "fontlab.pyi").read_text()
    for source in ("class Box__Inner", "def raise_(", "None_:", "def _private("):
        assert source in stub, f"{source} missing from generated sidecar"
    assert manifest["native_spellings"]["fontlab.Node.raise"] == "fontlab.Node.raise_"
    main(["verify-identities", str(capture), str(output)])


def test_generate_and_merge_when_capture_changes_then_manifest_never_stale(tmp_path):
    """R-L5 P1: pipeline from A, then generate+merge from B must not keep A's manifest."""
    capture_a = tmp_path / "a.json"
    capture_a.write_text(json.dumps(CAPTURE))
    capture_b_data = json.loads(json.dumps(CAPTURE))
    capture_b_data["modules"]["fontlab"]["namespace"]["names"].append("extra")
    capture_b_data["modules"]["fontlab"]["namespace"]["functions"].append({"name": "extra"})
    capture_b = tmp_path / "b.json"
    capture_b.write_text(json.dumps(capture_b_data))
    raw, output = tmp_path / "raw", tmp_path / "merged"
    main(["pipeline", "--capture", str(capture_a), "--raw", str(raw), "--output", str(output)])
    main(["generate", str(capture_b), str(raw)])
    main(["merge", str(raw), str(output)])
    assert not (output / MANIFEST).exists(), "merge left a manifest from another capture"
    provenance = json.loads((output / "_provenance.json").read_text())
    assert provenance["capture_identity"]["sha256"] == hashlib.sha256(capture_b.read_bytes()).hexdigest()
    main(["identities", str(capture_b), str(output)])
    with pytest.raises(ValueError, match="not the generation input"):
        verify_identities(capture_a, output)
    verify_identities(capture_b, output)


def test_derive_when_capture_lacks_names_arrays_then_declarations_supply_them(tmp_path):
    """R-L5 P2: legacy-style captures without `names` must not lose identities."""
    legacy = {"schema": 1, "modules": {"fontlab": {"available": True, "namespace": {
        "classes": [{"name": "Node", "methods": [{"name": "move"}, {"name": "raise"}],
                     "attributes": [{"name": "x"}], "constructors": [{"name": "__init__"}]}],
        "functions": [{"name": "get_value"}],
        "attributes": [{"name": "VERSION"}],
    }, "subpackages": {}}}}
    capture, package = _package(tmp_path, legacy)
    manifest = derive_identities(capture, package)
    scope = manifest["scopes"]["fontlab"]
    assert scope["names"] == ["Node", "VERSION", "get_value"]
    assert scope["classes"]["Node"]["members"] == ["move", "raise", "x"]
    assert manifest["native_spellings"]["fontlab.Node.raise"] == "fontlab.Node.raise_"


def test_pipeline_when_module_retained_then_old_rows_kept_and_tampering_fails(tmp_path):
    """--retain keeps one module's raw files and identities from the earlier capture."""
    first = tmp_path / "a.json"
    first.write_text(json.dumps(CAPTURE))
    raw, output = tmp_path / "raw", tmp_path / "merged"
    main(["pipeline", "--capture", str(first), "--raw", str(raw), "--output", str(output)])
    old_raw = (raw / "fontlab.py").read_bytes()
    old_row = json.loads((output / MANIFEST).read_text())["scopes"]["fontlab"]
    newer = json.loads(json.dumps(CAPTURE))
    newer["modules"]["fontlab"]["namespace"]["names"].remove("Node")
    newer["modules"]["fontlab"]["namespace"]["classes"].pop()
    newer["modules"]["fontlabpr"] = {"available": True, "namespace": {"names": []}}
    second = tmp_path / "b.json"
    second.write_text(json.dumps(newer))
    main(["pipeline", "--capture", str(second), "--raw", str(raw), "--output", str(output),
          "--retain", "fontlab"])
    assert (raw / "fontlab.py").read_bytes() == old_raw, "retained raw module was regenerated"
    manifest = verify_identities(second, output)
    assert manifest["scopes"]["fontlab"] == old_row
    assert manifest["scopes"]["fontlabpr"]["available"] is True, "other modules use the new capture"
    old_sha = hashlib.sha256(first.read_bytes()).hexdigest()
    assert manifest["retained_scopes"]["fontlab"]["capture_sha256"] == old_sha
    coverage = json.loads((raw / "coverage.json").read_text())
    assert "fontlab" in coverage["modules"] and "retained_scopes" in coverage
    kept = output / "_retained_identities.json"
    kept.write_text(kept.read_text().replace('"x"', '"y"'))
    with pytest.raises(ValueError, match="does not match the hash"):
        verify_identities(second, output)


def test_verify_when_native_scope_tampered_with_module_retained_then_fails(tmp_path):
    """Retaining one module must not weaken the check of scopes from the new capture."""
    first = tmp_path / "a.json"
    first.write_text(json.dumps(CAPTURE))
    raw, output = tmp_path / "raw", tmp_path / "merged"
    main(["pipeline", "--capture", str(first), "--raw", str(raw), "--output", str(output)])
    newer = json.loads(json.dumps(CAPTURE))
    newer["modules"]["fontlabpr"] = {"available": True, "namespace": {"names": []}}
    second = tmp_path / "b.json"
    second.write_text(json.dumps(newer))
    main(["pipeline", "--capture", str(second), "--raw", str(raw), "--output", str(output),
          "--retain", "fontlab"])
    verify_identities(second, output)
    manifest = json.loads((output / MANIFEST).read_text())
    manifest["scopes"]["fontlabpr"]["available"] = False
    (output / MANIFEST).write_text(json.dumps(manifest))
    with pytest.raises(ValueError):
        verify_identities(second, output)


@pytest.mark.parametrize(
    ("extra", "message"),
    [
        (["--retain", "PythonQt", "--qt-cache", "cache"], "cannot be combined with --qt-cache"),
        (["--retain", "PythonQt.private"], "top-level module names"),
        (["--retain", "nosuch"], "no earlier coverage"),
    ],
)
def test_pipeline_when_retain_invalid_then_argument_error_and_nothing_written(
    tmp_path, capsys, extra, message
):
    """Bad --retain values fail before generation and leave no retained file."""
    first = tmp_path / "a.json"
    first.write_text(json.dumps(CAPTURE))
    raw, output = tmp_path / "raw", tmp_path / "merged"
    main(["pipeline", "--capture", str(first), "--raw", str(raw), "--output", str(output)])
    with pytest.raises(SystemExit):
        main(["pipeline", "--capture", str(first), "--raw", str(raw), "--output", str(output),
              *[str(tmp_path / x) if x == "cache" else x for x in extra]])
    assert message in capsys.readouterr().err
    assert not (output / "_retained_identities.json").exists()


def test_merge_when_extension_registry_changes_then_manifest_is_dropped(tmp_path):
    """An overlay that adds an extension must not keep the old manifest's registry."""
    capture = tmp_path / "capture.json"
    capture.write_text(json.dumps(CAPTURE))
    raw, output = tmp_path / "raw", tmp_path / "merged"
    main(["pipeline", "--capture", str(capture), "--raw", str(raw), "--output", str(output)])
    assert (output / MANIFEST).exists(), "pipeline should write the manifest"
    main(["merge", str(raw), str(output)])
    assert (output / MANIFEST).exists(), "an unchanged re-merge must keep the manifest"
    overlay = tmp_path / "overlay.json"
    overlay.write_text(json.dumps({"fontlab.Node": {"extensions": [
        "def helper(self) -> int:\n    return 1"]}}))
    main(["merge", str(raw), str(output), "--overlay", str(overlay)])
    assert not (output / MANIFEST).exists(), "merge kept a manifest with an old extension registry"
    main(["identities", str(capture), str(output)])
    assert json.loads((output / MANIFEST).read_text())["maintained_extensions"] == ["fontlab.Node.helper"]
    verify_identities(capture, output)
