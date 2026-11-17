# this_file: tests/test_api91.py
"""FontLab 9.1 API records: present in the 9.1.9813 capture, guarded JSON helpers."""

import ast
from pathlib import Path

import pytest

from fontlab_echopy import api91

ROOT = Path(__file__).parents[1]


def _captured_members(module: str) -> dict[str, set[str]]:
    tree = ast.parse((ROOT / "generated" / f"{module}.py").read_text())
    classes = {}
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            classes[node.name] = {
                n.target.id if isinstance(n, ast.AnnAssign) else n.name
                for n in node.body
                if isinstance(n, (ast.AnnAssign, ast.FunctionDef))
            }
    return classes


# flPackage.info returns an Info object; its members are captured on that class.
INFO_OWNER = "fontlab.flPackage.info"


@pytest.mark.parametrize("key", sorted(api91.NEW_IN_9_1))
def test_new_in_9_1_when_checked_against_capture_then_present(key):
    """The 9.1.9813 capture declares every recorded 9.1 member in the stubs."""
    change = api91.NEW_IN_9_1[key]
    parts = change.owner.split(".")
    classes = _captured_members(parts[0])
    if len(parts) == 1:
        assert change.member in classes, f"{key} missing from capture"
    elif change.owner == INFO_OWNER:
        assert change.member in classes["Info"], f"{key} missing from capture"
    else:
        assert parts[1] in classes, f"owner {change.owner} missing from capture"
        assert change.member in classes[parts[1]], f"{key} missing from capture"
    assert change.source and change.signature.startswith(change.member)


def test_removed_in_9_1_when_checked_against_capture_then_absent():
    assert "size" not in _captured_members("fontgate")["fgBrush"]
    assert set(api91.REMOVED_IN_9_1) == {"fontgate.fgBrush.size"}


def test_pen_parameters_when_listed_then_match_source_keys():
    keys = set(api91.PenParameters.__annotations__)
    assert {
        "thickness",
        "width",
        "join",
        "cap0",
        "cap1",
        "remove_overlap",
        "tolerance",
    } <= keys
    assert len(keys) == 19
    assert api91.CAP_TYPES[5] == "fixed" and api91.JOIN_TYPES[2] == "miter"


def test_warnings_when_read_then_name_bytes_crash_and_join_int():
    text = " ".join(api91.WARNINGS)
    assert (
        "SIGBUS" in text
        and "QByteArray" in text
        and "fl#8630" in text
        and ".data()" in text
    )


INFO_KEYS = {
    k for k, c in api91.NEW_IN_9_1.items() if c.owner == "fontlab.flPackage.info"
}


def test_detect_when_outside_fontlab_then_false_and_info_not_checked():
    found = api91.detect()
    assert set(found) == set(api91.NEW_IN_9_1)
    assert INFO_KEYS and all(found[k] is None for k in INFO_KEYS)
    assert all(v is False for k, v in found.items() if k not in INFO_KEYS)


def test_detect_when_font_given_then_info_members_checked():
    class Info:
        nametablePath = None
        otherData = None

    class Font:
        info = Info()

    found = api91.detect(Font())
    assert all(found[k] is True for k in INFO_KEYS)
    assert all(api91.detect(object())[k] is False for k in INFO_KEYS)


def test_has_member_when_owner_none_then_false():
    assert api91.has_member(None, "x") is False
    assert api91.has_member(object(), "__class__") is True


class FakeQByteArray:
    def __init__(self, raw: bytes):
        self.raw = raw

    def data(self):
        return self.raw


class FakeProducer:
    seen = None

    @classmethod
    def getObjectsFromJsonData(cls, data):
        cls.seen = data
        return []


@pytest.mark.parametrize("value", [b"{}", bytearray(b"{}"), "{}"])
def test_objects_from_json_when_bytes_like_then_wrapped_before_native_call(value):
    assert api91.objects_from_json(value, FakeProducer, FakeQByteArray) == []
    assert (
        isinstance(FakeProducer.seen, FakeQByteArray) and FakeProducer.seen.raw == b"{}"
    )


def test_to_qbytearray_when_qbytearray_then_passed_through():
    qba = FakeQByteArray(b"x")
    assert api91.to_qbytearray(qba, FakeQByteArray) is qba


def test_to_qbytearray_when_other_type_then_type_error():
    with pytest.raises(TypeError, match="QByteArray, bytes"):
        api91.to_qbytearray(3, FakeQByteArray)


def test_to_qbytearray_when_outside_fontlab_then_runtime_error():
    with pytest.raises(RuntimeError, match="QByteArray is unavailable"):
        api91.to_qbytearray(b"{}")


def test_qbytearray_bytes_when_qbytearray_or_bytes_then_bytes():
    assert api91.qbytearray_bytes(FakeQByteArray(b"ab")) == b"ab"
    assert api91.qbytearray_bytes(bytearray(b"ab")) == b"ab"


def test_objects_from_json_when_outside_fontlab_then_runtime_error():
    with pytest.raises(RuntimeError, match="flModelProducer is unavailable"):
        api91.objects_from_json(b"{}")


def test_objects_from_json_when_host_lacks_9_1_then_attribute_error():
    with pytest.raises(AttributeError, match="FontLab 9.1"):
        api91.objects_from_json(b"{}", object(), FakeQByteArray)


def test_pen_parameters_when_live_read_sample_then_keys_declared():
    sample = {
        "cap0": "butt",
        "cap1": "butt",
        "join": "miter",
        "miter_limit": 2.0,
        "thickness": 0.0,
    }
    assert set(sample) <= set(api91.PenParameters.__annotations__)
    assert "join_type" not in api91.PenParameters.__annotations__


def test_fgbrush_defaults_when_recorded_then_members_are_new_in_9_1():
    members = {
        c.member for c in api91.NEW_IN_9_1.values() if c.owner == "fontgate.fgBrush"
    }
    assert set(api91.FGBRUSH_DEFAULTS) <= members
    assert api91.JOIN_TYPES[api91.FGBRUSH_DEFAULTS["join_type"]] == "miter"
    assert api91.CAP_TYPES[api91.CAP_PARAMS_DEFAULTS["type"]] == "butt"
