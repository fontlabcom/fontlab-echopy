# this_file: src/fontlab_echopy/__init__.py
"""Native FontLab APIs with source-readable definitions for documentation.

Inside FontLab, exported native objects retain their identity. Outside FontLab,
modules can be inspected, but operations raise NativeUnavailable.
"""
import sys
from pathlib import Path
from importlib import import_module
from types import ModuleType
from ._runtime import NativeUnavailable

__all__ = ["fontlab", "fontgate", "fontpr", "fontlabpr", "PythonQt", "NativeUnavailable"]
# FL (FontLab 5 API) is listed once its shim has been generated from a native capture.
if Path(__file__).with_name("FL.py").exists():
    __all__.insert(4, "FL")


# Issue 201: Echopy shims only the native bindings. These generated packages moved.
MOVED = {
    **dict.fromkeys(("GlyphsApp", "vanilla", "AppKit", "Cocoa", "Foundation", "objc"), "fontlab-glyport"),
    "fontlabapp_shim": "fontlab-fontlabapp",
    "aidus_code_tools": "fontlab-aidus-code",
}


def _moved_error(name: str) -> ImportError:
    return ImportError(f"fontlab_echopy.{name} moved out of Echopy; it now belongs to {MOVED[name]}.")


class _MovedFinder:
    """Make `import fontlab_echopy.<moved>[.sub]` name the new home."""

    @staticmethod
    def find_spec(fullname: str, path=None, target=None):
        parts = fullname.split(".")
        if parts[0] == __name__ and len(parts) > 1 and parts[1] in MOVED:
            raise _moved_error(parts[1])
        return None


# A reload defines a new class; drop the old finder so only one stays registered.
sys.meta_path[:] = [f for f in sys.meta_path if getattr(f, "__name__", "") != "_MovedFinder"]
sys.meta_path.insert(0, _MovedFinder)


def __getattr__(name: str) -> ModuleType:
    if name in MOVED:
        raise _moved_error(name)
    if name in __all__:
        module = import_module(f"{__name__}.{name}")
        globals()[name] = module
        return module
    raise AttributeError(name)
