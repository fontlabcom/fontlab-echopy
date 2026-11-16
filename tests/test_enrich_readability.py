# this_file: tests/test_enrich_readability.py
"""Upstream HTML structure belongs in readable source docstrings."""

import ast

from fontlab_echopy.tooling.enrich import parse_qt
from fontlab_echopy.tooling.merge import enrich_node


def test_enrichment_when_overloads_exist_then_each_signature_stays_on_its_own_code_line():
    node = ast.parse(
        'def resize(self, w, h):\n    """Captured native resize."""\n    ...'
    ).body[0]
    signatures = [
        "resize(self, size: QSize) -> None",
        "resize(self, w: int, h: int) -> None",
    ]
    enrich_node(node, {"signatures": signatures})
    doc = ast.get_docstring(node)
    assert "```python\n" + "\n".join(signatures) + "\n```" in doc, (
        "overloads must render as readable source lines"
    )
    assert doc.startswith("Captured native resize."), (
        "enrichment must retain native evidence"
    )


def test_qt_when_structured_description_then_paragraphs_code_links_and_list_survive():
    html = """<div class="descr"><h2>Detailed Description</h2>
    <p>A readable paragraph with <code>QWidget</code>.</p>
    <p>A second paragraph with <a href="qobject.html">QObject</a>.</p>
    <ul><li>First item</li><li>Second item</li></ul>
    <pre>widget.resize(120, 80);\nwidget.show();</pre></div>
    <h3 class="fn" id="resize">void resize(int w, int h)</h3>
    <p>Resize the widget.</p><p>Preserve the height.</p>"""
    doc = parse_qt(html, source_url="https://doc.qt.io/archives/qt-5.15/qwidget.html")
    assert "`QWidget`" in doc["doc"]
    assert "\n\nA second paragraph" in doc["doc"]
    assert "[QObject](https://doc.qt.io/archives/qt-5.15/qobject.html)" in doc["doc"]
    assert "- First item" in doc["doc"]
    assert (
        "```" in doc["doc"] and "widget.resize(120, 80);\nwidget.show();" in doc["doc"]
    )
    assert "Resize the widget.\n\nPreserve the height." in doc["members"]["resize"]


def test_qt_when_cpp_subscript_operator_then_markdown_does_not_invent_relative_link():
    html = '<div class="descr"><p>Use operator[](int i).</p><p><a href="qjsonvalue.html">operator[]</a>(key)</p></div>'
    doc = parse_qt(html)
    assert r"operator\[\](int i)" in doc["doc"]
    assert r"[operator\[\]](" in doc["doc"]
