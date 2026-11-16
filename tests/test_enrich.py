# this_file: tests/test_enrich.py
"""Realistic upstream parsing fixtures plus explicit extension behavior."""
import zipfile

from fontlab_echopy.extensions import has_layer, layer_names, object_name
from fontlab_echopy.tooling.enrich import parse_qt, parse_stubs


def test_stub_overloads_and_class_members(tmp_path):
    path = tmp_path / "pyside.whl"
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("PySide2/QtWidgets.pyi", "class QWidget:\n    @overload\n    def resize(self, w: int, h: int) -> None: ...\n    @overload\n    def resize(self, size: QSize) -> None: ...\n")
    data = parse_stubs(path)
    assert len(data["QWidget"]["members"]["resize"]) == 2
    assert data["QWidget"]["module"] == "QtWidgets"


def test_qt_doc_parser_keeps_member_signatures_and_descriptions():
    html = '''<div class="descr"><h2>Detailed Description</h2><p>The QWidget class is the base of all UI objects.</p></div>
    <h3 class="fn" id="resize">void QWidget::resize(int w, int h)</h3><p>Resizes the widget to width w and height h.</p>
    <h3 class="fn" id="resize-1">void QWidget::resize(const QSize &amp;size)</h3><p>This is an overloaded function.</p>'''
    data = parse_qt(html)
    assert "base of all UI" in data["doc"]
    assert "int w" in data["members"]["resize"]
    assert "overloaded" in data["members"]["resize"]


def test_helpers_preserve_native_like_values():
    class Layer:
        name = "Regular"
    class Glyph:
        layers = [Layer()]
    class Widget:
        objectName = "panel"
    assert layer_names(Glyph()) == ["Regular"]
    assert has_layer(Glyph(), "Regular")
    assert not has_layer(Glyph(), "Missing")
    assert object_name(Widget()) == "panel"
