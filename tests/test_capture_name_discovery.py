# this_file: tests/test_capture_name_discovery.py
"""Owned namespaces exercise complete discovery without instantiating API types."""

from types import ModuleType

import pytest

from fontlab_echopy.tooling.capture import namespace


def test_namespace_when_dir_omits_dictionary_names_then_retains_each_public_name():
    class Partial(ModuleType):
        def __dir__(self):
            return ["visible", "visible", "__doc__"]

    owned = Partial("owned")
    owned.visible, owned.hidden = 1, 2
    owned.__dict__[123] = "ignore non-string metadata key"
    result = namespace(owned, "owned")
    assert result["names"] == ["hidden", "visible"]
    assert [item["name"] for item in result["attributes"]] == ["hidden", "visible"]
    assert result["errors"] == []


def test_namespace_when_class_dir_omits_members_then_keeps_descriptors_without_calling():
    class Partial(type):
        def __dir__(cls):
            return []

    class Owned(metaclass=Partial):
        @property
        def dangerous(self):
            raise AssertionError("Do not instantiate or evaluate instance properties")

        def operation(self, count=3):
            raise AssertionError("Do not invoke API methods")

    result = namespace(Owned, "Owned", False)
    assert result["names"] == ["dangerous", "operation"]
    assert result["attributes"][0]["name"] == "dangerous"
    assert result["functions"][0]["signature"] == "(self, count=3)"


@pytest.mark.parametrize("failing", ["__dir__", "__dict__"])
def test_namespace_when_one_name_source_fails_then_keeps_other_source_and_error(failing):
    class Owned:
        visible = 7

        def __init__(self):
            self.visible = 7

        def __dir__(self):
            if failing == "__dir__":
                raise ValueError("owned discovery failure")
            return ["visible"]

        def __getattribute__(self, name):
            if name == failing == "__dict__":
                raise ValueError("owned dictionary failure")
            return object.__getattribute__(self, name)

    result = namespace(Owned(), "Owned")
    assert result["names"] == ["visible"]
    assert result["errors"] == [{"name": failing, "error": "ValueError"}]


@pytest.mark.parametrize("failing", ["__dir__", "__dict__"])
def test_namespace_when_name_discovery_times_out_then_propagates_cancellation(failing):
    class Owned:
        def __dir__(self):
            if failing == "__dir__":
                raise TimeoutError("owned deadline")
            return []

        def __getattribute__(self, name):
            if name == failing == "__dict__":
                raise TimeoutError("owned deadline")
            return object.__getattribute__(self, name)

    with pytest.raises(TimeoutError, match="owned deadline"):
        namespace(Owned(), "Owned")


def test_namespace_when_object_has_slots_only_then_dictionary_absence_is_normal():
    class Owned:
        __slots__ = ()

        def __dir__(self):
            return []

    assert namespace(Owned(), "Owned")["errors"] == []
