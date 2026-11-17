# this_file: src/fontlab_echopy/api91.py
"""Python API changes in FontLab 9.1 (build 9812), recorded from the C++ source.

The shipped stubs now come from a FontLab 9.1.9813 capture and declare these
members (``fgBrush.size`` is gone). This module records each new or removed
name, its signature and its source location, and gives hasattr-based feature
detection for hosts that may still run 9.0. It also gives two guarded
helpers for the clipboard JSON calls.

Status: member presence and the QByteArray route are verified live on
FontLab 9.1.9812 (2026-11-16): every ``NEW_IN_9_1`` member exists by
``hasattr`` (``flPackage.info`` members checked on a real font's ``info``) and
``fgBrush.size`` is absent; ``QtCore.QByteArray(raw)`` round-trips through
``getObjectsFromJsonData``. Passing a Python ``bytes`` object to
``getObjectsFromJsonData`` crashes FontLab (SIGBUS in the native QByteArray
converter). Behavior (``penParameters`` writes, ``expandStroke``, ``makeStroke``,
presentation overrides, refresh calls) is read from the source and not
live-verified.
"""

from __future__ import annotations

from typing import Any, Literal, NamedTuple, TypedDict

from ._runtime import resolve

FONTLAB_VERSION = "9.1"
FONTLAB_BUILD = 9812


class PenParameters(TypedDict, total=False):
    """Keys of ``flShape.penParameters`` (Proteus pygate/pyflshape.cpp:132-154).

    The setter replaces the whole stroke: omitted keys revert to defaults, and
    ``thickness`` 0 removes the pen. ``width`` is an alias of ``thickness``.
    Send ``join`` as an int when writing (fl#8630).

    Verified live (read only) on 9.1.9812: the getter returns a plain dict with
    string ``join`` and caps, e.g. ``{'cap0': 'butt', 'cap1': 'butt',
    'join': 'miter', 'miter_limit': 2.0, 'thickness': 0.0}``. Writing is
    source-derived.
    """

    thickness: float
    width: float
    join: int | Literal["miter", "bevel", "round"]
    miter_limit: float
    proportion: float
    contrast: float
    rotation: float
    cap0: Literal["butt", "round", "square"]
    cap1: Literal["butt", "round", "square"]
    cap_offset0: float
    cap_offset1: float
    cap_shaping0: float
    cap_shaping1: float
    cap_curvature0: float
    cap_curvature1: float
    cap_rotation0: float
    cap_rotation1: float
    remove_overlap: bool
    tolerance: float


# fontgate.fgCapParams(type=0, offset=0, shaping=0, rotation=0, curvature=0.554).
CAP_TYPES = {
    0: "butt",
    1: "square",
    2: "round",
    3: "horizontal",
    4: "vertical",
    5: "fixed",
}
# fontgate.fgBrush.join_type values.
JOIN_TYPES = {0: "bevel", 1: "round", 2: "miter"}

# Defaults of a new fontgate.fgBrush() on 9.1.9812 (verified live, read only).
# cap0/cap1 default to fgCapParams(type=0, offset=0, shaping=0, rotation=0, curvature=0.554).
CAP_PARAMS_DEFAULTS = {
    "type": 0,
    "offset": 0,
    "shaping": 0,
    "rotation": 0,
    "curvature": 0.554,
}
FGBRUSH_DEFAULTS = {
    "thickness": 1.0,
    "proportion": 0.5,
    "contrast": 1.0,
    "rotation": 0.0,
    "tolerance": 1.0,
    "remove_overlap": False,
    "join_type": 2,
    "miter_limit": 3.0,
}


class Change(NamedTuple):
    """One API change: native owner, member, signature, C++ source and note."""

    owner: str
    member: str
    signature: str
    source: str
    note: str


