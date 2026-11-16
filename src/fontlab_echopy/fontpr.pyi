# this_file: src/fontlab_echopy/fontpr.pyi
# Generated from native metadata and independent enrichment inputs.
"""FontLab MCP tools for embedded Python."""
from __future__ import annotations
from typing import Any

class Error:
    """Common base class for all non-exit exceptions.

Native bases: Exception"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Native constructor; consult class documentation for supported overloads."""
        ...

    def add_note(self, *args: Any, **kwargs: Any) -> Any:
        """Exception.add_note(note) --
add a note to the exception"""
        ...

    def with_traceback(self, *args: Any, **kwargs: Any) -> Any:
        """Exception.with_traceback(tb) --
set self.__traceback__ to tb and return self."""
        ...
    args: Any

def available(*args: Any, **kwargs: Any) -> Any:
    """Return True when MCP tools are ready."""
    ...

def build_glyph(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def call(*args: Any, **kwargs: Any) -> Any:
    """call(name, **kwargs) - invoke an MCP tool."""
    ...

def close_font(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def delete_all_kerning_classes(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def delete_all_kerning_pairs(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def delete_kerning_class(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def delete_kerning_pair(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def edit_glyph_nodes(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def edit_layer_hints(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def explain(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def geometry(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_active_font(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_active_glyphs(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_current_glyphs(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_font_info(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_font_metrics(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_glyph(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_glyph_metrics(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_glyph_nodes(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_kerning_pair(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_layer_hints(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def get_preferences(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def list_actions(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def list_aidus_files(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def list_fonts(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def list_glyphs(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def list_kerning_classes(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def list_kerning_pairs(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def list_tools(*args: Any, **kwargs: Any) -> Any:
    """Return MCP tool metadata."""
    ...

def new_font(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def open_font(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def read_aidus_file(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def rename_kerning_class(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def run_actions(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def save_font(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_active_font(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_active_glyph(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_font_info(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_font_metrics(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_glyph(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_glyph_anchors(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_glyph_metrics(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_kerning_class(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_kerning_pair(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def set_preferences(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...

def write_aidus_file(*args: Any, **kwargs: Any) -> Any:
    """Call an MCP tool by name."""
    ...
__all__ = ['Error', 'available', 'build_glyph', 'call', 'close_font', 'delete_all_kerning_classes', 'delete_all_kerning_pairs', 'delete_kerning_class', 'delete_kerning_pair', 'edit_glyph_nodes', 'edit_layer_hints', 'explain', 'geometry', 'get_active_font', 'get_active_glyphs', 'get_current_glyphs', 'get_font_info', 'get_font_metrics', 'get_glyph', 'get_glyph_metrics', 'get_glyph_nodes', 'get_kerning_pair', 'get_layer_hints', 'get_preferences', 'list_actions', 'list_aidus_files', 'list_fonts', 'list_glyphs', 'list_kerning_classes', 'list_kerning_pairs', 'list_tools', 'new_font', 'open_font', 'read_aidus_file', 'rename_kerning_class', 'run_actions', 'save_font', 'set_active_font', 'set_active_glyph', 'set_font_info', 'set_font_metrics', 'set_glyph', 'set_glyph_anchors', 'set_glyph_metrics', 'set_kerning_class', 'set_kerning_pair', 'set_preferences', 'write_aidus_file']
