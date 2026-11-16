# this_file: tests/test_moved_modules.py
"""Issue 201: modules that left Echopy fail loudly and name their new home."""

import pytest

import fontlab_echopy
from fontlab_echopy import MOVED


@pytest.mark.parametrize("name", sorted(MOVED))
def test_moved_module_when_imported_then_import_error_names_new_home(name):
    with pytest.raises(ImportError, match=MOVED[name]):
        getattr(fontlab_echopy, name)
    with pytest.raises(ImportError, match=MOVED[name]):
        exec(f"from fontlab_echopy import {name}", {})


@pytest.mark.parametrize("name", sorted(MOVED))
@pytest.mark.parametrize("form", ["import fontlab_echopy.{n}", "from fontlab_echopy.{n} import x", "from fontlab_echopy.{n}.sub import y", "import fontlab_echopy.{n}.sub"])
def test_moved_module_when_submodule_imported_then_import_error_names_new_home(name, form):
    with pytest.raises(ImportError, match=MOVED[name]):
        exec(form.format(n=name), {})


def test_moved_modules_when_listed_then_not_shipped_or_exported():
    assert not set(MOVED) & set(fontlab_echopy.__all__), "moved names must not be exported"
    assert {"GlyphsApp", "vanilla", "AppKit", "fontlabapp_shim", "aidus_code_tools"} <= set(MOVED)


def test_unknown_attribute_when_accessed_then_attribute_error():
    with pytest.raises(AttributeError):
        fontlab_echopy.no_such_module
