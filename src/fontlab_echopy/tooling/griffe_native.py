# this_file: src/fontlab_echopy/tooling/griffe_native.py
"""Preserve captured native classes that also have empty pseudo-namespaces.

PythonQt.BoolResult is a callable native class and an introspectable object.
Griffe's ordinary child-module bookkeeping otherwise shadows the class with
its empty namespace. Restore only the class explicitly present in the merged
sidecar, without importing native code or inventing members.
"""

from pathlib import Path
from typing import Any

from griffe import Extension, visit


class NativeNamespaceExtension(Extension):
    """Use the actual enriched source declaration for an empty child facet."""

    def on_package(self, *, pkg: Any, loader: Any, **kwargs: Any) -> None:
        if pkg.name != "fontlab_echopy" or "PythonQt" not in pkg.members:
            return
        qt = pkg.members["PythonQt"]
        path = Path(qt.filepath).with_suffix(".pyi")
        declared = visit(
            "PythonQt",
            filepath=path,
            code=path.read_text(),
            modules_collection=loader.modules_collection,
        )
        for name, candidate in declared.members.items():
            existing = qt.members.get(name)
            if (
                not candidate.is_alias
                and candidate.is_class
                and existing is not None
                and existing.is_module
                and existing.exports is not None
                and not existing.exports
            ):
                qt.set_member(name, candidate)
