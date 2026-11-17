# this_file: src/fontlab_echopy/tooling/generate.py
"""Emit deterministic, source-readable facades from native captures."""
from __future__ import annotations

import ast
from collections.abc import Iterator
import json
import keyword
import re
from pathlib import Path
from typing import Any

from .signatures import annotation, signature


def valid(name: str) -> bool:
    return name.isidentifier() and not keyword.iskeyword(name) and not name.startswith("__")


def source_name(name: str) -> str:
    """Expose C++ nested/template names as readable source identifiers."""
    candidate = re.sub(r"\W", "_", name)
    if keyword.iskeyword(candidate):
        return candidate + "_"
    return candidate if valid(candidate) else "native_" + candidate


def _source_names(owner: str, names: list[str]) -> dict[str, str]:
    """Map native to source names; two natives sharing one source name is a bug."""
    mapping, seen = {}, {}
    for name in names:
        source = source_name(name)
        if source in seen and seen[source] != name:
            raise ValueError(
                f"Source name collision in {owner}: {seen[source]!r} and {name!r} -> {source!r}"
            )
        seen[source] = name
        mapping[name] = source
    return mapping


def _validate_scope_names(owner: str, scope: dict[str, Any]) -> None:
    """Check both the captured inventory and declarations before output changes."""
    keys = ("classes", "functions", "attributes", "constants", "modules")
    names = set(scope.get("names", []))
    names.update(item["name"] for key in keys for item in scope.get(key, []))
    mapping = _source_names(owner, sorted(names))
    reserved = {"Any", "globals", "_bind", "_unavailable",
                "_echopy_native", "_echopy_name", "_echopy_aliases", "_echopy_unavailable"}
    for original, source in mapping.items():
        if source in reserved:
            raise ValueError(
                f"Reserved source name in {owner}: {original!r} -> {source!r}"
            )
    for cls in scope.get("classes", []):
        members = set(cls.get("names", []))
        members.update(
            item["name"]
            for key in ("methods", "attributes", "constants")
            for item in cls.get(key, [])
            if not item["name"].startswith("__")
        )
        _source_names(owner + "." + source_name(cls["name"]), sorted(members))


def scopes(data: dict[str, Any]) -> Iterator[tuple[str, dict[str, Any], bool, bool]]:
    """Normalize fresh captures and legacy introspector JSON without rewriting it."""
    for name, module in sorted(data["modules"].items()):
        yield name, module.get("namespace", {}), bool(module.get("subpackages")), module.get("available", True)
        for child, entry in sorted(module.get("subpackages", {}).items()):
            yield name + "." + child, entry.get("namespace", entry), False, True


def function(
    info: dict[str, Any], module: str, method: bool = False, builtins_name: str = ""
) -> str:
    name = info["name"]
    text = info.get("signature", "")
    doc = info.get("doc", "")
    if text in {"", "(...)"}:
        candidates = [line.strip() for line in doc.splitlines() if name + "(" in line]
        text = candidates[0] if len(candidates) == 1 else "(...)"
    binding = info.get("binding") if method else None
    decorated = binding in {"staticmethod", "classmethod"}
    args, result = signature(text, name, method and not decorated and binding != "instancemethod")
    if name == "__init__":
        result = "None"
    doc = doc or f"Native {module}.{name}; argument details are not documented."
    indent = "    " if method else ""
    identifier = name if name == "__init__" else source_name(name)
    if identifier != name:
        doc += f"\n\nNative spelling: {name}; access it through getattr on the native object."
    qualifier = builtins_name + "." if builtins_name else ""
    decorator = f"{indent}@{qualifier}{binding}\n" if decorated else ""
    return decorator + f"{indent}def {identifier}({args}) -> {result}:\n{indent}    {doc!r}\n{indent}    _unavailable({(module + '.' + name)!r})\n\n"


