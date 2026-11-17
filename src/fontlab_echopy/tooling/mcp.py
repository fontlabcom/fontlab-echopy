# this_file: src/fontlab_echopy/tooling/mcp.py
"""Build a ``fontpr`` merge overlay from the FontLab MCP specification.

``fontpr`` is the embedded-Python face of FontLab's MCP server: every MCP tool
is a module function that takes keyword arguments only. The specification
(``fontlab-mcp.json``) gives each tool's description, input schema, effect,
result shape, notes and examples. This module turns those into ``reference``
docstrings and keyword-only ``signature`` patches for tools that the captured
``generated/fontpr.py`` actually defines. Tools that exist on only one side are
reported, never invented.
"""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path
from typing import Any

REFERENCE_SOURCE = "FontLab MCP specification"
JSON_TYPES = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "object": "dict[str, Any]",
}
# The fontpr module refuses these tools (fontpr_module.cpp, blocked list).
BLOCKED = ("run_python", "get_python_output")
MODULE_DOC = """FontLab MCP tools for embedded Python.

`fontpr` exposes the tools of FontLab's MCP server as ordinary functions inside
FontLab's own Python. A script can call the same focused, validated operations
that an external MCP client uses, without a network connection or a token.

Calling convention:

- Every tool function takes keyword arguments only. Positional arguments are
  ignored, so `fontpr.list_glyphs(font_id=1)` works and
  `fontpr.list_glyphs(1)` does not pass `font_id`.
- `fontpr.call(name, **kwargs)` calls a tool by its MCP name; `name` must be a
  string (otherwise `TypeError`), for example
  `fontpr.call("list_glyphs", font_id=1)`.
- `fontpr.available()` returns True once the MCP tools are ready. Before then
  every call raises `fontpr.Error("MCP tools are not available yet.")`.
- `fontpr.list_tools()` returns a list of tool metadata dicts (`name`,
  `description`, `inputSchema` and the other MCP fields) for the running
  build. Blocked tools are left out, and the list is empty when tools are
  unavailable. Treat it as authoritative: the functions documented here come
  from one build and one specification.
- `run_python` and `get_python_output` are blocked: calling them through
  `fontpr` raises `fontpr.Error`, because a script is already running Python.

Results:

- A tool error (`isError`) raises `fontpr.Error` with the tool's message.
- Otherwise the first text result is parsed as JSON and returned as a `dict` or
  `list`; text that is not JSON is returned as `str`.
- Inspect payload fields such as `success`, `status`, `changed`, `applied` and
  `persisted`. A returned value does not by itself mean that the font changed.
"""


def schema_type(schema: dict[str, Any]) -> str:
    """Python annotation for a JSON-schema property."""
    kind = schema.get("type")
    if isinstance(kind, list):
        names = [JSON_TYPES.get(k, "Any") for k in kind if k != "null"]
        return " | ".join(dict.fromkeys(names)) or "Any"
    if kind == "array":
        items = schema.get("items")
        inner = schema_type(items) if isinstance(items, dict) else "Any"
        return f"list[{inner}]"
    return JSON_TYPES.get(kind, "Any")


INTEGER_NAMES = re.compile(r"(limit|offset|max_chars|.*_(id|count|index))")


def param_type(name: str, schema: dict[str, Any]) -> str:
    """Identifiers, counts, indices and page sizes (``font_id``, ``limit``,
    ``min_contour_count``) are integers even where the schema says number."""
    kind = schema_type(schema)
    return "int" if kind == "float" and INTEGER_NAMES.fullmatch(name) else kind


def signature(tool: dict[str, Any]) -> str:
    """Keyword-only parameter list; required parameters come first."""
    schema = tool.get("inputSchema", {})
    props: dict[str, Any] = schema.get("properties", {})
    required = [n for n in schema.get("required", []) if n in props]
    named = [f"{name}: {param_type(name, props[name])}" for name in required]
    named += [
        f"{name}: {param_type(name, spec)} | None = None"
        for name, spec in props.items()
        if name not in required
    ]
    rest = (
        ["**kwargs: Any"]
        if schema.get("additionalProperties", True) is not False
        else []
    )
    return ", ".join(["*", *named, *rest] if named else rest)


def parameter_lines(tool: dict[str, Any]) -> list[str]:
    schema = tool.get("inputSchema", {})
    required = set(schema.get("required", []))
    lines = []
    for name, spec in schema.get("properties", {}).items():
        flags = ["required" if name in required else "optional"]
        if "enum" in spec:
            flags.append("one of " + ", ".join(f"`{v}`" for v in spec["enum"]))
        desc = " ".join(str(spec.get("description", "")).split())
        lines.append(
            f"- `{name}` ({schema_type(spec)}, {'; '.join(flags)}): {desc}".rstrip(": ")
        )
    return lines


