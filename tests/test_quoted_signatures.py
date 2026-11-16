# this_file: tests/test_quoted_signatures.py
"""Quoted native defaults must survive generated executable declarations."""
import inspect
import pytest
from fontlab_echopy.tooling.generate import module_source
from fontlab_echopy.tooling.signatures import annotation, signature, split_params


@pytest.mark.parametrize("value", ["a,b", "(", "]", "<", "}", 'a\"b,c', "a'b,c", r"a\b,c", "a - b", ") - marker", "a\"b'c,d", ""])
@pytest.mark.parametrize("method", [False, True])
def test_generated_native_default_preserves_literal_and_following_parameter(value, method):
    literal = repr(value)
    info = {"name": "draw", "signature": f"void draw(QString text = {literal}, int count = 2)"}
    scope = ({"classes": [{"name": "Canvas", "methods": [info]}]} if method else {"functions": [info]})
    namespace = {"__name__": "quoted_signature_fixture"}
    exec(compile(module_source("missing_quoted_fixture_native", scope, True), "<fixture>", "exec"), namespace)
    function = namespace["Canvas"].draw if method else namespace["draw"]
    params = list(inspect.signature(function).parameters.values())
    assert [p.name for p in params] == (["self"] if method else []) + ["text", "count"]
    assert [p.default for p in params[-2:]] == [value, 2], "Literal defaults must remain exact"


def test_trailing_prose_preserves_separator_inside_quoted_default():
    args, result = signature('void draw(QString text = "a - b,c", int count = 2) - native description', 'draw')
    assert args == 'text: str = "a - b,c", count: int = 2'
    assert result == 'None'


def test_nested_template_parameters_and_literal_delimiters_remain_separate():
    assert split_params('QMap<QString, QList<int>> values, QString text="[,)", int count=2') == ['QMap<QString, QList<int>> values', 'QString text="[,)"', 'int count=2']
    assert annotation('QMap<QString, QList<int>>') == 'dict[str, list[int]]'


def test_unterminated_native_literal_keeps_variadic_fallback():
    assert signature('void draw(QString text="a,b)', 'draw') == ('*args: Any, **kwargs: Any', 'Any')
