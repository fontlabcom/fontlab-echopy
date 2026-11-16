# this_file: src/fontlab_echopy/tooling/signatures.py
"""Conservative native-signature conversion; uncertain signatures remain variadic.

C++ type mappings retain the legacy generator's conventions. Native source text
is kept in docstrings so conversion never erases the original evidence.
"""
from __future__ import annotations

import ast
import keyword
import re

TYPES = {"void": "None", "bool": "bool", "int": "int", "uint": "int", "long": "int", "unsigned int": "int", "qint64": "int", "quint64": "int", "float": "float", "double": "float", "qreal": "float", "QString": "str", "QByteArray": "bytes", "QStringList": "list[str]", "QVariant": "Any", "QVariantList": "list[Any]", "QVariantMap": "dict[str, Any]"}


_QUOTED = re.compile(r"\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'", re.DOTALL)


def outside_literals(text: str) -> str:
    """Mask quoted content while retaining offsets into the original signature."""
    return _QUOTED.sub(lambda match: " " * len(match[0]), text)


def split_params(text: str) -> list[str]:
    """Split commas outside nested template, tuple, and default expressions."""
    parts, start, depth = [], 0, 0
    for index, char in enumerate(outside_literals(text)):
        if char in "(<[{":
            depth += 1
        elif char in ")>]}":
            depth -= 1
        elif char == "," and depth == 0:
            parts.append(text[start:index].strip())
            start = index + 1
    return [part for part in parts + [text[start:].strip()] if part]


def annotation(text: str) -> str:
    """Map known native types and preserve valid forward references."""
    text = re.sub(r"\bconst\b", "", text).strip().rstrip("&*").strip()
    if text in TYPES:
        return TYPES[text]
    template = re.fullmatch(r"(QList|QVector|QSet|QMap|QHash)<(.*)>", text)
    if template:
        container = {"QSet": "set", "QMap": "dict", "QHash": "dict"}.get(template[1], "list")
        return container + "[" + ", ".join(annotation(p) for p in split_params(template[2])) + "]"
    if re.fullmatch(r"[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*", text):
        return text if text in {"str", "bytes", "list", "dict", "tuple", "type", "Any", "None"} or text.startswith(("Q", "fl", "fg")) else "Any"
    return "Any"


def python_signature(text: str, method: bool) -> tuple[str, str] | None:
    """Parse a Python signature with AST and annotate undocumented parameters."""
    try:
        node = ast.parse("def function" + text + ": pass").body[0]
    except SyntaxError:
        return None
    args = node.args
    for arg in args.posonlyargs + args.args + args.kwonlyargs + [a for a in (args.vararg, args.kwarg) if a]:
        if arg.arg not in {"self", "cls"} and arg.annotation is None:
            arg.annotation = ast.Name(id="Any", ctx=ast.Load())
    if method and not any(a.arg in {"self", "cls"} for a in args.posonlyargs + args.args):
        receiver_group = args.posonlyargs if args.posonlyargs else args.args
        receiver_group.insert(0, ast.arg(arg="self"))
    # Native defaults sometimes contain addresses or expressions; only literal
    # defaults belong in executable documentation source.
    for group in (args.defaults, args.kw_defaults):
        for index, value in enumerate(group):
            if value is None:
                continue
            try:
                ast.literal_eval(value)
            except (ValueError, TypeError):
                group[index] = ast.Constant(value=Ellipsis)
    return ast.unparse(args), ast.unparse(node.returns) if node.returns else "Any"


def signature(text: str, name: str, method: bool = False) -> tuple[str, str]:
    """Convert a documented signature; never infer missing native parameters."""
    fallback = (("self, " if method else "") + "*args: Any, **kwargs: Any", "Any")
    text = (text or "").strip().removeprefix("X.")
    # Legacy docs append prose after a signature, not part of its grammar.
    separator = outside_literals(text).find(" - ")
    if separator >= 0:
        text = text[:separator]
    if text in {"", "(...)"}:
        return fallback
    if text.startswith("("):
        return python_signature(text, method) or fallback
    match = re.fullmatch(r"(?:(.+?)\s+)?" + re.escape(name) + r"\((.*)\)(?:\s*->\s*(.+))?", text)
    if not match:
        return fallback
    result = annotation(match[3] or (match[1] or "").removeprefix("static "))
    params = ["self"] if method else []
    for index, raw in enumerate(split_params(match[2])):
        part, sep, default = raw.partition("=")
        words = part.strip().split()
        arg = words[-1] if words else ""
        if not arg.isidentifier() or keyword.iskeyword(arg) or arg in {"self", "cls"}:
            return fallback
        typ = annotation(" ".join(words[:-1])) if len(words) > 1 else "Any"
        if len(words) == 1 and arg.startswith(("Q", "fl", "fg")):
            typ, arg = annotation(arg), f"arg{index}"
        param = arg + ": " + typ
        if sep:
            default = {"false": "False", "true": "True", "NULL": "None", "nullptr": "None"}.get(default.strip(), default.strip())
            try:
                ast.literal_eval(default)
            except (ValueError, SyntaxError):
                default = "..."
            param += " = " + default
        params.append(param)
    args = ", ".join(params)
    try:
        compile(f"def function({args}) -> {result}: pass", "<signature>", "exec")
    except SyntaxError:
        return fallback
    return args, result
