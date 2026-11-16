# this_file: tests/test_cli_commands.py
"""Each standalone CLI subcommand runs against a tiny capture."""

import json

import pytest

from fontlab_echopy.tooling.cli import main

CAPTURE = {
    "schema": 1,
    "modules": {
        "fontlab": {
            "available": True,
            "namespace": {
                "names": ["get_value"],
                "functions": [{"name": "get_value", "signature": "() -> int", "doc": "Read a value."}],
            },
        }
    },
}


@pytest.fixture
def capture(tmp_path):
    path = tmp_path / "capture.json"
    path.write_text(json.dumps(CAPTURE))
    return path


def test_generate_merge_identities_docnames_when_run_in_order_then_each_reports(tmp_path, capture, capsys):
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    main(["generate", str(capture), str(raw)])
    assert json.loads(capsys.readouterr().out)["modules"]["fontlab"]["native_names"] == 1
    main(["merge", str(raw), str(merged)])
    capsys.readouterr()
    main(["identities", str(capture), str(merged)])
    assert json.loads(capsys.readouterr().out)["capture_sha256"], "identities must report the capture hash"
    main(["verify-identities", str(capture), str(merged)])
    assert json.loads(capsys.readouterr().out)["scopes"] >= 1
    main(["docnames", str(tmp_path / "docs")])
    assert json.loads(capsys.readouterr().out)["manifest"] == "docnames-manifest.json"


def test_capture_when_no_native_modules_then_exit_2_and_no_output(tmp_path, capsys):
    out = tmp_path / "capture.json"
    with pytest.raises(SystemExit) as caught:
        main(["capture", str(out)])
    assert caught.value.code == 2
    assert not out.exists(), "a capture outside FontLab must not write output"
