# this_file: src/fontlab_echopy/tooling/merge.py
"""Merge independently maintained JSON enrichment into generated Python source."""

from __future__ import annotations

import ast
import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .generate import remove_stale, source_name


def documented_outputs(tree: ast.Module, relative: Path) -> tuple[str, str]:
    """Emit a small native facade and a complete canonical documentation stub."""
    aliases = {}
    kept = []
    classes = {node.name for node in tree.body if isinstance(node, ast.ClassDef)}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if (
                isinstance(target, ast.Name)
                and target.id == "__echopy_source_aliases__"
            ):
                aliases.update(ast.literal_eval(node.value))
            # Compatibility with the exact class markers in historical raw output.
            elif (
                isinstance(target, ast.Subscript)
                and isinstance(target.value, ast.Call)
                and isinstance(target.value.func, ast.Name)
                and target.value.func.id == "globals"
                and not target.value.args
                and not target.value.keywords
                and isinstance(target.slice, ast.Constant)
                and isinstance(target.slice.value, str)
                and isinstance(node.value, ast.Name)
                and node.value.id in classes
                and source_name(target.slice.value) == node.value.id
                and target.slice.value != node.value.id
            ):
                aliases[target.slice.value] = node.value.id
        if (
            isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AnnAssign, ast.Import))
            or isinstance(node, ast.ImportFrom)
            and node.module in {"__future__", "typing"}
            or isinstance(node, ast.Assign)
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "__all__"
            or isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
        ):
            kept.append(node)
    tree.body = kept
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            doc = ast.get_docstring(node)
            node.body = ([ast.Expr(value=ast.Constant(value=doc))] if doc else []) + [
                ast.Expr(value=ast.Constant(value=Ellipsis))
            ]
    ast.fix_missing_locations(tree)
    module = ".".join(relative.with_suffix("").parts).removesuffix(".__init__")
    marker = "\n# Generated from native metadata and independent enrichment inputs.\n"
    stub = (
        "# this_file: src/fontlab_echopy/"
        + relative.with_suffix(".pyi").as_posix()
        + marker
        + ast.unparse(tree)
        + "\n"
    )
    facade = "# this_file: src/fontlab_echopy/" + relative.as_posix() + marker
    facade += (
        repr(
            "Native "
            + module
            + "; complete annotated documentation is in the adjacent .pyi source."
        )
        + "\n"
    )
    facade += "from fontlab_echopy._runtime import populate as _populate\n"
    facade += f"_populate(globals(), {module!r}, {aliases!r})\n"
    return facade, stub


PLACEHOLDER_LEADS = (
    re.compile(r"\S+ representation"),  # fontlab class stub: "flGlyph representation"
    re.compile(r"\S+<[^>]*> doc"),  # template stub: "flObjectsList<flGuideLine> doc"
    re.compile(r"Call an MCP tool by name\."),  # generic fontpr tool stub
)
STRUCTURAL_LEADS = ("Constructors:", "Native bases:")


def is_placeholder_lead(paragraph: str) -> bool:
    """True when a generated first paragraph carries no description of its own."""
    text = paragraph.strip()
    return (
        not text
        or text.startswith(STRUCTURAL_LEADS)
        or any(p.fullmatch(text) for p in PLACEHOLDER_LEADS)
    )


def with_reference(doc: str, reference: str) -> str:
    """Put upstream reference prose first, replacing a placeholder lead.

    A real lead (for example a captured C++ signature line) stays first and the
    reference follows it. Constructors and native bases keep their place after.
    """
    lead, sep, rest = doc.partition("\n\n")
    if lead.strip().startswith(STRUCTURAL_LEADS):
        lead, rest = "", doc
    first = reference.partition("\n\n")[0]
    if is_placeholder_lead(lead) or " ".join(lead.split()) == " ".join(first.split()):
        return reference + ("\n\n" + rest if rest else "")
    return lead + "\n\n" + reference + (sep + rest if rest else "")


def reference_source(patch: dict[str, Any]) -> str:
    return patch.get("reference_source", "upstream reference")


