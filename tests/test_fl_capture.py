# this_file: tests/test_fl_capture.py
"""FL (FontLab 5 API): chunked capture, absence record and generated shim."""

import ast
import importlib
import sys
import types
from types import SimpleNamespace

import pytest

import fontlab_echopy
from fontlab_echopy.tooling import chunked
from fontlab_echopy.tooling.capture import capture, finish_module, namespace
from fontlab_echopy.tooling.generate import generate


class Font:
    """A font."""

    def Save(self, path=None):
        """Save(path)"""

    def Close(self):
        """Close()"""


class Glyph:
    """A glyph."""

    width = property(lambda self: 1)


class FontLabApp:
    """The application object."""

    def Open(self, path):
        """Open(path)"""


def make_fl(with_all=True):
    module = types.ModuleType("FL")
    module.__doc__ = "FontLab 5 API."
    module.Font, module.Glyph, module.FontLabApp = Font, Glyph, FontLabApp
    module.fl = FontLabApp()
    module.Point = lambda x, y: (x, y)
    module.VERSION = 5
    if with_all:
        module.__all__ = ["Font", "Glyph", "fl", "Point", "VERSION"]
    return module


@pytest.fixture
def fl_module(monkeypatch):
    module = make_fl()
    monkeypatch.setitem(sys.modules, "FL", module)
    return module


def fake_run(calls=None, fail_over=None):
    """Execute remote code locally, as the host would, in a fresh namespace."""

    def run(code, **variables):
        if fail_over is not None and len(variables.get("ONLY", [])) > fail_over:
            raise RuntimeError("too big")
        if calls is not None:
            calls.append(variables.get("ONLY"))
        scope = dict(variables)
        exec(code, scope)
        return SimpleNamespace(value=scope["result"])

    return run


def test_namespace_when_instances_requested_then_instance_class_captured():
    scope = finish_module(namespace(make_fl(), "FL", instances=True), ["Font", "fl"])
    assert [c["name"] for c in scope["classes"]] == ["Font", "FontLabApp", "Glyph"], "fl's class must be captured"
    assert any(a["name"] == "fl" and a["type"] == "FontLabApp" for a in scope["attributes"])
    assert scope["exports"] == ["Font", "fl"]
    assert "instance_classes" not in scope


def test_capture_when_fl_absent_then_recorded_unavailable():
    result = capture(["FL"])
    assert result["modules"]["FL"] == {"available": False, "reason": "native module absent", "namespace": {}}


def test_capture_when_fl_present_then_star_exports_recorded(fl_module):
    scope = capture(["FL"])["modules"]["FL"]["namespace"]
    assert scope["exports"] == ["Font", "Glyph", "Point", "VERSION", "fl"]


def test_capture_when_fl_has_no_all_then_no_exports_key(monkeypatch):
    monkeypatch.setitem(sys.modules, "FL", make_fl(with_all=False))
    assert "exports" not in capture(["FL"])["modules"]["FL"]["namespace"]


def test_chunked_capture_when_budget_small_then_same_as_direct_capture(fl_module, monkeypatch):
    monkeypatch.setattr(chunked, "BUDGET", 8)
    calls = []
    item = chunked.capture_module(fake_run(calls), "FL", (RuntimeError,))
    direct = capture(["FL"])["modules"]["FL"]
    assert len(calls) > 1, "a small budget must produce several host calls"
    for key in ("classes", "functions", "attributes", "names", "exports", "errors"):
        assert item["namespace"][key] == direct["namespace"][key], key


def test_chunked_capture_when_call_fails_then_split_until_it_fits(fl_module):
    calls = []
    item = chunked.capture_module(fake_run(calls, fail_over=2), "FL", (RuntimeError,))
    assert max(len(c) for c in calls if c) <= 2
    assert {"Font", "Glyph", "fl"} <= set(item["namespace"]["names"])


def test_chunked_capture_when_single_name_fails_then_recorded_as_error_and_rest_captured(fl_module):
    inner = fake_run()

    def run(code, **variables):
        if "Glyph" in variables.get("ONLY", ()):  # fails until split down to the single name
            raise RuntimeError("boom")
        return inner(code, **variables)

    scope = chunked.capture_module(run, "FL", (RuntimeError,))["namespace"]
    assert scope["errors"] == [{"name": "Glyph", "error": "RuntimeError"}]
    assert {"name": "Glyph", "type": "Any", "doc": "Native member could not be inspected."} in scope["attributes"]
    assert "Font" in {c["name"] for c in scope["classes"]}, "other names must still be captured"