_NEW = (
    Change(
        "fontlab.flModelProducer",
        "getClipboardDataJson",
        "getClipboardDataJson(package_id: int, upm: float, objects: list) -> QByteArray",
        "pygate/pyflmodelproducer.cpp:114",
        "Static. Objects: flContour, flShape, flLayer or flGlyph. Images are dropped; "
        "references stay unresolved; the clipboard is not touched.",
    ),
    Change(
        "fontlab.flModelProducer",
        "getObjectsFromJsonData",
        "getObjectsFromJsonData(data: QByteArray) -> list | None",
        "pygate/pyflmodelproducer.cpp:76-94",
        "Pass a QByteArray only; bytes crashes FontLab 9.1.9812 (live). Returns detached "
        "objects with fresh ids; malformed JSON returns None.",
    ),
    Change(
        "fontlab.flShape",
        "penParameters",
        "penParameters: PenParameters",
        "pygate/pyflshape.cpp:105,132-154",
        "Stroke dict; the setter replaces all keys.",
    ),
    Change(
        "fontlab.flShape",
        "expandStroke",
        "expandStroke(outer_only: bool = False) -> bool",
        "pygate/pyflshape.cpp:182",
        "Returns False when the shape has no stroke.",
    ),
    Change(
        "fontlab.SmartCornerParameters",
        "inktrap_len",
        "inktrap_len: float",
        "pygate/pygatetypeconverters.cpp:1129",
        "Default 2.0. Value struct: read, modify, then assign back to the package.",
    ),
    Change(
        "fontlab.flAxis",
        "extrapolate",
        "extrapolate: bool",
        "pygate/pyflaxis.cpp:146",
        "Default False; the UI allows up to 25% beyond the axis range.",
    ),
    Change(
        "fontlab.flGlyphInfo",
        "setActiveLayer",
        "setActiveLayer(layer: flLayer) -> bool",
        "pygate/pyflglyphinfo.cpp:128-133",
        "Presentation override.",
    ),
    Change(
        "fontlab.flGlyphInfo",
        "setLocation",
        "setLocation(location: flLocation) -> bool",
        "pygate/pyflglyphinfo.cpp:128-133",
        "Presentation override.",
    ),
    Change(
        "fontlab.flGlyphInfo",
        "clearPresentationOverride",
        "clearPresentationOverride() -> bool",
        "pygate/pyflglyphinfo.cpp:128-133",
        "Presentation override.",
    ),
    Change(
        "fontlab.flGlyphInfo",
        "activeLayer",
        "activeLayer: flLayer",
        "pygate/pyflglyphinfo.cpp:128-133",
        "Read-only.",
    ),
    Change(
        "fontlab.flGlyphInfo",
        "isEditable",
        "isEditable: bool",
        "pygate/pyflglyphinfo.cpp:128-133",
        "Read-only.",
    ),
    Change(
        "fontlab.flGlyphInfo",
        "hasPresentationOverride",
        "hasPresentationOverride: bool",
        "pygate/pyflglyphinfo.cpp:128-133",
        "Read-only.",
    ),
    Change(
        "fontlab.fgSymbol",
        "setLayerOverride",
        "setLayerOverride(layer_name: str) -> Any",
        "pygate/pyfgsymbol.cpp:127-131",
        "Presentation override.",
    ),
    Change(
        "fontlab.fgSymbol",
        "setLocation",
        "setLocation(location: flLocation) -> Any",
        "pygate/pyfgsymbol.cpp:127-131",
        "Presentation override.",
    ),
    Change(
        "fontlab.fgSymbol",
        "clearPresentationOverride",
        "clearPresentationOverride() -> Any",
        "pygate/pyfgsymbol.cpp:127-131",
        "Presentation override.",
    ),
    Change(
        "fontlab.fgSymbol",
        "location",
        "location: flLocation",
        "pygate/pyfgsymbol.cpp:127-131",
        "Read-only.",
    ),
    Change(
        "fontlab.fgSymbol",
        "hasLocation",
        "hasLocation: bool",
        "pygate/pyfgsymbol.cpp:127-131",
        "Read-only.",
    ),
    Change(
        "fontlab.flPackage.info",
        "nametablePath",
        "nametablePath: str | None",
        "pygate/pyflpackage.cpp",
        "Font Info attribute.",
    ),
    Change(
        "fontlab.flPackage.info",
        "otherData",
        "otherData: dict",
        "pygate/pyflpackage.cpp",
        "Font Info attribute.",
    ),
    Change(
        "fontlab.flPreferences",
        "editorIndependentGlyphMasters",
        "editorIndependentGlyphMasters: bool",
        "pygate/pyflpreferences.cpp:420",
        "Preference.",
    ),
    Change(
        "fontlab.flPreferences",
        "generalActivateFontWindowOnOpen",
        "generalActivateFontWindowOnOpen: bool",
        "pygate/pyflpreferences.cpp:591",
        "Preference.",
    ),
    *(
        Change(
            "fontgate.fgBrush",
            name,
            f"{name}: {kind}",
            "pyfontgate fgBrush (source not in local snapshot)",
            note,
        )
        for name, kind, note in (
            ("thickness", "float", "Stroke thickness."),
            ("proportion", "float", "0..1."),
            ("contrast", "float", "1.0 means no contrast."),
            ("rotation", "float", "Pen rotation."),
            ("tolerance", "float", "Expansion tolerance."),
            ("remove_overlap", "bool", "Remove overlap after expansion."),
            ("join_type", "int", "0 bevel, 1 round, 2 miter."),
            ("miter_limit", "float", "Miter limit."),
            ("cap0", "fgCapParams", "A copy; assign back after editing."),
            ("cap1", "fgCapParams", "A copy; assign back after editing."),
        )
    ),
    Change(
        "fontgate",
        "fgCapParams",
        "fgCapParams(type=0, offset=0, shaping=0, rotation=0, curvature=0.554)",
        "pyfontgate fgCapParams (source not in local snapshot)",
        "Cap type 0 butt, 1 square, 2 round, 3 horizontal, 4 vertical, "
        "5 fixed. Copy constructor and asDict().",
    ),
    Change(
        "fontgate.fgShape",
        "makeStroke",
        "makeStroke(cap0: fgCapParams = ..., cap1: fgCapParams = ...) "
        "-> fgShape | None",
        "pyfontgate fgShape (source not in local snapshot)",
        "Returns a detached shape.",
    ),
)
NEW_IN_9_1: dict[str, Change] = {f"{c.owner}.{c.member}": c for c in _NEW}

