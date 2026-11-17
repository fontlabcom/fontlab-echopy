# this_file: tests/test_runtime_edges.py
"""Boundary checks for missing modules, pseudo namespaces and regeneration."""
import json
import sys
import types
import subprocess
from pathlib import Path

import pytest

from fontlab_echopy._runtime import bind, resolve
from fontlab_echopy.tooling.generate import generate
from fontlab_echopy.tooling.merge import merge
from fontlab_echopy.tooling.enrich import download


def test_nonimportable_pythonqt_child_resolves_through_native_root(monkeypatch):
    root = types.ModuleType("fake_echopy")
    root.Config = types.SimpleNamespace(enabled=True)
    monkeypatch.setitem(sys.modules, root.__name__, root)
    assert resolve("fake_echopy.Config") is root.Config
    assert resolve("fake_echopy.absent") is None


def test_child_facade_import_does_not_overwrite_native_object(monkeypatch):
    native = types.ModuleType("fake_echopy")
    original = types.SimpleNamespace(value=42)
    native.Config = original
    monkeypatch.setitem(sys.modules, native.__name__, native)
    parent = types.ModuleType("parent_facade")
    child = types.ModuleType("child_facade")
    monkeypatch.setitem(sys.modules, parent.__name__, parent)
    monkeypatch.setitem(sys.modules, child.__name__, child)
    bind(parent.__dict__, "fake_echopy")
    bind(child.__dict__, "fake_echopy.Config")
    parent.Config = child
    assert native.Config is original
    assert parent.Config is original
    assert child.value == 42


def test_native_import_dependency_failure_is_not_suppressed(tmp_path, monkeypatch):
    (tmp_path / "broken_echopy.py").write_text("import nonexistent_echopy_dependency")
    monkeypatch.syspath_prepend(str(tmp_path))
    with pytest.raises(ModuleNotFoundError, match="nonexistent_echopy_dependency"):
        resolve("broken_echopy")


def test_cpp_nested_names_have_static_source_and_native_lookup(tmp_path):
    data = {"modules": {"native": {"namespace": {"names": ["Outer::Inner"], "classes": [{"name": "Outer::Inner"}]}}}}
    report = generate(data, tmp_path)
    source = (tmp_path / "native.py").read_text()
    assert "class Outer__Inner:" in source
    assert "__echopy_source_aliases__ = {'Outer::Inner': 'Outer__Inner'}" in source
    assert not report["modules"]["native"]["missing_names"]
    compile(source, "native.py", "exec")


def test_merge_rejects_same_folder_and_bad_overlay(tmp_path):
    with pytest.raises(ValueError, match="must differ"):
        merge(tmp_path, tmp_path, [])
    patch = tmp_path / "bad.json"
    patch.write_text("not json")
    with pytest.raises(json.JSONDecodeError):
        merge(tmp_path, tmp_path / "out", [patch])


def test_cached_wheel_hash_mismatch_is_rejected_without_network(tmp_path):
    file = tmp_path / "wheel.whl"
    file.write_bytes(b"corrupt")
    with pytest.raises(ValueError, match="SHA256 mismatch"):
        download("https://example.invalid/wheel", file, "0" * 64)


def test_alias_imports_share_canonical_module_identity():
    import echopy.fontlab
    import fontlab_echopy.fontlab
    import echopy.PythonQt.Config
    import fontlab_echopy.PythonQt.Config
    assert echopy.fontlab is fontlab_echopy.fontlab
    assert sys.modules["echopy.PythonQt.Config"] is sys.modules["fontlab_echopy.PythonQt.Config"]


def test_committed_native_coverage_has_no_missing_names():
    path = Path(__file__).parents[1] / "reports/native-coverage.json"
    report = json.loads(path.read_text())
    assert report["unavailable"] == []
    assert len(report["modules"]) == 17
    assert all(not row["missing_names"] for row in report["modules"].values())
    assert all(not row["missing_class_members"] for row in report["modules"].values())
    assert all(not row["inspection_errors"] and not row["class_inspection_errors"] for row in report["modules"].values())


def test_regeneration_removes_only_stale_generated_modules(tmp_path):
    generate({"modules": {"old": {"namespace": {}}}}, tmp_path)
    manual = tmp_path / "manual.py"
    manual.write_text("# preserved handwritten support\n")
    generate({"modules": {"new": {"namespace": {}}}}, tmp_path)
    assert not (tmp_path / "old.py").exists()
    assert (tmp_path / "new.py").exists()
    assert manual.read_text() == "# preserved handwritten support\n"


def test_alias_import_is_lazy_in_fresh_interpreter():
    result = subprocess.run([sys.executable, "-c", "import sys; from echopy import fontlab; assert 'fontlab_echopy.PythonQt.Qt' not in sys.modules; assert fontlab.__spec__.name == 'fontlab_echopy.fontlab'"], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_pipeline_without_host_preserves_existing_output(tmp_path, capsys):
    from fontlab_echopy.tooling.cli import main
    raw = tmp_path / "raw"
    raw.mkdir()
    sentinel = raw / "existing.py"
    sentinel.write_text("# existing output\n")
    with pytest.raises(SystemExit) as exc:
        main(["pipeline", "--raw", str(raw), "--output", str(tmp_path / "merged")])
    assert exc.value.code == 2
    assert "requires FontLab or --capture" in capsys.readouterr().err
    assert sentinel.read_text() == "# existing output\n"


def test_capture_propagates_host_timeout_instead_of_recording_a_gap():
    from fontlab_echopy.tooling.capture import namespace
    class Deadline:
        def __dir__(self):
            return ["expired"]
        @property
        def expired(self):
            raise TimeoutError("host deadline expired")
    with pytest.raises(TimeoutError, match="host deadline expired"):
        namespace(Deadline(), "deadline")
