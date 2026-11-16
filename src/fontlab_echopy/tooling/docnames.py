# this_file: src/fontlab_echopy/tooling/docnames.py
"""Expose enriched source to documentation tools under actual native names.

The output consists of explicit source aliases, not copied declarations or
runtime replacements. Point a source-only documentation loader at this output
and the installed/source Echopy package with runtime inspection disabled.
"""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
from typing import Any

MARKER = "# Generated documentation namespace from enriched Echopy."
SHIM_MARKER = "_shim.json"


def _declared_names(tree: ast.Module) -> list[str]:
    """Retain explicit declarations, sanitized C++ names and listed re-exports."""
    names = set()
    exports = next(
        (
            set(ast.literal_eval(node.value))
            for node in tree.body
            if isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and getattr(node.targets[0], "id", None) == "__all__"
        ),
        set(),
    )
    for node in tree.body:
        if isinstance(node, ast.ImportFrom):
            # Shims re-export documented classes; only names in __all__ count.
            names.update(
                alias.asname or alias.name
                for alias in node.names
                if (alias.asname or alias.name) in exports
            )
        if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            names.add(node.name)
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            names.add(node.target.id)
        elif (
            isinstance(node, ast.Assign)
            and len(node.targets) == 1
            and isinstance(node.targets[0], ast.Name)
            and not node.targets[0].id.startswith("__")
        ):
            names.add(node.targets[0].id)  # Type aliases such as `Path = Literal[...]`.
    return sorted(names)


def _alias_source(
    module: str, names: list[str], relative: Path, source_doc: str | None
) -> str:
    """Write ordinary readable Python imports that Griffe resolves statically."""
    doc = (
        (source_doc or module + " native API reference.")
        + "\n\nDocumentation is derived from captured and enriched Echopy source.\nNative objects are supplied by FontLab."
    )
    doc_source = ast.unparse(
        ast.Module(body=[ast.Expr(value=ast.Constant(value=doc))], type_ignores=[])
    )
    lines = [f"# this_file: {relative.as_posix()}", MARKER, doc_source]
    if names:
        lines += ["", f"from fontlab_echopy.{module} import ("]
        lines += [f"    {name} as {name}," for name in names]
        lines += [")"]
    lines += ["", "__all__ = ["]
    lines += [f"    {name!r}," for name in names]
    lines += ["]", ""]
    source = "\n".join(lines)
    ast.parse(source)
    return source


def export_docnames(output: Path, *, source: Path | None = None) -> dict[str, Any]:
    """Generate deterministic documentation namespaces from merged sidecars.

    Never capture/import native modules, copy class bodies or edit merged source.
    Generated namespaces belong on a documentation loader path only.
    """
    source = (source or Path(__file__).resolve().parents[1]).resolve()
    output = Path(output).expanduser().resolve()
    if output.is_relative_to(source) or source.is_relative_to(output):
        raise ValueError("Documentation output must be outside the source tree.")
    modules, outputs = {}, {}
    for path in sorted(source.rglob("*.pyi")):
        relative = path.relative_to(source)
        module = ".".join(relative.with_suffix("").parts).removesuffix(".__init__")
        # Kept after issue 201: fontlab-python-docs still globs */_shim.json for shim packages
        # (marked packages from other producers); Echopy itself ships none.
        shim = (source / relative.parts[0] / SHIM_MARKER).is_file()
        if (
            module not in {"fontlab", "fontgate", "fontpr", "fontlabpr", "FL", "PythonQt"}
            and not module.startswith("PythonQt.")
            and not shim
        ):
            continue
        data = path.read_bytes()
        tree = ast.parse(data)
        names = _declared_names(tree)
        target = relative.with_suffix(".py")
        class_facet = False
        if not names and path.name != "__init__.pyi":
            parent_source = path.parent / "__init__.pyi"
            if parent_source.exists():
                parent_tree = ast.parse(parent_source.read_bytes())
                class_facet = any(
                    isinstance(node, ast.ClassDef) and node.name == path.stem
                    for node in parent_tree.body
                )
        content = _alias_source(
            module, names, target, ast.get_docstring(tree, clean=False)
        )
        if not class_facet:
            outputs[target] = content
        modules[module] = {
            "source": "fontlab_echopy/" + relative.as_posix(),
            "source_sha256": hashlib.sha256(data).hexdigest(),
            "output": None if class_facet else target.as_posix(),
            "output_sha256": None
            if class_facet
            else hashlib.sha256(content.encode()).hexdigest(),
            "declared_names": names,
            "class_facet": class_facet,
        }
    if not modules:
        raise ValueError("No native API sidecars found in the source tree.")
    # Check ownership before touching any output, including a previous manifest.
    for relative in outputs:
        existing = output / relative
        if existing.exists() and MARKER not in existing.read_text().splitlines()[:3]:
            raise ValueError(
                f"Refusing to overwrite unrelated documentation source: {relative}"
            )
    manifest = output / "docnames-manifest.json"
    if (
        manifest.exists()
        and json.loads(manifest.read_text()).get("producer")
        != "fontlab_echopy.tooling.docnames"
    ):
        raise ValueError("Refusing to overwrite an unrelated documentation manifest.")
    output.mkdir(parents=True, exist_ok=True)
    for relative, content in outputs.items():
        path = output / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    stale = []
    for path in output.rglob("*.py"):
        if (
            path.relative_to(output) not in outputs
            and MARKER in path.read_text().splitlines()[:3]
        ):
            stale.append(path)
    for path in stale:
        path.unlink()
    report = {
        "schema_version": 1,
        "producer": "fontlab_echopy.tooling.docnames",
        "scope": "source-only documentation namespaces; no native inspection",
        "modules": modules,
    }
    manifest.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return report
