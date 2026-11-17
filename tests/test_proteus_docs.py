# this_file: tests/test_proteus_docs.py
"""Proteus/MCP reference overlays and the merge keys they rely on."""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path

from fontlab_echopy.tooling import mcp, proteus
from fontlab_echopy.tooling.merge import (
    enrich_node,
    is_placeholder_lead,
    merge,
    with_reference,
)

ROOT = Path(__file__).resolve().parents[1]

GENERATED = '''"""Python interface for FontLab data objects"""
from typing import Any
class flThing:
    """flThing representation

Constructors:
  flThing()

Native bases: object"""
    name: Any
    def fix(self, *args: Any, **kwargs: Any) -> Any:
        """bool fix()"""
class flObjectsList_flThing_:
    """flObjectsList<flThing> doc

Native bases: object"""
    def append(self, *args: Any, **kwargs: Any) -> Any:
        """void append(flThing)"""
Mode: dict
def CurrentThing(*args: Any, **kwargs: Any) -> Any:
    """CurrentThing() -> flThing"""
'''

CLASS = """# flThing — A demonstration thing.

**Python name:** `flThing`
**C++:** `flThing` in `pygate/pyflthing.h`
**Source:** `/Users/someone/pyflthing.cpp`

<!-- generated -->
Things hold [names](other.md).

```python
# not a heading
thing = flThing()
```

## Properties

| Property | Type | Description |
|---|---|---|
| `name` | `str` | The thing's name. |

## Methods

| Signature | Description |
|---|---|
| `bool fix()` | Repair the thing. |

## Tutorial

Use it gently.

## See also

- other
"""

LIST = """# flObjectsList wrappers

**Runtime type names:** `flObjectsList<flThing>`

Native lists.

| Method | Contract |
|---|---|
| `append(item)` | Add one item. |
"""

MODULE = """# Module reference

## Things

### CurrentThing()

```python
thing = fontlab.CurrentThing()
```
Return the current thing.

**Returns:** `flThing` or `None`

### Missing()

Not captured.
"""

ENUMS = """# Enums

## Mode (module dictionary)

How things behave.

| Key | Native value | Description |
|---|---|---|
| `Quiet` | `0` | Silent mode |
| `Loud` | `1` | Native enum value. |

## Class enum dictionaries

| Class | Key |
|---|---|
| x | y |
"""

OVERVIEW = """# fontlab

## Architecture

Python calls C++ objects.
- Bindings live in `pygate/pyflthing.cpp`.

## Documented Classes

Skip this.
"""


def fixture(tmp_path: Path) -> tuple[Path, Path]:
    generated = tmp_path / "generated"
    generated.mkdir()
    (generated / "fontlab.py").write_text(GENERATED)
    docs = tmp_path / "api-docs"
    (docs / "classes").mkdir(parents=True)
    (docs / "classes" / "flThing.md").write_text(CLASS)
    (docs / "classes" / "flObjectsList.md").write_text(LIST)
    (docs / "classes" / "README.md").write_text("# index\n")
    (docs / "00-overview.md").write_text(OVERVIEW)
    (docs / "01-module-reference.md").write_text(MODULE)
    (docs / "02-enums-and-constants.md").write_text(ENUMS)
    return docs, generated


def test_build_when_articles_present_then_classes_members_functions_enums_mapped(
    tmp_path,
):
    docs, generated = fixture(tmp_path)
    overlay = proteus.build(docs, generated)
    patches = overlay.patches
    thing = patches["fontlab.flThing"]["reference"]
    assert thing.startswith("A demonstration thing."), thing
    assert "Things hold names." in thing, "links must keep their text only"
    assert "# not a heading" in thing, "fenced lines are not section headings"
    assert (
        "## Tutorial" in thing
        and "## Properties" not in thing
        and "See also" not in thing
    )
    assert patches["fontlab.flThing.name"]["reference"] == "The thing's name."
    assert patches["fontlab.flThing.fix"]["reference"] == "Repair the thing."
    assert (
        patches["fontlab.flObjectsList_flThing_.append"]["reference"] == "Add one item."
    )
    assert "Return the current thing." in patches["fontlab.CurrentThing"]["reference"]
    mode = patches["fontlab.Mode"]["reference"]
    assert "- `Quiet`: Silent mode" in mode and "- `Loud`" in mode, mode
    assert "Native enum value" not in mode
    assert "Python calls C++ objects." in patches["fontlab"]["reference"]
    assert "Skip this." not in patches["fontlab"]["reference"]
    assert "fontlab.Missing" in overlay.unplaced, (
        "uncaptured names are reported, not emitted"
    )
    assert all(
        p["reference_source"] == proteus.REFERENCE_SOURCE for p in patches.values()
    )