def test_chunked_capture_when_failure_type_not_listed_then_propagates(fl_module):
    with pytest.raises(RuntimeError):
        chunked.capture_module(fake_run(fail_over=0), "FL", (ValueError,))


def test_remote_source_when_capture_import_changes_then_raises(monkeypatch):
    monkeypatch.setattr(chunked, "_RESOLVE", "from nowhere import resolve")
    with pytest.raises(RuntimeError, match="no longer imports"):
        chunked.remote_source("")


def test_generate_when_exports_not_captured_then_reported(tmp_path):
    scope = {"name": "m", "names": ["a"], "attributes": [{"name": "a", "type": "int"}], "exports": ["a", "ghost"]}
    report = generate({"schema": 1, "modules": {"m": {"available": True, "namespace": scope}}}, tmp_path)
    assert report["modules"]["m"]["exports_not_captured"] == ["ghost"]
    assert "'ghost'" not in (tmp_path / "m.py").read_text()


def test_shipped_fl_shim_when_imported_offline_then_listed_and_documented():
    import fontlab_echopy
    from fontlab_echopy import FL

    assert "FL" in fontlab_echopy.__all__
    assert FL.__doc__, "FL carries its native description"
    assert hasattr(FL, "Font"), "the captured Font class is declared"


def test_chunked_capture_when_module_absent_then_unavailable_record():
    item = chunked.capture_module(fake_run(), "FL", (RuntimeError,))
    assert item == {"available": False, "reason": "native module absent", "namespace": {}}


def test_remote_source_when_built_then_needs_no_echopy_install():
    source = chunked.remote_source(chunked.CHUNK)
    assert "fontlab_echopy" not in source.replace("# this_file: src/fontlab_echopy/tooling/capture.py", "")
    assert len(source.encode()) < 16000, "must leave room under the 32 KiB host code limit"
    ast.parse(source)


def test_plan_chunks_when_sizes_given_then_groups_respect_budget():
    assert chunked.plan_chunks({"a": 5, "b": 5, "c": 5}, budget=10) == [["a", "b"], ["c"]]
    assert chunked.plan_chunks({"big": 500}, budget=10) == [["big"]]
    assert chunked.plan_chunks({}) == []


def test_generate_when_fl_captured_then_passthrough_shim_with_star_exports(fl_module, tmp_path):
    data = {"schema": 1, "modules": {"FL": chunked.capture_module(fake_run(), "FL", (RuntimeError,))}}
    report = generate(data, tmp_path)
    source = (tmp_path / "FL.py").read_text()
    ast.parse(source)
    assert "class Font:" in source and "class FontLabApp:" in source
    assert "fl: FontLabApp" in source, "the fl instance must be typed with its captured class"
    assert "__all__ = ['Font', 'Glyph', 'Point', 'VERSION', 'fl']" in source
    assert "_bind(globals(), 'FL'" in source, "inside FontLab the native module is delegated"
    assert report["modules"]["FL"]["missing_names"] == []
    assert report["modules"]["FL"]["missing_class_members"] == {}


def test_generate_when_fl_absent_then_documented_as_absent(tmp_path):
    data = {"schema": 1, "modules": {"FL": {"available": False, "reason": "native module absent", "namespace": {}}}}
    report = generate(data, tmp_path)
    assert report["unavailable"] == ["FL"]
    assert "absent" in (tmp_path / "FL.py").read_text()


def test_moved_finder_when_package_reloaded_then_single_finder_registered():
    importlib.reload(fontlab_echopy)
    importlib.reload(fontlab_echopy)
    finders = [f for f in sys.meta_path if getattr(f, "__name__", "") == "_MovedFinder"]
    assert len(finders) == 1, "reload must not stack duplicate finders"
    with pytest.raises(ImportError, match="fontlab-glyport"):
        importlib.import_module("fontlab_echopy.GlyphsApp")
