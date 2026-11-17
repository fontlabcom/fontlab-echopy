# this_file: src/fontlab_echopy/tooling/proteus.py
"""Build a merge overlay from the FontLab Proteus API documentation.

The Proteus checkout ships Markdown articles (``api-docs``) written for the
``fontlab`` module. This module turns them into ``reference`` patches keyed by
the dotted names that :mod:`fontlab_echopy.tooling.merge` targets. Only names
present in the captured ``generated`` modules are emitted; the rest are
reported. Source paths, C++ names and binding-file notes are stripped, so no
machine path or implementation detail reaches a published docstring.
"""

from __future__ import annotations

import ast
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REFERENCE_SOURCE = "FontLab Proteus API documentation"
MEMBER_SECTIONS = {
    "constructors",
    "constructor",
    "methods",
    "static methods",
    "properties",
}
SKIPPED_SECTIONS = MEMBER_SECTIONS | {"additional constructor annotations", "see also"}
NAME_HEADERS = {"method", "name", "property", "field", "signature"}
DESCRIPTION_HEADERS = {"description", "meaning", "contract"}
PLACEHOLDER_DESCRIPTIONS = {"native enum value.", ""}
# Lines that describe the C++ implementation rather than the Python API.
DROPPED_LINE = re.compile(
    r"^\s*(\*\*(Python names?|Runtime type names|C\+\+|Sources?|Implementation):\*\*"
    r"|\*\(Implemented as .*\)\*\s*$|Source: `)"
)
UNSAFE = ("/Users/", ".cpp", "pygate/", ".h`", "pyfl")
LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)
H1 = re.compile(r"^#\s+(.*)$")


@dataclass
class Overlay:
    """Patches plus a report of what could not be placed."""

    patches: dict[str, dict[str, Any]] = field(default_factory=dict)
    unplaced: list[str] = field(default_factory=list)
    duplicates: list[str] = field(default_factory=list)
    dropped_lines: int = 0

    def add(self, key: str, text: str, targets: set[str]) -> None:
        text = text.strip()
        if not text:
            return
        if key not in targets:
            self.unplaced.append(key)
            return
        if key in self.patches:
            if text in self.patches[key]["reference"]:
                return
            self.duplicates.append(key)
            text = self.patches[key]["reference"] + "\n\n" + text
        self.patches[key] = {"reference": text, "reference_source": REFERENCE_SOURCE}


def target_keys(generated: Path) -> dict[str, set[str]]:
    """Index captured names: ``"keys"`` holds every dotted key merge targets;
    every other entry maps a top-level name to the modules that define it."""
    owners: dict[str, set[str]] = {}
    keys: set[str] = set()
    for path in sorted(generated.glob("*.py")):
        module = path.stem
        keys.add(module)
        for node in ast.parse(path.read_text()).body:
            name = _node_name(node)
            if name is None:
                continue
            owners.setdefault(name, set()).add(module)
            keys.add(f"{module}.{name}")
            if isinstance(node, ast.ClassDef):
                for child in node.body:
                    child_name = _node_name(child)
                    if child_name and not isinstance(child, ast.ClassDef):
                        keys.add(f"{module}.{name}.{child_name}")
    return {"keys": keys, **owners}


def _node_name(node: ast.AST) -> str | None:
    if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
        return node.name
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return node.target.id
    return None


def split_sections(text: str) -> list[tuple[str, list[str]]]:
    """Split Markdown at ``##`` headings, ignoring ``#`` lines inside fences."""
    sections: list[tuple[str, list[str]]] = [("", [])]
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith("## "):
            sections.append((line[3:].strip(), []))
            continue
        sections[-1][1].append(line)
    return sections


def clean(lines: list[str], overlay: Overlay) -> str:
    """Drop implementation notes, links, rules and unsafe lines; tidy blanks."""
    text = COMMENT.sub("", "\n".join(lines))
    kept: list[str] = []
    for line in text.splitlines():
        if DROPPED_LINE.match(line) or line.strip() == "---":
            continue
        if any(token in line for token in UNSAFE):
            overlay.dropped_lines += 1
            continue
        kept.append(LINK.sub(r"\1", line.rstrip()))
    return re.sub(r"\n{3,}", "\n\n", "\n".join(kept)).strip()