def module_source(name: str, scope: dict[str, Any], available: bool) -> str:
    doc = scope.get("doc") or f"Native API for {name}."
    if not available:
        doc += " This optional module was absent from the captured host. Runtime delegation supports future hosts."
    occupied = set()
    for owner in (scope, *scope.get("classes", [])):
        occupied.update(source_name(item) for item in owner.get("names", []))
        occupied.update(
            source_name(item["name"])
            for key in ("classes", "functions", "attributes", "constants", "modules", "methods", "constructors")
            for item in owner.get(key, [])
            if "name" in item
        )
    builtins_name = "_echopy_builtins"
    while builtins_name in occupied:
        builtins_name += "_"
    source = f"# Generated from native API metadata; edit enrichment inputs, then merge.\n{doc!r}\nfrom __future__ import annotations\nfrom typing import Any\nimport builtins as {builtins_name}\nfrom fontlab_echopy._runtime import bind as _bind, unavailable as _unavailable\n\n"
    names = set()
    aliases = {}
    for cls in sorted(scope.get("classes", []), key=lambda c: c["name"]):
        identifier = source_name(cls["name"])
        if identifier != cls["name"]:
            aliases[cls["name"]] = identifier
        names.add(cls["name"])
        doc = cls.get('doc') or 'Native ' + name + '.' + cls['name']
        if cls.get('bases'):
            doc += "\n\nNative bases: " + ", ".join(cls['bases'])
        if cls.get('mro'):
            doc += "\n\nCaptured native MRO: " + ", ".join(cls['mro'])
        if cls.get('allocation_constructor'):
            allocation = cls['allocation_constructor']
            doc += "\n\nNative __new__ allocation evidence (not an __init__ overload):\n" + allocation.get('signature', '(...)') + "\n" + allocation.get('doc', '')
        source += f"class {identifier}:\n    {doc!r}\n"
        constructors = cls.get("constructors", [])
        if constructors:
            info = dict(constructors[0]) if len(constructors) == 1 else {
                "signature": "(self, *args, **kwargs)",
                "doc": "Native constructor overloads (no single signature selected):\n\n"
                + "\n\n".join(
                    item.get("signature", "(...)") + "\n" + item.get("doc", "")
                    for item in constructors
                ),
            }
            info["name"] = "__init__"
            source += function(info, name + "." + cls["name"], True, builtins_name)
        else:
            source += "    def __init__(self, *args: Any, **kwargs: Any) -> None:\n        'Native constructor; consult class documentation for supported overloads.'\n        _unavailable(" + repr(name + "." + cls["name"]) + ")\n\n"
        for info in sorted(cls.get("methods", []), key=lambda m: m["name"]):
            if not info["name"].startswith("__"):
                source += function(info, name + "." + cls["name"], True, builtins_name)
        for attr in sorted(cls.get("attributes", []) + cls.get("constants", []), key=lambda a: a["name"]):
            if not attr["name"].startswith("__"):
                source += f"    {source_name(attr['name'])}: {annotation(attr.get('type', ''))}\n"
                if attr.get("doc"):
                    source += f"    {attr['doc']!r}\n"
        source += "\n"
    for info in sorted(scope.get("functions", []), key=lambda f: f["name"]):
        if not info["name"].startswith("__") and info["name"] not in names:
            names.add(info["name"])
            if source_name(info["name"]) != info["name"]:
                aliases[info["name"]] = source_name(info["name"])
            source += function(info, name)
    for info in scope.get("attributes", []) + scope.get("constants", []) + scope.get("modules", []):
        if not info["name"].startswith("__") and info["name"] not in names:
            names.add(info["name"])
            if source_name(info["name"]) != info["name"]:
                aliases[info["name"]] = source_name(info["name"])
            kind = info.get("type", "")  # An instance of a class this module declares (FL.fl).
            kind = source_name(kind) if kind in {c["name"] for c in scope.get("classes", [])} else annotation(kind)
            source += f"{source_name(info['name'])}: {kind}\n"
            if info.get("doc"):
                source += f"{info['doc']!r}\n"
    source += f"\n__echopy_source_aliases__ = {aliases!r}\n"
    exported = sorted(set(scope["exports"]) & names) if "exports" in scope else sorted(names)  # `from FL import *`
    source += f"__all__ = {exported!r}\n_bind(globals(), {name!r}, __echopy_source_aliases__)\n"
    ast.parse(source)
    return source


def generate(
    data: dict[str, Any],
    output: Path,
    capture_identity: dict[str, str] | None = None,
    keep: tuple[str, ...] = (),
) -> dict[str, Any]:
    """Write source plus a name-coverage manifest; never modify overlay files.

    ``capture_identity`` (the capture's SHA-256) travels with the raw output so
    merge can record which capture the merged package documents. ``keep`` names
    top-level modules whose existing raw files stay untouched (retained scopes).
    """
    for name, scope, _package, _available in scopes(data):
        _validate_scope_names(name, scope)
    output = Path(output)
    report: dict[str, Any] = {"modules": {}, "unavailable": []}
    if capture_identity is not None:
        report["capture_identity"] = capture_identity
    written = set()
    for top in keep:
        written.update(output.joinpath(top).rglob("*.py"))
        written.add(output / (top + ".py"))
    for name, scope, package, available in scopes(data):
        relative = Path(*name.split(".")) / "__init__.py" if package else Path(*name.split(".")).with_suffix(".py")
        path = output / relative
        written.add(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        source = "# this_file: generated/" + relative.as_posix() + "\n" + module_source(name, scope, available)
        path.write_text(source, encoding="utf-8")
        declared = set()
        for node in ast.parse(source).body:
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                declared.add(node.name)
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                declared.add(node.target.id)
        expected = set(scope.get("names", [])) or {item["name"] for key in ("classes", "functions", "attributes", "constants", "modules") for item in scope.get(key, [])}
        classes = scope.get("classes", [])
        declared_classes = {node.name: node for node in ast.parse(source).body if isinstance(node, ast.ClassDef)}
        missing_members = {}
        for cls in classes:
            node = declared_classes[source_name(cls["name"])]
            members = {member.name for member in node.body if isinstance(member, ast.FunctionDef)} | {member.target.id for member in node.body if isinstance(member, ast.AnnAssign)}
            missing = [member for member in cls.get("names", []) if source_name(member) not in members]
            if missing:
                missing_members[cls["name"]] = missing
        report["modules"][name] = {"native_names": len(expected), "declared_names": len(declared), "source_aliases": {n: source_name(n) for n in expected if not valid(n)}, "missing_names": sorted(n for n in expected if source_name(n) not in declared), "inspection_errors": scope.get("errors", []), "classes": len(classes), "class_members": sum(len(c.get("names", [])) for c in classes), "missing_class_members": missing_members, "class_inspection_errors": {c["name"]: c["errors"] for c in classes if c.get("errors")}}
        uncaptured = sorted(set(scope.get("exports", ())) - set(scope.get("names", ())) - expected)
        if uncaptured:  # `__all__` entries the capture never saw; the shim cannot export them.
            report["modules"][name]["exports_not_captured"] = uncaptured
        if not available:
            report["unavailable"].append(name)
    remove_stale(output, written)
    (output / "coverage.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report


def remove_stale(output: Path, written: set[Path]) -> None:
    """Remove only previously generated modules, never handwritten support code."""
    for path in list(output.rglob("*.py")) + list(output.rglob("*.pyi")):
        if path not in written and any(line.startswith("# Generated from") for line in path.read_text().splitlines()[:2]):
            path.unlink()
