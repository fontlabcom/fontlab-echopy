# this_file: examples/native_smoke.py
"""Run inside FontLab against an installed wheel; does not edit open fonts."""
import importlib
import json
import fontlab as native_fl
import fontgate as native_fg
import PythonQt
from echopy import fontlab as fl, fontgate as fg, fontpr
from fontlab_echopy.extensions import install_extensions, object_name
from fontlab_echopy._runtime import resolve

assert fl.flNode is native_fl.flNode
assert fg.fgGlyph is native_fg.fgGlyph
node = fl.flNode(12, 34)
assert isinstance(node, native_fl.flNode)
assert (node.x, node.y) == (12, 34)
node.x = 56
assert node.x == 56
qtgui = importlib.import_module("fontlab_echopy.PythonQt.QtGui")
qtcore = importlib.import_module("fontlab_echopy.PythonQt.QtCore")
widget = qtgui.QWidget()
point = qtcore.QPointF(12, 34)
copied_point = qtcore.QPointF(point)
assert copied_point.x() == 12 and copied_point.y() == 34
widget.resize(qtcore.QSize(23, 45))
assert isinstance(widget.size, PythonQt.QtCore.QSize)
widget.objectName = "echopy-native-smoke"
had_extension = hasattr(PythonQt.QtGui.QWidget, "echopy_object_name")
try:
    installed = install_extensions()
    assert object_name(widget) == "echopy-native-smoke"
    assert widget.echopy_object_name() == "echopy-native-smoke"
    assert fontpr.available()
    coverage = {}
    for name in ["fontlab", "fontgate", "fontpr", "PythonQt"]:
        native = importlib.import_module(name)
        facade = importlib.import_module("fontlab_echopy." + name)
        missing = [member for member in dir(native) if not member.startswith("__") and getattr(facade, member) is not getattr(native, member)]
        assert not missing, (name, missing)
        coverage[name] = len([member for member in dir(native) if not member.startswith("__")])
    for child in ("BoolResult", "Config", "Debug", "Qt", "QtCore", "QtGui", "QtNetwork", "QtOpenGL", "QtSvg", "QtUiTools", "QtXmlPatterns", "private"):
        name = "PythonQt." + child
        native = resolve(name)
        facade = importlib.import_module("fontlab_echopy." + name)
        names = [member for member in dir(native) if not member.startswith("__")]
        for member in names:
            original, wrapped = getattr(native, member), getattr(facade, member)
            assert type(original) is type(wrapped), (name, member)
            if isinstance(original, type):
                assert original is wrapped, (name, member)
        coverage[name] = len(names)
    print(json.dumps({"identity": True, "constructors": True, "native_argument_conversion": True, "native_return_type": True, "properties": True, "extensions": installed, "native_name_coverage": coverage}, sort_keys=True))
finally:
    if not had_extension and hasattr(PythonQt.QtGui.QWidget, "echopy_object_name"):
        delattr(PythonQt.QtGui.QWidget, "echopy_object_name")
    widget.deleteLater()
