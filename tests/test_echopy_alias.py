# this_file: tests/test_echopy_alias.py
"""The `echopy` alias package: lazy attributes, unknown names, and FL listing."""

import importlib

import pytest

import echopy


def test_alias_attribute_when_listed_then_lazily_imports_canonical_module():
    import fontlab_echopy.fontgate

    assert echopy.fontgate is fontlab_echopy.fontgate


def test_alias_attribute_when_unknown_then_attribute_error():
    with pytest.raises(AttributeError):
        echopy.no_such_module


def test_alias_import_when_canonical_module_missing_then_module_not_found():
    with pytest.raises(ModuleNotFoundError):
        importlib.import_module("echopy.no_such_module")


def test_alias_all_when_fl_shim_generated_then_lists_fl(monkeypatch):
    import pathlib

    assert "FL" in importlib.reload(echopy).__all__, "the generated FL shim is shipped"
    real = pathlib.Path.exists
    monkeypatch.setattr(pathlib.Path, "exists", lambda self: False if self.name == "FL.py" else real(self))
    try:
        assert "FL" not in importlib.reload(echopy).__all__
    finally:
        monkeypatch.undo()
        importlib.reload(echopy)


def test_alias_import_when_fresh_then_canonical_package_not_imported():
    import subprocess
    import sys

    code = "import sys, echopy; assert 'fontlab_echopy' not in sys.modules"
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
