# this_file: src/fontlab_echopy/extensions.py
"""Native-compatible helpers, also usable when a native class is immutable.

No native method is replaced. Explicit installation adds convenience methods to
mutable classes and reports immutable classes instead of changing class identity.
"""
from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any
from ._runtime import resolve


def layer_names(glyph: Any) -> list[str]:
    """List layer names on a native flGlyph, preserving its native objects."""
    return [layer.name for layer in glyph.layers]


def has_layer(glyph: Any, name: str) -> bool:
    """Fallback convenience operation for hosts without has_layer."""
    return name in layer_names(glyph)


def object_name(widget: Any) -> str:
    """Read PythonQt's objectName property or a callable Qt binding accessor."""
    name = widget.objectName
    return str(name() if callable(name) else name)


def get_extension(key: str, specs: Mapping[str, Callable[..., Any]] | None = None) -> Callable[..., Any]:
    """Return a merged patch function for direct use on immutable native classes."""
    if specs is None:
        from ._patch_extensions import EXTENSIONS
        specs = EXTENSIONS
    return specs[key]


def install_extensions(specs: Mapping[str, Callable[..., Any]] | None = None) -> dict[str, str]:
    """Add non-colliding helpers; return explicit installed/existing/immutable status."""
    if specs is None:
        from ._patch_extensions import EXTENSIONS
        specs = EXTENSIONS
    result = {}
    for key, function in specs.items():
        path, member = key.rsplit(".", 1)
        cls = resolve(path)
        if cls is None:
            result[key] = "unavailable"
        elif hasattr(cls, member):
            result[key] = "existing"
        else:
            try:
                setattr(cls, member, function)
                result[key] = "installed"
            except (TypeError, AttributeError):
                result[key] = f"immutable; use fontlab_echopy.extensions.get_extension({key!r})"
    return result
