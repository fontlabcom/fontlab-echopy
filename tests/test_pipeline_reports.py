# this_file: tests/test_pipeline_reports.py
"""A fresh generation must update the reports consumed by documentation."""

import hashlib
import json

import pytest

from fontlab_echopy.tooling.cli import main


def test_pipeline_when_capture_changes_then_current_reports_match_generated_source(
    tmp_path,
):
    data = {
        "schema": 1,
        "modules": {
            "fontlab": {
                "available": True,
                "namespace": {
                    "names": ["get_value"],
                    "functions": [
                        {
                            "name": "get_value",
                            "signature": "() -> int",
                            "doc": "Read a value.",
                        }
                    ],
                },
            }
        },
    }
    capture = tmp_path / "capture.json"
    capture.write_text(json.dumps(data))
    reports = tmp_path / "reports"
    main(
        [
            "pipeline",
            "--capture",
            str(capture),
            "--raw",
            str(tmp_path / "raw"),
            "--output",
            str(tmp_path / "merged"),
            "--reports",
            str(reports),
        ]
    )
    current = json.loads((reports / "native-coverage.json").read_text())
    assert current["modules"]["fontlab"]["native_names"] == 1
    assert current["modules"]["fontlab"]["missing_names"] == []
    assert (tmp_path / "merged" / "fontlab.pyi").exists()
    pipeline = json.loads((reports / "pipeline.json").read_text())
    assert (
        pipeline["capture_identity"]["sha256"]
        == hashlib.sha256(capture.read_bytes()).hexdigest()
    )


def test_pipeline_when_overlay_requested_without_cache_then_rejected_before_output(
    tmp_path,
):
    output = tmp_path / "merged"
    with pytest.raises(SystemExit) as caught:
        main(
            [
                "pipeline",
                "--raw",
                str(tmp_path / "raw"),
                "--output",
                str(output),
                "--qt-overlay",
                str(tmp_path / "qt.json"),
            ]
        )
    assert caught.value.code == 2
    assert not output.exists(), (
        "invalid pipeline options must fail before capture or mutation"
    )
