# this_file: tests/test_capture_discovery_pipeline.py
"""Newly discovered owned APIs survive the real capture/generate/merge pipeline."""

import ast
import sys
from types import ModuleType

from fontlab_echopy.tooling import capture as tool
from fontlab_echopy.tooling.generate import generate
from fontlab_echopy.tooling.merge import merge


def test_pipeline_when_registered_namespace_has_hidden_names_then_keeps_complete_declarations(
    tmp_path, monkeypatch
):
    class Partial(ModuleType):
        def __dir__(self):
            return []

    class Hidden:
        """Owned discovered class documentation."""

        def __init__(self, count=7):
            raise AssertionError("Capture must not construct an API instance")

        def operation(self, amount=3):
            """Owned callable documentation."""
            raise AssertionError("Capture must not invoke an API operation")

    root, child = ModuleType("PythonQt"), Partial("PythonQt.QtOwnedPipeline")
    child.Hidden, child.marker = Hidden, 1
    monkeypatch.setitem(sys.modules, "PythonQt", root)
    monkeypatch.setitem(sys.modules, child.__name__, child)
    monkeypatch.setattr(tool, "QT_SEEDS", ())
    data = tool.capture(["PythonQt"])
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    report = generate(data, raw)
    merge(raw, merged, [])
    scope = report["modules"][child.__name__]
    assert scope["native_names"] == 2 and scope["missing_names"] == []
    assert scope["missing_class_members"] == {} and scope["inspection_errors"] == []
    tree = ast.parse((merged / "PythonQt/QtOwnedPipeline.pyi").read_text())
    cls = next(node for node in tree.body if isinstance(node, ast.ClassDef))
    assert cls.name == "Hidden"
    assert ast.get_docstring(cls) == Hidden.__doc__ + "\n\nNative bases: object\n\nCaptured native MRO: Hidden, object"
    methods = {node.name: node for node in cls.body if isinstance(node, ast.FunctionDef)}
    assert ast.literal_eval(methods["__init__"].args.defaults[0]) == 7
    assert ast.literal_eval(methods["operation"].args.defaults[0]) == 3
    assert ast.get_docstring(methods["operation"]) == Hidden.operation.__doc__
    assert "marker: int" in ast.unparse(tree)


def test_pipeline_when_child_import_dependency_fails_then_report_retains_failure(
    tmp_path, monkeypatch
):
    root = ModuleType("PythonQt")
    monkeypatch.setattr(tool, "resolve", lambda name: root)
    monkeypatch.setattr(tool, "QT_SEEDS", ("QtOwnedDependency",))

    def load(name):
        raise ModuleNotFoundError("owned missing dependency", name="owned_dependency")

    monkeypatch.setattr("importlib.import_module", load)
    report = generate(tool.capture(["PythonQt"]), tmp_path / "raw")
    assert report["modules"]["PythonQt"]["inspection_errors"] == [
        {"name": "QtOwnedDependency", "error": "ModuleNotFoundError"}
    ], "A complete declaration count must not erase failed discovery"