def enrich_node(node: ast.AST, patch: dict[str, Any]) -> None:
    """Apply docs/types only to explicit targets; preserve overload provenance."""
    if isinstance(node, ast.AnnAssign):
        if patch.get("reference"):
            node._echopy_reference = (
                patch["reference"] + "\n\nSource: " + reference_source(patch)
            )
        if patch.get("doc"):
            node._echopy_doc = (
                patch["doc"] + "\n\nSource: " + patch.get("source", "native metadata")
            )
        if patch.get("returns"):
            node.annotation = ast.parse(patch["returns"], mode="eval").body
    if hasattr(node, "body") and (
        "doc" in patch or patch.get("signatures") or patch.get("reference")
    ):
        doc = ast.get_docstring(node) or ""
        if patch.get("reference"):
            doc = with_reference(doc, patch["reference"])
        supplemental = patch.get("doc", "")
        if supplemental and supplemental != doc:
            doc += ("\n\nSupplemental documentation:\n" if doc else "") + supplemental
        if patch.get("signatures"):
            doc += (
                "\n\nUpstream PySide2 reference signatures (binding differences may apply):\n\n```python\n"
                + "\n".join(patch["signatures"])
                + "\n```"
            )
        if patch.get("reference"):
            doc += "\n\nSource: " + reference_source(patch)
        if patch.get("source"):
            doc += "\n\nSource: " + patch["source"]
        statement = ast.Expr(value=ast.Constant(value=doc))
        if ast.get_docstring(node) is not None:
            node.body[0] = statement
        else:
            node.body.insert(0, statement)
    if isinstance(node, ast.FunctionDef):
        if "signature" in patch:
            # Replace the captured parameter list, e.g. a dynamic (*args, **kwargs).
            template = ast.parse(f"def _({patch['signature']}): pass").body[0]
            node.args = template.args
        for arg in node.args.posonlyargs + node.args.args + node.args.kwonlyargs:
            if arg.arg in patch.get("parameter_types", {}):
                arg.annotation = ast.parse(
                    patch["parameter_types"][arg.arg], mode="eval"
                ).body
        if "returns" in patch:
            node.returns = ast.parse(patch["returns"], mode="eval").body
    if isinstance(node, ast.ClassDef):
        for source in patch.get("extensions", []):
            extension = ast.parse(source).body[0]
            if not isinstance(extension, ast.FunctionDef):
                raise ValueError("Extensions must be explicit function definitions")  # noqa: TRY004 -- invalid source content
            if any(getattr(n, "name", None) == extension.name for n in node.body):
                raise ValueError(
                    f"Extension collides with native member: {node.name}.{extension.name}"
                )
            node.body.append(extension)