def table_rows(lines: list[str]) -> list[dict[str, str]]:
    """Parse every pipe table in ``lines`` into header-keyed rows."""
    rows: list[dict[str, str]] = []
    header: list[str] | None = None
    for line in lines:
        if not line.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
        if header is None:
            header = [c.lower() for c in cells]
        elif not all(set(c) <= set("-: ") for c in cells):
            rows.append(dict(zip(header, cells)))
    return rows


def split_member_tables(lines: list[str]) -> tuple[list[str], list[str]]:
    """Separate pipe tables whose header names members from the other lines."""
    prose: list[str] = []
    tables: list[str] = []
    member_table = False
    for i, line in enumerate(lines):
        if not line.startswith("|"):
            member_table = False
            prose.append(line)
            continue
        if i == 0 or not lines[i - 1].startswith("|"):
            header = {c.strip().lower() for c in line.strip().strip("|").split("|")}
            member_table = bool(header & NAME_HEADERS)
            if member_table and tables:
                tables.append("")  # keep table_rows from joining two tables
        (tables if member_table else prose).append(line)
    return prose, tables


def member_name(cell: str) -> str | None:
    """``bool hasActive()`` -> ``hasActive``; ``\\`name\\``` -> ``name``."""
    text = cell.replace("`", "").split("(", 1)[0]
    names = re.findall(r"[A-Za-z_]\w*", text)
    return names[-1] if names else None


def class_names(text: str, stem: str, owners: dict[str, set[str]]) -> list[str]:
    """Python names declared by an article, falling back to its file stem."""
    names: list[str] = []
    for line in text.splitlines():
        if line.startswith("**Python name"):
            names += re.findall(r"`([A-Za-z_]\w*)`", line)
        if line.startswith("**Runtime type names:**"):
            names += [f"{a}_{b}_" for a, b in re.findall(r"`(\w+)<(\w+)>`", line)]
    if not names and stem in owners:
        names = [stem]
    return list(dict.fromkeys(names))


def lead_with_prose(doc: str) -> str:
    """Start with the first prose sentence, not "Inherits from" or a heading.

    Tools and tooltips show only the first line, so the inheritance note moves
    after the first prose paragraph and the remaining text keeps its order.
    """
    paragraphs = doc.split("\n\n")
    if not paragraphs[0].startswith("Inherits from"):
        return doc
    prose = next(
        (
            i
            for i, p in enumerate(paragraphs)
            if i and not p.startswith(("#", "|", "-", "```"))
        ),
        None,
    )
    if prose is None:
        return doc
    inherits = paragraphs.pop(0)
    first = paragraphs.pop(prose - 1)
    return "\n\n".join([first, inherits, *paragraphs])


def class_overlay(path: Path, index: dict[str, set[str]], overlay: Overlay) -> None:
    text = path.read_text()
    targets = index["keys"]
    sections = split_sections(text)
    preamble = sections[0][1]
    at = next((i for i, line in enumerate(preamble) if H1.match(line)), None)
    title = H1.match(preamble[at]) if at is not None else None
    body, preamble_tables = split_member_tables(
        [ln for i, ln in enumerate(preamble) if i != at]
    )
    heading = title.group(1) if title else ""
    lead = heading.split(" — ", 1)[1].strip() if " — " in heading else ""
    parts = [lead.rstrip(".") + "." if lead else "", clean(body, overlay)]
    members: dict[str, list[str]] = {}
    member_blocks = [("methods", preamble_tables), *sections[1:]]
    for heading, lines in member_blocks:
        if heading.lower() in MEMBER_SECTIONS:
            for row in table_rows(lines):
                name_cell = next((row[h] for h in row if h in NAME_HEADERS), "")
                desc = next((row[h] for h in row if h in DESCRIPTION_HEADERS), "")
                name = member_name(name_cell)
                desc = clean([desc], overlay)
                if name and desc:
                    members.setdefault(name, []).append(desc)
        elif heading.lower() not in SKIPPED_SECTIONS:
            parts.append(f"## {heading}\n\n" + clean(lines, overlay))
    doc = lead_with_prose("\n\n".join(p for p in parts if p.strip()))
    names = class_names(text, path.stem, index)
    if not names:
        overlay.unplaced.append(f"article:{path.name}")
    for name in names:
        for module in sorted(index.get(name, {"fontlab"})):
            overlay.add(f"{module}.{name}", doc, targets)
            for member, descs in members.items():
                text = "\n\n".join(dict.fromkeys(descs))
                overlay.add(f"{module}.{name}.{member}", text, targets)


