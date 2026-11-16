# this_file: src/echopy/__init__.py
"""Lazy compatibility aliases sharing canonical fontlab_echopy modules."""
from importlib import import_module, util
from importlib.abc import Loader, MetaPathFinder
from importlib.machinery import ModuleSpec
import sys
from pathlib import Path
from types import ModuleType

__all__ = ["fontlab", "fontgate", "fontpr", "fontlabpr", "PythonQt"]
_canonical = util.find_spec("fontlab_echopy")  # Locates the package without importing it.
if _canonical is not None and _canonical.origin and Path(_canonical.origin).with_name("FL.py").exists():
    __all__.insert(4, "FL")  # Listed once the FL shim has been generated from a capture.


class _AliasLoader(Loader):
    """Reuse a canonical module, retaining its canonical import metadata."""

    def __init__(self, canonical: str) -> None:
        self.canonical = canonical

    def create_module(self, spec: ModuleSpec) -> ModuleType:
        module = import_module(self.canonical)
        self.original_spec = module.__spec__
        return module

    def exec_module(self, module: ModuleType) -> None:
        module.__spec__ = self.original_spec


class _AliasFinder(MetaPathFinder):
    """Resolve only echopy's namespace, without eagerly importing Qt sources."""
    _echopy_alias = True

    def find_spec(self, fullname: str, path: list[str] | None = None, target: ModuleType | None = None) -> ModuleSpec | None:
        if not fullname.startswith("echopy."):
            return None
        canonical = "fontlab_echopy." + fullname.removeprefix("echopy.")
        original = util.find_spec(canonical)
        if original is None:
            return None
        return util.spec_from_loader(fullname, _AliasLoader(canonical), is_package=original.submodule_search_locations is not None)


if not any(getattr(finder, "_echopy_alias", False) for finder in sys.meta_path):
    sys.meta_path.insert(0, _AliasFinder())


def __getattr__(name: str) -> ModuleType:
    if name in __all__:
        module = import_module(__name__ + "." + name)
        globals()[name] = module
        return module
    raise AttributeError(name)
