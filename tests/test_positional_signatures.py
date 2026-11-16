# this_file: tests/test_positional_signatures.py
"""Generated declarations preserve receiver order and native defaults."""
import inspect

import pytest

from fontlab_echopy.tooling.generate import module_source


@pytest.mark.parametrize("text, method", [
    ("(value, /)", True),
    ("(value=1, /)", True),
    ("(value, /, other=2, *, flag=True)", True),
    ("(value=1, /, other=2, *rest, flag=True, **options)", True),
    ("(self, value=1, /)", True),
    ("(cls, value=1, /)", True),
    ("(value=1)", True),
    ("(*, value=1)", True),
    ("(value=1, /)", False),
])
def test_generated_signature_preserves_parameter_order_kinds_and_defaults(text, method):
    original = {}
    exec("def move" + text + ": pass", original)
    expected = list(inspect.signature(original["move"]).parameters.values())
    if method and expected[0].name not in {"self", "cls"}:
        kind = (inspect.Parameter.POSITIONAL_ONLY
                if expected[0].kind == inspect.Parameter.POSITIONAL_ONLY
                else inspect.Parameter.POSITIONAL_OR_KEYWORD)
        expected.insert(0, inspect.Parameter("self", kind))
    info = {"name": "move", "signature": text}
    scope = ({"classes": [{"name": "Point", "methods": [info]}]}
             if method else {"functions": [info]})
    namespace = {"__name__": "signature_fixture"}
    source = module_source("missing_signature_fixture_native", scope, True)
    exec(compile(source, "<generated-signature>", "exec"), namespace)
    function = namespace["Point"].move if method else namespace["move"]
    actual = [p.replace(annotation=inspect.Parameter.empty)
              for p in inspect.signature(function).parameters.values()]
    assert actual == expected, f"Generated declaration changed {text}: {actual}"