def example(tool: dict[str, Any]) -> str:
    """First specification example rendered as a fontpr call."""
    for item in tool.get("examples", []):
        args = ", ".join(f"{k}={v!r}" for k, v in item.get("arguments", {}).items())
        purpose = item.get("purpose", "")
        comment = f"# {purpose}\n" if purpose else ""
        return f"```python\n{comment}result = fontpr.{tool['name']}({args})\n```"
    return ""


def tool_doc(tool: dict[str, Any]) -> str:
    parts = [" ".join(tool.get("description", "").split())]
    params = parameter_lines(tool)
    parts.append(
        "Parameters:\n\n" + "\n".join(params) if params else "Parameters: none."
    )
    effect = tool.get("effect")
    if effect:
        parts.append(
            f"Effect: {effect}." + (" Destructive." if tool.get("destructive") else "")
        )
    if tool.get("result"):
        parts.append(f"Returns: `{tool['result']}`")
    notes = [" ".join(n.split()) for n in tool.get("notes", [])]
    if notes:
        parts.append("Notes:\n\n" + "\n".join(f"- {n}" for n in notes))
    parts.append(example(tool))
    return "\n\n".join(p for p in parts if p)


def module_doc(spec: dict[str, Any]) -> str:
    """Module docstring: fixed calling convention plus targeting and rules."""
    parts = [MODULE_DOC.strip()]
    targeting = spec.get("targeting") or {}
    if targeting:
        parts.append(
            "Targeting:\n\n"
            + "\n".join(
                f"- `{k}`: {' '.join(str(v).split())}" for k, v in targeting.items()
            )
        )
    rules = spec.get("agent_rules") or []
    if rules:
        parts.append("Working rules:\n\n" + "\n".join(f"- {r}" for r in rules))
    limits = spec.get("known_limitations") or []
    if limits:
        parts.append(
            "Known limitations:\n\n"
            + "\n".join(f"- {item.get('id')}: {item.get('detail')}" for item in limits)
        )
    return "\n\n".join(parts)


HELPER_PATCHES: dict[str, dict[str, str]] = {
    "call": {
        "reference": "Call an MCP tool by its name with keyword arguments.\n\n"
        "`name` must be a str, otherwise `TypeError` is raised. Example: "
        '`fontpr.call("list_glyphs", font_id=1)`.',
        "reference_source": REFERENCE_SOURCE,
        "signature": "name: str, /, **kwargs: Any",
    },
    "list_tools": {
        "reference": "Return the MCP tool metadata dicts of the running build.\n\n"
        "Each dict carries `name`, `description` and `inputSchema`. Blocked tools "
        "(`run_python`, `get_python_output`) are left out; the list is empty "
        "while the MCP tools are unavailable.",
        "reference_source": REFERENCE_SOURCE,
        "signature": "",
    },
}


def captured_functions(generated: Path) -> set[str]:
    tree = ast.parse((generated / "fontpr.py").read_text())
    return {n.name for n in tree.body if isinstance(n, ast.FunctionDef)}


def build(
    spec: dict[str, Any], captured: set[str]
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Return ``(patches, report)`` for tools defined in both sources."""
    tools = {tool["name"]: tool for tool in spec.get("tools", [])}
    patches: dict[str, Any] = {
        "fontpr": {"reference": module_doc(spec), "reference_source": REFERENCE_SOURCE}
    }
    for name in sorted(set(tools) & captured):
        patches[f"fontpr.{name}"] = {
            "reference": tool_doc(tools[name]),
            "reference_source": REFERENCE_SOURCE,
            "signature": signature(tools[name]),
        }
    for key, value in HELPER_PATCHES.items():
        if key in captured:  # only patch helpers the capture defines
            patches[f"fontpr.{key}"] = value
    helpers = {"available", "call", "list_tools"}
    report = {
        "spec_tools": len(tools),
        "documented": len(set(tools) & captured),
        "spec_only": sorted(set(tools) - captured),
        "capture_only": sorted(captured - set(tools) - helpers),
        "blocked_in_spec": [name for name in BLOCKED if name in tools],
    }
    return patches, report


def write(mcp_json: Path, generated: Path, output: Path) -> dict[str, Any]:
    patches, report = build(
        json.loads(mcp_json.read_text()), captured_functions(generated)
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(patches, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    )
    return report