def merge(raw: Path, output: Path, overlays: list[Path]) -> dict[str, Any]:
    """Merge overlays in order; raw inputs and overlays remain untouched."""
    raw, output = Path(raw), Path(output)
    if raw.resolve() == output.resolve():
        raise ValueError("Raw and merged output folders must differ")
    patches: dict[str, Any] = {}
    for path in overlays:
        for key, value in json.loads(Path(path).read_text()).items():
            patches.setdefault(key, {}).update(value)
    applied = set()
    written = set()
    extensions: list[tuple[str, ast.FunctionDef]] = []
    for path in sorted(raw.rglob("*.py")):
        relative = path.relative_to(raw)
        module = ".".join(relative.with_suffix("").parts).removesuffix(".__init__")
        tree = ast.parse(path.read_text())
        targets = {module: tree}
        for node in tree.body:
            if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                targets[module + "." + node.target.id] = node
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                targets[module + "." + node.name] = node
                if isinstance(node, ast.ClassDef):
                    targets.update(
                        {
                            module + "." + node.name + "." + child.name: child
                            for child in node.body
                            if isinstance(child, ast.FunctionDef)
                        }
                    )
                    targets.update(
                        {
                            module + "." + node.name + "." + child.target.id: child
                            for child in node.body
                            if isinstance(child, ast.AnnAssign)
                            and isinstance(child.target, ast.Name)
                        }
                    )
        for key in targets.keys() & patches.keys():
            enrich_node(targets[key], patches[key])
            applied.add(key)
            for source in patches[key].get("extensions", []):
                function = copy.deepcopy(ast.parse(source).body[0])
                extensions.append((key + "." + function.name, function))
        owners = [tree, *(node for node in tree.body if isinstance(node, ast.ClassDef))]
        for owner in owners:
            body = []
            for index, child in enumerate(owner.body):
                body.append(child)
                following = (
                    owner.body[index + 1] if index + 1 < len(owner.body) else None
                )
                if not (
                    isinstance(following, ast.Expr)
                    and isinstance(following.value, ast.Constant)
                    and isinstance(following.value.value, str)
                ):
                    following = None
                if hasattr(child, "_echopy_reference"):
                    if following is None:
                        following = ast.Expr(value=ast.Constant(value=""))
                        body.append(following)
                    following.value.value = with_reference(
                        following.value.value, child._echopy_reference
                    )
                if hasattr(child, "_echopy_doc"):
                    if following is not None:
                        following.value.value += (
                            "\n\nSupplemental documentation:\n" + child._echopy_doc
                        )
                    else:
                        body.append(
                            ast.Expr(value=ast.Constant(value=child._echopy_doc))
                        )
            owner.body = body
        ast.fix_missing_locations(tree)
        source, stub = documented_outputs(tree, relative)
        compile(source, relative.as_posix(), "exec")
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source)
        written.add(target)
        stub_path = target.with_suffix(".pyi")
        stub_path.write_text(stub)
        written.add(stub_path)
    runtime = [
        "# this_file: src/fontlab_echopy/_patch_extensions.py",
        "# Generated from maintained extension patches; regenerate with merge.",
        '"""Executable overlay helpers; installation is explicitly requested."""',
        "from __future__ import annotations",
        "from typing import Any",
    ]
    registry = []
    for index, (key, function) in enumerate(
        sorted(extensions, key=lambda entry: entry[0])
    ):
        function.name = f"_extension_{index}"
        runtime.append(ast.unparse(ast.fix_missing_locations(function)))
        registry.append(f"    {key!r}: {function.name},")
    runtime.extend(["EXTENSIONS = {", *registry, "}", ""])
    extension_path = output / "_patch_extensions.py"
    extension_path.parent.mkdir(parents=True, exist_ok=True)
    extension_source = "\n".join(runtime)
    compile(extension_source, str(extension_path), "exec")
    extension_path.write_text(extension_source)
    written.add(extension_path)
    remove_stale(output, written)
    result = {"applied": len(applied), "unmatched": sorted(patches.keys() - applied)}
    provenance_path = output / "_provenance.json"
    provenance = (
        json.loads(provenance_path.read_text()) if provenance_path.exists() else {}
    )
    coverage_path = raw / "coverage.json"
    native = json.loads(coverage_path.read_text()) if coverage_path.exists() else {}
    identity = native.pop("capture_identity", None)
    if coverage_path.exists():
        provenance["native_coverage"] = native
    # A raw tree without its own capture identity (the committed `generated/`)
    # re-merges the capture already recorded, so keep that identity. Identities
    # embed `merge.unmatched` and the extension registry, so they survive only
    # while both are unchanged; a new capture identity, a different unmatched
    # set or a changed registry needs `identities` again.
    previous = provenance.get("capture_identity")
    manifest_path = output / "_identities.json"
    shipped = (
        json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    )
    stale = (
        (identity is not None and identity != previous)
        or provenance.get("merge", {}).get("unmatched") != result["unmatched"]
        or shipped.get("maintained_extensions")
        != sorted(key for key, _ in extensions)
    )
    if identity is not None:
        provenance["capture_identity"] = identity
    if stale:
        manifest_path.unlink(missing_ok=True)
    provenance.update(
        schema_version=1,
        merge=result,
        overlays=[
            {"file": path.name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
            for path in overlays
        ],
        merged_outputs={
            path.relative_to(output).as_posix(): hashlib.sha256(
                path.read_bytes()
            ).hexdigest()
            for path in sorted(written)
        },
    )
    provenance_path.write_text(json.dumps(provenance, indent=2, sort_keys=True) + "\n")
    return result