REMOVED_IN_9_1: dict[str, Change] = {
    "fontgate.fgBrush.size": Change(
        "fontgate.fgBrush",
        "size",
        "size: fgPoint",
        "pyfontgate fgBrush (source not in local snapshot)",
        "Removed in 9.1 (breaking). Use thickness and the other stroke members.",
    ),
}

WARNINGS = (
    (
        "Passing Python bytes to getObjectsFromJsonData crashes FontLab 9.1.9812 (SIGBUS, verified live). "
        "Pass the QByteArray from getClipboardDataJson or QtCore.QByteArray(b); never bytes, bytearray or str."
    ),
    "bytes(qbytearray) raises TypeError in FontLab's PythonQt; use qbytearray.data().",
    (
        "getClipboardDataJson, getObjectsFromJsonData, penParameters and expandStroke record no Undo and send "
        "no notifications."
    ),
    "Send penParameters['join'] as an int (fl#8630).",
    (
        "Verified live on 9.1.9812: member presence, fgBrush.size absence, the QtCore.QByteArray(raw) "
        "round trip, penParameters read (plain dict, string join/caps) and fgBrush() defaults. Behavior (penParameters writes, expandStroke, makeStroke, presentation overrides) is "
        "source-derived and not live-verified."
    ),
)


def has_member(owner: Any, member: str) -> bool:
    """Detect a feature by attribute presence; never compare build numbers."""
    return owner is not None and hasattr(owner, member)


def detect(font: Any = None) -> dict[str, bool | None]:
    """Report which 9.1 members the running host exposes; False outside FontLab; Font Info entries are None unless a font is passed.

    ``flPackage.info`` members need a font: pass ``font`` (an ``flPackage``) to
    check ``font.info``; without it those entries are ``None`` ("not checked").
    """
    found: dict[str, bool | None] = {}
    for key, change in NEW_IN_9_1.items():
        if change.owner == "fontlab.flPackage.info":
            found[key] = (
                None
                if font is None
                else has_member(getattr(font, "info", None), change.member)
            )
            continue
        found[key] = has_member(resolve(change.owner), change.member)
    return found


def _qbytearray_type() -> Any:
    qbytearray = resolve("PythonQt.QtCore.QByteArray")
    if qbytearray is None:
        raise RuntimeError(
            "PythonQt.QtCore.QByteArray is unavailable; run inside FontLab."
        )
    return qbytearray


def to_qbytearray(data: Any, qbytearray: Any = None) -> Any:
    """Wrap bytes, bytearray or str in a QByteArray; pass a QByteArray through."""
    qbytearray = qbytearray or _qbytearray_type()
    if isinstance(data, str):
        data = data.encode("utf-8")
    if isinstance(data, (bytes, bytearray)):
        return qbytearray(bytes(data))
    if isinstance(data, qbytearray):
        return data
    raise TypeError(
        f"QByteArray, bytes, bytearray or str expected, not {type(data).__name__}"
    )


def qbytearray_bytes(data: Any) -> bytes:
    """Read a QByteArray as bytes with data(); bytes(qbytearray) fails in PythonQt."""
    if isinstance(data, (bytes, bytearray)):
        return bytes(data)
    return bytes(data.data())


def objects_from_json(
    data: Any, producer: Any = None, qbytearray: Any = None
) -> list | None:
    """Call getObjectsFromJsonData safely: bytes and str are wrapped before the native call."""
    producer = producer or resolve("fontlab.flModelProducer")
    if producer is None:
        raise RuntimeError(
            "fontlab.flModelProducer is unavailable; run inside FontLab."
        )
    if not has_member(producer, "getObjectsFromJsonData"):
        raise AttributeError("getObjectsFromJsonData needs FontLab 9.1 or later")
    return producer.getObjectsFromJsonData(to_qbytearray(data, qbytearray))
