# this_file: src/fontlab_echopy/_patch_extensions.py
# Generated from maintained extension patches; regenerate with merge.
"""Executable overlay helpers; installation is explicitly requested."""
from __future__ import annotations
from typing import Any
def _extension_0(self) -> str:
    """Read the objectName after explicit install_extensions()."""
    from fontlab_echopy.extensions import object_name
    return object_name(self)
def _extension_1(self, name: str) -> bool:
    """Check for a named layer; see extensions.has_layer on immutable classes."""
    from fontlab_echopy.extensions import has_layer
    return has_layer(self, name)
def _extension_2(self) -> list[str]:
    """List layer names; immutable native classes use extensions.layer_names."""
    from fontlab_echopy.extensions import layer_names
    return layer_names(self)
EXTENSIONS = {
    'PythonQt.QtGui.QWidget.echopy_object_name': _extension_0,
    'fontlab.flGlyph.has_layer': _extension_1,
    'fontlab.flGlyph.layer_names': _extension_2,
}