def test_build_when_articles_name_sources_then_no_paths_or_cpp_leak(tmp_path):
    docs, generated = fixture(tmp_path)
    text = json.dumps(proteus.build(docs, generated).patches)
    for token in ("/Users/", ".cpp", "pygate/", "**C++:**", "<!--", "Python name"):
        assert token not in text, token


def test_shipped_overlays_when_scanned_then_no_machine_paths_or_cpp_sources():
    for name in ("fontlab-proteus.json", "fontpr-mcp.json"):
        text = (ROOT / "enrichment" / name).read_text()
        assert not re.search(r"/Users/|\.cpp\b|pygate/", text), name
    module = json.loads((ROOT / "enrichment/fontpr-mcp.json").read_text())["fontpr"][
        "reference"
    ]
    for secret in ("47400", "token_file", "initialize_extra_param", "127.0.0.1"):
        assert secret not in module, f"connection detail leaked: {secret}"


def test_placeholder_lead_when_stub_text_then_detected():
    assert is_placeholder_lead("flGlyph representation")
    assert is_placeholder_lead("flObjectsList<flGuideLine> doc")
    assert is_placeholder_lead("Call an MCP tool by name.")
    assert is_placeholder_lead("")
    assert not is_placeholder_lead("bool fix()")
    assert not is_placeholder_lead("A real description.")


def test_with_reference_when_placeholder_then_replaced_and_structure_kept():
    doc = "flThing representation\n\nConstructors:\n  flThing()\n\nNative bases: object"
    out = with_reference(doc, "Real text.")
    assert out.startswith("Real text.\n\nConstructors:"), out
    assert "representation" not in out and out.endswith("Native bases: object")
    assert with_reference("bool fix()", "Repair.") == "bool fix()\n\nRepair."
    assert with_reference("", "Only.") == "Only."


def test_merge_when_reference_and_manual_then_order_and_sources(tmp_path):
    docs, generated = fixture(tmp_path)
    ref = tmp_path / "ref.json"
    ref.write_text(json.dumps(proteus.build(docs, generated).patches))
    manual = tmp_path / "manual.json"
    manual.write_text(
        json.dumps({"fontlab.flThing": {"doc": "Curated note.", "source": "manual"}})
    )
    out = tmp_path / "out"
    result = merge(generated, out, [ref, manual])
    assert result["unmatched"] == []
    tree = ast.parse((out / "fontlab.pyi").read_text())
    cls = next(
        n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "flThing"
    )
    doc = ast.get_docstring(cls)
    order = [
        doc.index(s)
        for s in (
            "A demonstration",
            "Constructors:",
            "Supplemental documentation:\nCurated note.",
            f"Source: {proteus.REFERENCE_SOURCE}",
            "Source: manual",
        )
    ]
    assert order == sorted(order), doc
    assert "representation" not in doc
    names = [n for n in cls.body if isinstance(n, ast.AnnAssign)]
    assert names, "property must survive"
    assert "Repair the thing." in ast.get_docstring(
        next(n for n in cls.body if isinstance(n, ast.FunctionDef))
    )
    assert "Python calls C++ objects." in ast.get_docstring(tree)


def test_enrich_node_when_signature_patch_then_keyword_only_args():
    node = ast.parse(
        "def tool(*args, **kwargs):\n    'Call an MCP tool by name.'"
    ).body[0]
    enrich_node(
        node,
        {
            "signature": "*, name: str, count: int | None = None",
            "reference": "Does it.",
        },
    )
    text = ast.unparse(node)
    assert text.startswith("def tool(*, name: str, count: int | None=None):"), text
    assert "Does it." in text and "Call an MCP" not in text


