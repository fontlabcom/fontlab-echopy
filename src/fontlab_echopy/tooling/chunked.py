# this_file: src/fontlab_echopy/tooling/chunked.py
"""Capture one native module through several short host calls.

Each remopy ``run`` has a 5 s deadline, 32 KiB of code and 64 KiB of output, so
one module is surveyed first and then captured in small name groups. Everything
is read-only: names, classes and signatures only, never property values.
"""
from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import Any

from . import capture as _capture
from .capture import finish_module

BUDGET = 120  # Members per host call; each call is split further when it fails.
_RESOLVE = "from fontlab_echopy._runtime import resolve"
_STUB = "def resolve(name):\n    import importlib\n    return importlib.import_module(name)"

SURVEY = """
import importlib, inspect
try:
    module = importlib.import_module(MODULE)
except ModuleNotFoundError as error:
    if error.name != MODULE:
        raise
    result = {"available": False}
else:
    names = sorted(n for n in dir(module) if not n.startswith("__"))
    sizes = {}
    for n in names:
        try:
            obj = getattr(module, n)
            kind = obj if inspect.isclass(obj) else type(obj)
            sizes[n] = len(dir(kind)) if kind.__module__ != "builtins" else 1
        except Exception:
            sizes[n] = 1
    exports = getattr(module, "__all__", None)
    result = {"available": True, "names": names, "sizes": sizes,
              "exports": None if exports is None else list(exports), "doc": inspect.getdoc(module) or ""}
"""

CHUNK = """
import importlib
result = namespace(importlib.import_module(MODULE), MODULE, only=ONLY, instances=True)
"""


def remote_source(body: str) -> str:
    """Self-contained code: the capture module (no Echopy install needed) plus ``body``."""
    source = Path(_capture.__file__).read_text(encoding="utf-8")
    if _RESOLVE not in source:
        raise RuntimeError("capture.py no longer imports resolve as expected")
    return source.replace(_RESOLVE, _STUB) + "\n" + body


def plan_chunks(sizes: dict[str, int], budget: int = BUDGET) -> list[list[str]]:
    """Group names so each group's member count stays within ``budget``."""
    chunks: list[list[str]] = []
    total = 0
    for name in sorted(sizes):
        if not chunks or total + sizes[name] > budget:
            chunks.append([])
            total = 0
        chunks[-1].append(name)
        total += sizes[name]
    return chunks


def capture_module(run: Callable[..., Any], module: str, failures: tuple[type[Exception], ...]) -> dict[str, Any]:
    """``run(code, **vars)`` must return an object with ``.value``; returns a capture item."""
    survey = run(remote_source(SURVEY), MODULE=module).value
    if not survey["available"]:
        return {"available": False, "reason": "native module absent", "namespace": {}}
    code = remote_source(CHUNK)
    scope: dict[str, Any] = {"name": module, "doc": survey["doc"], "names": survey["names"],
                             "classes": [], "functions": [], "attributes": [], "errors": []}

    def fetch(names: list[str]) -> None:
        try:
            part = run(code, MODULE=module, ONLY=names).value
        except failures as error:
            if len(names) > 1:
                middle = len(names) // 2
                fetch(names[:middle])
                fetch(names[middle:])
                return
            # One name that cannot be captured is a recorded gap, as in a direct capture.
            scope["errors"].append({"name": names[0], "error": type(error).__name__})
            scope["attributes"].append({"name": names[0], "type": "Any", "doc": "Native member could not be inspected."})
            return
        for key in ("classes", "functions", "attributes", "errors", "instance_classes"):
            scope.setdefault(key, []).extend(part.get(key, []))

    for names in plan_chunks(survey["sizes"]):
        fetch(names)
    return {"available": True, "namespace": finish_module(scope, survey["exports"]), "subpackages": {}}
