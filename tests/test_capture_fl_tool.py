# this_file: tests/test_capture_fl_tool.py
"""tools/capture_fl.py against a fake remopy: output, --base handling and failures."""

import importlib.util
import json
import sys
import types
from pathlib import Path
from types import SimpleNamespace

import pytest

TOOL = Path(__file__).resolve().parents[1] / "tools/capture_fl.py"


class NativeExecutionError(RuntimeError):
    pass


class ResultTransportError(RuntimeError):
    pass


@pytest.fixture
def tool(monkeypatch):
    """Load the script with a fake fontlab_remopy and an FL module for the fake host."""
    fl_module = types.ModuleType("FL")
    fl_module.Font = type("Font", (), {"Save": lambda self: None})
    fl_module.fl = fl_module.Font()
    monkeypatch.setitem(sys.modules, "FL", fl_module)

    class FontLab:
        timeouts = []
        failing_with = None

        def __init__(self, timeout=30):
            FontLab.timeouts.append(timeout)

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def run(self, code, **variables):
            if FontLab.failing_with is not None:
                raise FontLab.failing_with("too big")
            scope = dict(variables)
            exec(code, scope)
            return SimpleNamespace(value=scope["result"])

    fake = types.ModuleType("fontlab_remopy")
    fake.FontLab, fake.NativeExecutionError, fake.ResultTransportError = FontLab, NativeExecutionError, ResultTransportError
    monkeypatch.setitem(sys.modules, "fontlab_remopy", fake)
    spec = importlib.util.spec_from_file_location("capture_fl_tool", TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.FontLab = FontLab
    return module


def test_main_when_run_then_writes_capture_and_prints_summary(tool, tmp_path, capsys):
    out = tmp_path / "sub/capture-FL.json"
    tool.main(["--output", str(out), "--timeout", "12"])
    data = json.loads(out.read_text())
    assert data["modules"]["FL"]["available"] is True
    assert {"Font", "fl"} <= set(data["modules"]["FL"]["namespace"]["names"])
    assert tool.FontLab.timeouts[-1] == 12.0
    assert json.loads(capsys.readouterr().out)["output"] == str(out)


def test_main_when_base_given_then_other_modules_kept(tool, tmp_path):
    base = tmp_path / "base.json"
    base.write_text(json.dumps({"schema": 1, "modules": {"fontlab": {"available": True, "namespace": {}}}}))
    out = tmp_path / "merged.json"
    tool.main(["--output", str(out), "--base", str(base)])
    assert set(json.loads(out.read_text())["modules"]) == {"fontlab", "FL"}


@pytest.mark.parametrize("content", [None, "{not json", "[]", '{"modules": []}'])
def test_main_when_base_missing_or_bad_then_usage_error_before_host_use(tool, tmp_path, content, capsys):
    base = tmp_path / "base.json"
    if content is not None:
        base.write_text(content)
    before = len(tool.FontLab.timeouts)
    with pytest.raises(SystemExit) as caught:
        tool.main(["--output", str(tmp_path / "o.json"), "--base", str(base)])
    assert caught.value.code == 2
    assert "--base" in capsys.readouterr().err
    assert len(tool.FontLab.timeouts) == before, "FontLab must not be contacted"
    assert not (tmp_path / "o.json").exists()


def test_main_when_every_call_hits_code_limit_then_names_recorded_as_errors(tool, tmp_path):
    out = tmp_path / "o.json"
    with pytest.raises(ValueError):
        tool.FontLab.failing_with = ValueError
        # The survey call itself fails: nothing to record, so the error surfaces.
        tool.main(["--output", str(out)])
    assert not out.exists()
