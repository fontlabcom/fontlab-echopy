# this_file: src/fontlab_echopy/tooling/identities.py
"""Ship the captured identity contract so documentation can reconcile it offline.

The raw capture is a local input and is not distributed. This manifest records
every captured scope, name, class member and constructor, the source identity
the generator gives each one, and the merge facts documentation needs. Deriving
it reads the capture and the merged package; it never rewrites the sidecars.
"""

from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path
from typing import Any

from .generate import _source_names, scopes, source_name

MANIFEST = "_identities.json"


def _scope_names(namespace: dict[str, Any]) -> list[str]:
    """`names`, or the declaration collections the generator falls back to."""
    if namespace.get("names"):
        return sorted(namespace["names"])
    keys = ("classes", "functions", "attributes", "constants", "modules")
    return sorted({item["name"] for key in keys for item in namespace.get(key, [])})


def _class_members(cls: dict[str, Any]) -> list[str]:
    """`names`, or the non-dunder methods and attributes the generator emits."""
    if cls.get("names"):
        return sorted(cls["names"])
    keys = ("methods", "attributes", "constants")
    return sorted({m["name"] for key in keys for m in cls.get(key, []) if not m["name"].startswith("__")})


def _extensions(package: Path) -> list[str]:
    """Read the maintained extension registry that merge generated."""
    tree = ast.parse((package / "_patch_extensions.py").read_text())
    for node in tree.body:
        if (
            isinstance(node, ast.Assign)
            and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id == "EXTENSIONS"
            and isinstance(node.value, ast.Dict)
        ):
            return sorted(ast.literal_eval(key) for key in node.value.keys)
    raise ValueError("Extension registry missing from _patch_extensions.py")


def derive_identities(capture: Path | bytes, package: Path) -> dict[str, Any]:
    """Derive the manifest; the capture must be the one the package was built from."""
    package = Path(package)
    data = capture if isinstance(capture, bytes) else Path(capture).read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    provenance = json.loads((package / "_provenance.json").read_text())
    built_from = provenance.get("capture_identity", {}).get("sha256")
    if built_from != digest:
        raise ValueError(
            f"capture {digest} is not the generation input {built_from}"
        )
    modules = json.loads(data)["modules"]
    result: dict[str, Any] = {}
    spellings: dict[str, str] = {}
    for scope, namespace, _package, available in scopes(json.loads(data)):
        top, _, child = scope.partition(".")
        entry = modules[top]
        kind = entry["subpackages"][child].get("kind", "module") if child else "module"
        row: dict[str, Any] = {
            "available": available,
            "kind": kind,
            "names": _scope_names(namespace),
            "errors": namespace.get("errors", []),
            "classes": {},
        }
        if not available:
            row["reason"] = entry.get("reason", "native module absent")
        top_names = _source_names(scope, row["names"])
        for cls in sorted(namespace.get("classes", []), key=lambda c: c["name"]):
            members = _class_members(cls)
            constructors = sorted({c["name"] for c in cls.get("constructors", [])})
            owner = scope + "." + top_names.get(cls["name"], source_name(cls["name"]))
            # The generator emits constructors under their dunder name verbatim.
            mapped = _source_names(owner, members) | {c: c for c in constructors}
            row["classes"][cls["name"]] = {
                "members": members,
                "constructors": constructors,
                "errors": cls.get("errors", []),
            }
            native_owner = scope + "." + cls["name"]
            for name in members + constructors:
                native, source = native_owner + "." + name, owner + "." + mapped[name]
                if native != source:
                    spellings[native] = source
        for name, source in top_names.items():
            if name != source:
                spellings[scope + "." + name] = scope + "." + source
        result[scope] = row
    enrichment = provenance.get("qt_enrichment", {})
    return {
        "schema_version": 1,
        "producer": "fontlab_echopy.tooling.identities",
        "capture_sha256": digest,
        "scopes": result,
        "native_spellings": dict(sorted(spellings.items())),
        "maintained_extensions": _extensions(package),
        "merge_unmatched": provenance.get("merge", {}).get("unmatched", []),
        "enrichment_gaps": {
            "qt_document_failures": enrichment.get("qt_document_failures", {}),
            "unmatched_native_classes": enrichment.get("unmatched_native_classes", []),
        },
    }


def _encode(manifest: dict[str, Any]) -> str:
    return json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n"


def write_identities(capture: Path | bytes, package: Path) -> dict[str, Any]:
    """Write only the manifest file into the merged package."""
    manifest = derive_identities(capture, package)
    (Path(package) / MANIFEST).write_text(_encode(manifest), encoding="utf-8")
    return manifest


def verify_identities(capture: Path, package: Path) -> dict[str, Any]:
    """Re-derive from the raw capture; a missing capture fails instead of skipping."""
    if not Path(capture).is_file():
        raise FileNotFoundError(f"Raw capture not found: {capture}")
    manifest = derive_identities(capture, package)
    shipped = (Path(package) / MANIFEST).read_text(encoding="utf-8")
    if shipped != _encode(manifest):
        raise ValueError(f"{MANIFEST} differs from the manifest derived from {capture}")
    return manifest
