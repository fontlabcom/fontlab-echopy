# this_file: src/fontlab_echopy/_runtime.py
"""Identity-preserving delegation; documentation classes never wrap C++ values."""
from __future__ import annotations

import importlib
import sys
from types import ModuleType
from typing import Any, NoReturn


class NativeUnavailable(RuntimeError):
    """The operation needs a native module supplied by the FontLab host."""


def unavailable(name: str) -> NoReturn:
    """Reject documentation-only operations instead of returning dummy values."""
    raise NativeUnavailable(f"{name} requires the native API inside FontLab")


def resolve(name: str) -> Any:
    """Resolve PythonQt pseudo-namespaces through attributes, not import alone."""
    parts = name.split(".")
    try:
        value = importlib.import_module(parts[0])
    except ModuleNotFoundError as exc:
        if exc.name == parts[0]:
            return None
        raise
    for part in parts[1:]:
        value = getattr(value, part, None)
        if value is None:
            break
    return value


class NativeModule(ModuleType):
    """Delegate current native attributes, including mutable module globals."""

    def __getattribute__(self, name: str) -> Any:
        if not name.startswith("__") and name not in {"_echopy_native", "_echopy_name", "_echopy_aliases"}:
            native = ModuleType.__getattribute__(self, "_echopy_native")
            if native is not None:
                aliases = ModuleType.__getattribute__(self, "__dict__").get("_echopy_aliases", {})
                if name in aliases or name in aliases.values():
                    return getattr(native, aliases.get(name, name))
                try:
                    return getattr(native, name)
                except AttributeError:
                    pass
        return ModuleType.__getattribute__(self, name)

    def __getattr__(self, name: str) -> Any:
        native = self.__dict__.get("_echopy_native")
        if native is not None:
            return getattr(native, self.__dict__.get("_echopy_aliases", {}).get(name, name))
        raise AttributeError(name)

    def __dir__(self) -> list[str]:
        native = self.__dict__.get("_echopy_native")
        names = set(self.__dict__)
        if native is not None:
            aliases = self.__dict__.get("_echopy_aliases", {})
            native_names = set(dir(native))
            names.difference_update(aliases)
            names.difference_update(aliases.values())
            names.update(native_names)
            names.update(alias for alias, original in aliases.items() if original in native_names)
        return sorted(names)

    def __setattr__(self, name: str, value: Any) -> None:
        native = self.__dict__.get("_echopy_native")
        # Import machinery installs child facade modules on parent packages.
        # Those bookkeeping writes must never replace native PythonQt objects.
        is_facade = isinstance(value, NativeModule)
        if is_facade and native is None and isinstance(self.__dict__.get(name), type):
            # Some PythonQt classes also have an importable pseudo-namespace.
            # Preserve the offline class just as native delegation preserves it.
            return
        if native is not None and not name.startswith("__") and name not in {
            "_echopy_native", "_echopy_name", "_echopy_aliases"
        } and not is_facade:
            original = self.__dict__.get("_echopy_aliases", {}).get(name, name)
            setattr(native, original, value)
        else:
            ModuleType.__setattr__(self, name, value)

    def __delattr__(self, name: str) -> None:
        native = self.__dict__.get("_echopy_native")
        aliases = self.__dict__.get("_echopy_aliases", {})
        original = aliases.get(name, name)
        if native is not None and not name.startswith("__") and (
            name in aliases or name in aliases.values() or hasattr(native, original)
        ):
            delattr(native, original)
            self.__dict__.pop(name, None)
        else:
            ModuleType.__delattr__(self, name)


def bind(namespace: dict[str, Any], native_name: str, aliases: dict[str, str] | None = None) -> None:
    """Replace source declarations with native symbols without class mutation."""
    aliases = aliases or {}
    native = resolve(native_name)
    namespace["_echopy_aliases"] = {alias: original for original, alias in aliases.items()}
    if native is None:
        for original, alias in aliases.items():
            if alias in namespace:
                namespace[original] = namespace[alias]
    namespace["_echopy_native"] = native
    namespace["_echopy_name"] = native_name
    if native is not None:
        for name in dir(native):
            if not name.startswith("__"):
                namespace[name] = getattr(native, name)
                # Identity mappings also prevent stale fallback after native deletion.
                namespace["_echopy_aliases"].setdefault(name, name)
        namespace["__all__"] = [name for name in dir(native) if not name.startswith("__")]
    for original, alias in aliases.items():
        if original in namespace:
            namespace[alias] = namespace[original]
    module = sys.modules.get(namespace["__name__"])
    if module is not None:
        module.__class__ = NativeModule


def populate(namespace: dict[str, Any], native_name: str, aliases: dict[str, str]) -> None:
    """Bind instantly in FontLab; load source declarations only for offline docs.

Canonical .pyi sidecars retain complete annotations/docstrings. Outside FontLab,
their declarations become inspectable objects whose operations raise clearly.
Native imports never parse or compile the large documentation sidecars.
"""
    if resolve(native_name) is None:
        import ast
        from pathlib import Path
        path = Path(namespace["__file__"]).with_suffix(".pyi")
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                doc = ast.get_docstring(node)
                body = [ast.Expr(value=ast.Constant(value=doc))] if doc else []
                body.append(ast.Expr(value=ast.Call(func=ast.Name(id="_echopy_unavailable", ctx=ast.Load()), args=[ast.Constant(value=native_name + "." + node.name)], keywords=[])))
                node.body = body
        namespace["_echopy_unavailable"] = unavailable
        exec(compile(ast.fix_missing_locations(tree), str(path), "exec"), namespace)
    bind(namespace, native_name, aliases)