def function_overlay(path: Path, targets: set[str], overlay: Overlay) -> None:
    """``### Name(args)`` entries of the module reference become functions."""
    entry: str | None = None
    lines: list[str] = []
    fenced = False

    def flush() -> None:
        if entry:
            overlay.add(f"fontlab.{entry}", clean(lines, overlay), targets)

    for line in path.read_text().splitlines():
        if line.lstrip().startswith("```"):
            fenced = not fenced
        if not fenced and line.startswith("#"):
            flush()
            match = re.match(r"^###\s+([A-Za-z_]\w*)", line)
            entry, lines = (match.group(1) if match else None), []
            continue
        lines.append(line)
    flush()


def enum_overlay(path: Path, targets: set[str], overlay: Overlay) -> None:
    """Module-level enum dictionaries from the enums article."""
    for heading, lines in split_sections(path.read_text())[1:]:
        name = heading.split()[0] if heading else ""
        if not name or heading.lower().startswith("class enum"):
            continue
        intro = clean([line for line in lines if not line.startswith("|")], overlay)
        keys = []
        for row in table_rows(lines):
            key = row.get("key", "").strip("`")
            desc = row.get("description", "")
            if key:
                tail = "" if desc.lower() in PLACEHOLDER_DESCRIPTIONS else f": {desc}"
                keys.append(f"- `{key}`{tail}")
        text = "\n\n".join(
            p for p in (intro, "Keys:\n\n" + "\n".join(keys) if keys else "") if p
        )
        overlay.add(f"fontlab.{name}", text, targets)


def module_overlay(path: Path, targets: set[str], overlay: Overlay) -> None:
    """Condensed module overview: architecture, types and calling conventions."""
    keep = {
        "architecture",
        "type conventions",
        "calling conventions and inherited members",
    }
    parts = [
        f"## {heading}\n\n" + clean(lines, overlay)
        for heading, lines in split_sections(path.read_text())[1:]
        if heading.lower() in keep
    ]
    overlay.add("fontlab", "\n\n".join(parts), targets)


def build(api_docs: Path, generated: Path) -> Overlay:
    """Return the Proteus overlay for the captured modules in ``generated``."""
    index = target_keys(generated)
    targets = index["keys"]
    overlay = Overlay()
    module_overlay(api_docs / "00-overview.md", targets, overlay)
    function_overlay(api_docs / "01-module-reference.md", targets, overlay)
    enum_overlay(api_docs / "02-enums-and-constants.md", targets, overlay)
    for path in sorted((api_docs / "classes").glob("*.md")):
        if path.name != "README.md":
            class_overlay(path, index, overlay)
    return overlay


def write(api_docs: Path, generated: Path, output: Path) -> dict[str, Any]:
    """Write the overlay JSON and return a small report."""
    overlay = build(api_docs, generated)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(overlay.patches, indent=1, sort_keys=True, ensure_ascii=False) + "\n"
    )
    return {
        "patches": len(overlay.patches),
        "unplaced": sorted(set(overlay.unplaced)),
        "duplicates": sorted(set(overlay.duplicates)),
        "dropped_lines": overlay.dropped_lines,
    }
