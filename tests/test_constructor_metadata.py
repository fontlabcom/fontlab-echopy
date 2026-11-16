# this_file: tests/test_constructor_metadata.py
"""Captured constructors survive generation without invoking native objects."""
import ast
import inspect
import types
import pytest
from fontlab_echopy.tooling.capture import namespace
from fontlab_echopy.tooling.generate import module_source, generate
from fontlab_echopy.tooling.merge import merge


@pytest.mark.parametrize("signature", ["(self, value, /, *, label='a,b')", "(self, value=3)", "(value, /)", "(...)"])
def test_single_constructor_retains_captured_signature_and_doc(signature):
    record = {"name": "Point", "signature": signature, "doc": "Owned constructor evidence."}
    source = module_source("missing_constructor_fixture", {"classes": [{"name": "Point", "constructors": [record]}]}, True)
    scope = {"__name__": "constructor_fixture"}
    exec(compile(source, "<owned>", "exec"), scope)
    init = scope["Point"].__init__
    assert record["name"] == "Point", "Generation must not mutate capture records"
    assert init.__doc__ == record["doc"]
    if signature != "(...)":
        from fontlab_echopy.tooling.signatures import signature as convert
        expected, _ = convert(signature, "__init__", True)
        node = ast.parse(source).body
        cls = next(n for n in node if isinstance(n, ast.ClassDef))
        assert ast.unparse(cls.body[1].args) == expected
    assert str(inspect.signature(init).return_annotation) == "None"


@pytest.mark.parametrize("first_doc", ["First overload.", "__init__(int value)"])
def test_multiple_constructors_retain_all_evidence_without_selecting_overload(first_doc):
    records = [{"name": "__init__", "signature": "(self, value)", "doc": first_doc}, {"name": "__init__", "signature": "(self, x, y)", "doc": "Second overload."}]
    source = module_source("missing_constructor_fixture", {"classes": [{"name": "Point", "constructors": records}]}, True)
    scope = {"__name__": "constructor_fixture"}
    exec(compile(source, "<owned>", "exec"), scope)
    init = scope["Point"].__init__
    assert list(inspect.signature(init).parameters) == ["self", "args", "kwargs"]
    for record in records:
        assert record["signature"] in init.__doc__ and record["doc"] in init.__doc__


def test_capture_generate_merge_preserves_constructor_without_instantiation(tmp_path):
    class Point:
        def __init__(self, value, /, *, label="a,b") -> None:
            """Captured init-only documentation."""
            raise AssertionError("Never instantiate while documenting")
    module = types.ModuleType("missing_constructor_fixture")
    module.Point = Point
    data = {"modules": {module.__name__: {"namespace": namespace(module, module.__name__)}}}
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    generate(data, raw)
    merge(raw, merged, [])
    tree = ast.parse((merged / (module.__name__ + ".pyi")).read_text())
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef))
    init = next(n for n in cls.body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
    assert ast.get_docstring(init) == Point.__init__.__doc__
    assert [p.arg for p in init.args.posonlyargs] == ["self", "value"]
    assert [p.arg for p in init.args.kwonlyargs] == ["label"]
    assert ast.literal_eval(init.args.kw_defaults[0]) == "a,b"


@pytest.mark.parametrize("extra", [{}, {"constructors": []}])
def test_absent_constructor_metadata_retains_legacy_fallback(extra):
    from fontlab_echopy._runtime import NativeUnavailable
    source = module_source("missing_constructor_fixture", {"classes": [{"name": "Point", **extra}]}, True)
    scope = {"__name__": "constructor_fixture"}
    exec(compile(source, "<owned>", "exec"), scope)
    init = scope["Point"].__init__
    assert list(inspect.signature(init).parameters) == ["self", "args", "kwargs"]
    assert init.__doc__ == "Native constructor; consult class documentation for supported overloads."
    with pytest.raises(NativeUnavailable, match="missing_constructor_fixture.Point"):
        scope["Point"]()