SPEC = {
    "targeting": {"font": "Use font_id."},
    "agent_rules": ["Inspect first."],
    "known_limitations": [{"id": "non-atomic", "detail": "No transactions."}],
    "connection": {"token": "SECRET"},
    "tools": [
        {
            "name": "rename_glyph",
            "description": "Rename one glyph.",
            "destructive": True,
            "effect": "glyph mutation",
            "result": "{status}",
            "notes": ["Undo supported."],
            "examples": [
                {
                    "purpose": "Rename a",
                    "arguments": {"glyph_name": "a", "new_name": "b"},
                }
            ],
            "inputSchema": {
                "properties": {
                    "font_id": {"type": "number", "description": "Font."},
                    "glyph_name": {"type": "string", "description": "Old."},
                    "new_name": {"type": "string", "description": "New."},
                    "mode": {"type": "string", "enum": ["a", "b"]},
                    "names": {"type": "array", "items": {"type": "string"}},
                },
                "required": ["glyph_name", "new_name"],
                "additionalProperties": False,
            },
        },
        {"name": "spec_only", "description": "x", "inputSchema": {}},
        {"name": "run_python", "description": "x", "inputSchema": {}},
    ],
}


def test_mcp_build_when_spec_and_capture_then_only_shared_tools_documented():
    patches, report = mcp.build(
        SPEC, {"rename_glyph", "capture_only", "available", "call", "list_tools"}
    )
    assert set(patches) == {"fontpr", "fontpr.rename_glyph"}
    assert report["spec_only"] == ["run_python", "spec_only"]
    assert report["capture_only"] == ["capture_only"]
    assert report["blocked_in_spec"] == ["run_python"]
    tool = patches["fontpr.rename_glyph"]
    assert tool["signature"] == (
        "*, glyph_name: str, new_name: str, font_id: float | None = None, "
        "mode: str | None = None, names: list[str] | None = None"
    )
    doc = tool["reference"]
    for text in (
        "Rename one glyph.",
        "`new_name` (str, required): New.",
        "one of `a`, `b`",
        "Destructive.",
        "Returns: `{status}`",
        "- Undo supported.",
        "fontpr.rename_glyph(glyph_name='a', new_name='b')",
    ):
        assert text in doc, text
    module = patches["fontpr"]["reference"]
    assert "keyword arguments only" in module and "list_tools()" in module
    assert "No transactions." in module and "SECRET" not in module


def test_mcp_signature_when_open_schema_then_kwargs_kept():
    assert mcp.signature({"inputSchema": {}}) == "**kwargs: Any"
    closed = {"inputSchema": {"properties": {}, "additionalProperties": False}}
    assert mcp.signature(closed) == ""


def test_llms_render_when_stubs_then_compact_summaries_and_signatures(tmp_path):
    from fontlab_echopy.tooling import llms

    (tmp_path / "fontlab.pyi").write_text(
        '"""Python interface.\n\nMore."""\n'
        'class flThing:\n    """flThing representation\n\nA **real** thing. Detail."""\n'
        'class flBare:\n    """flBare representation"""\n'
        "def Go(x: int, *args: Any) -> None: ...\n"
        "def Any_(*args: Any, **kwargs: Any) -> Any: ...\n"
    )
    text = llms.render(tmp_path)
    assert text.startswith("# FontLab Python API")
    assert "## fontlab\n\nPython interface.\n" in text
    assert "- flThing: A real thing\n" in text and "- flBare\n" in text
    assert "- Go(x: int, *args: Any)\n" in text and "- Any_(...)\n" in text
    assert "## fontgate" not in text, "missing modules are skipped"


def test_shipped_llms_when_generated_then_small_and_current():
    from fontlab_echopy.tooling import llms

    shipped = (ROOT / "src_docs/md/llms.txt").read_text()
    assert len(shipped.encode()) < 60_000
    assert shipped == llms.render(ROOT / "src/fontlab_echopy"), (
        "rerun `fontlab-echopy llms`"
    )
    assert "## PythonQt" not in shipped and "fontlabpr" not in shipped
