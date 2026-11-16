# this_file: tests/test_capture_pythonqt_discovery.py
"""Only owned roots, registry children and import hooks model PythonQt discovery."""

import sys
from types import ModuleType

import pytest

from fontlab_echopy.tooling import capture as tool


@pytest.fixture
def owned(monkeypatch):
    root = ModuleType("PythonQt")
    monkeypatch.setitem(sys.modules, "PythonQt", root)
    monkeypatch.setattr(tool, "QT_SEEDS", ())
    # Exclude pre-existing loaded child names without changing the real registry.
    for name in tuple(sys.modules):
        if name.startswith("PythonQt."):
            monkeypatch.delitem(sys.modules, name)
    return root


def result():
    return tool.capture(["PythonQt"])["modules"]["PythonQt"]


def child(name, marker):
    value = ModuleType("PythonQt." + name)
    setattr(value, marker, 1)
    return value


def test_capture_when_child_is_registered_without_root_attribute_then_retains_namespace(
    owned, monkeypatch
):
    monkeypatch.setitem(sys.modules, "PythonQt.QtOwned", child("QtOwned", "registered"))
    assert result()["subpackages"]["QtOwned"]["namespace"]["names"] == ["registered"]


def test_capture_when_root_and_registry_disagree_then_root_object_has_precedence(
    owned, monkeypatch
):
    owned.QtOwned = child("QtOwned", "root")
    monkeypatch.setitem(sys.modules, "PythonQt.QtOwned", child("QtOwned", "registry"))
    assert result()["subpackages"]["QtOwned"]["namespace"]["names"] == ["root"]


def test_capture_when_seed_requires_import_then_captures_imported_child(owned, monkeypatch):
    monkeypatch.setattr(tool, "QT_SEEDS", ("QtOwned",))
    imported, calls = child("QtOwned", "imported"), []
    original = tool.resolve
    monkeypatch.setattr(
        tool, "resolve", lambda name: owned if name == "PythonQt" else original(name)
    )

    def load(name):
        calls.append(name)
        assert name == "PythonQt.QtOwned"
        return imported

    monkeypatch.setattr("importlib.import_module", load)
    assert result()["subpackages"]["QtOwned"]["namespace"]["names"] == ["imported"]
    assert calls == ["PythonQt.QtOwned"]


def test_capture_when_only_nested_child_registered_then_discovers_immediate_parent(
    owned, monkeypatch
):
    monkeypatch.setitem(sys.modules, "PythonQt.QtOwned.Deep", child("QtOwned.Deep", "deep"))
    monkeypatch.setattr(tool, "resolve", lambda name: owned)
    calls = []

    def load(name):
        calls.append(name)
        assert name == "PythonQt.QtOwned"
        return child("QtOwned", "parent")

    monkeypatch.setattr("importlib.import_module", load)
    assert list(result()["subpackages"]) == ["QtOwned"]
    assert calls == ["PythonQt.QtOwned"]


def test_capture_when_root_child_is_scalar_then_never_imports_a_shadow(owned, monkeypatch):
    owned.QtOwned = 7
    monkeypatch.setattr(tool, "resolve", lambda name: owned)
    monkeypatch.setattr(
        "importlib.import_module", lambda name: pytest.fail("Scalar is authoritative")
    )
    assert result()["subpackages"] == {}


@pytest.mark.parametrize("dependency", ["PythonQt.QtOwned", "owned_missing_dependency"])
def test_capture_when_child_import_missing_then_distinguishes_absence_from_dependency_error(
    owned, monkeypatch, dependency
):
    monkeypatch.setattr(tool, "QT_SEEDS", ("QtOwned",))
    monkeypatch.setattr(tool, "resolve", lambda name: owned)

    def load(name):
        raise ModuleNotFoundError("owned import failure", name=dependency)

    monkeypatch.setattr("importlib.import_module", load)
    data = result()
    assert data["subpackages"] == {}
    expected = (
        []
        if dependency == "PythonQt.QtOwned"
        else [{"name": "QtOwned", "error": "ModuleNotFoundError"}]
    )
    assert data["namespace"]["errors"] == expected


def test_capture_when_root_child_read_fails_then_records_once_and_continues(monkeypatch, owned):
    calls = []

    class Broken(ModuleType):
        def __dir__(self):
            return ["QtBad", "QtGood"]

        def __getattribute__(self, name):
            if name == "QtBad":
                calls.append(name)
                raise ValueError("owned read failure")
            return ModuleType.__getattribute__(self, name)

    root = Broken("PythonQt")
    root.QtGood = child("QtGood", "safe")
    monkeypatch.setitem(sys.modules, "PythonQt", root)
    data = result()
    assert list(data["subpackages"]) == ["QtGood"]
    assert data["namespace"]["errors"] == [{"name": "QtBad", "error": "ValueError"}]
    assert calls == ["QtBad"], "Failed API getters must not be retried by child discovery"


@pytest.mark.parametrize("error", [ImportError, RuntimeError])
def test_capture_when_child_import_fails_then_retains_error_and_other_scopes(
    owned, monkeypatch, error
):
    owned.QtGood = child("QtGood", "safe")
    monkeypatch.setattr(tool, "QT_SEEDS", ("QtBad",))
    monkeypatch.setattr(tool, "resolve", lambda name: owned)

    def load(name):
        raise error("owned import failure")

    monkeypatch.setattr("importlib.import_module", load)
    data = result()
    assert list(data["subpackages"]) == ["QtGood"]
    assert data["namespace"]["errors"] == [{"name": "QtBad", "error": error.__name__}]


def test_capture_when_registry_changes_during_import_then_finishes_original_snapshot(
    owned, monkeypatch
):
    monkeypatch.setattr(tool, "QT_SEEDS", ("QtOwned",))
    monkeypatch.setattr(tool, "resolve", lambda name: owned)

    def load(name):
        monkeypatch.setitem(sys.modules, "PythonQt.AddedLater", child("AddedLater", "later"))
        return child("QtOwned", "original")

    monkeypatch.setattr("importlib.import_module", load)
    assert list(result()["subpackages"]) == ["QtOwned"]


@pytest.mark.parametrize("error", [TimeoutError, KeyboardInterrupt, SystemExit])
def test_capture_when_child_import_cancelled_then_propagates(owned, monkeypatch, error):
    monkeypatch.setattr(tool, "QT_SEEDS", ("QtOwned",))
    monkeypatch.setattr(tool, "resolve", lambda name: owned)

    def load(name):
        raise error("owned cancellation")

    monkeypatch.setattr("importlib.import_module", load)
    with pytest.raises(error, match="owned cancellation"):
        result()
