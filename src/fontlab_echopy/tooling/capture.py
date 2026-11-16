# this_file: src/fontlab_echopy/tooling/capture.py
"""Read native API metadata without constructing objects or invoking methods.

Replaces the bounded legacy introspector. Values, addresses, interpreter paths,
and user documents are deliberately not captured. No member-count limits apply.
"""
from __future__ import annotations

from collections.abc import Mapping
import ast
import importlib
import inspect
import re
import sys
from typing import Any

from fontlab_echopy._runtime import resolve

TARGETS = ("fontlab", "fontgate", "fontpr", "fontlabpr", "FL", "PythonQt")
# FontLab 5 style module: star exports and module-level instances such as `fl`.
FL_SHAPED = ("FL",)
QT_SEEDS = ("BoolResult", "Config", "Debug", "Qt", "QtCore", "QtGui", "QtNetwork", "QtOpenGL", "QtSvg", "QtUiTools", "QtXmlPatterns", "private")


def clean_doc(value: Any) -> str:
    """Keep API documentation while removing host-specific filesystem paths."""
    doc = inspect.getdoc(value) or ""
    return re.sub(r"/(?:Users|home|tmp|private/var)/[^\s'\"<>]+", "<local-path>", doc)


def callable_info(name: str, value: Any) -> dict[str, Any]:
    """Use inspect signatures when supported; retain native docs as evidence."""
    evidence = {}
    try:
        sig = str(inspect.signature(value))
        evidence["signature_source"] = "inspect.signature"
    except (TypeError, ValueError):
        sig = "(...)"
        text = getattr(value, "__text_signature__", None)
        if isinstance(text, str) and text:
            evidence["text_signature"] = text
            try:
                tree = ast.parse("def _" + text + ": pass")
                function = tree.body[0]
                if len(tree.body) != 1 or len(function.body) != 1 or not isinstance(function.body[0], ast.Pass):
                    raise ValueError("Text signature contains statements")
                compile(tree, "<text-signature>", "exec")
                args = function.args
                for default in args.defaults + [v for v in args.kw_defaults if v is not None]:
                    ast.literal_eval(default)
            except (SyntaxError, ValueError, TypeError):
                evidence["signature_source"] = "unresolved __text_signature__"
            else:
                sig = text
                evidence["signature_source"] = "__text_signature__"
    return {"name": name, "doc": clean_doc(value), "signature": sig, **evidence}


def _names(value: Any, errors: list[dict[str, str]]) -> list[str]:
    """Union advertised and stored names without evaluating instance properties."""
    names = set()
    for source in ("__dir__", "__dict__"):
        try:
            found = dir(value) if source == "__dir__" else getattr(value, source, {})
            if source == "__dir__" or isinstance(found, Mapping):
                names.update(n for n in found if isinstance(n, str) and not n.startswith("__"))
        except TimeoutError:
            raise
        except Exception as exc:
            errors.append({"name": source, "error": type(exc).__name__})
    return sorted(names)


def class_info(obj: type, name: str) -> dict[str, Any]:
    """One class: members, bases and constructor, without recursing into nested types."""
    info = namespace(obj, name, False)
    info["methods"] = info.pop("functions")
    info["bases"] = [base.__name__ for base in obj.__bases__]
    info["mro"] = [base.__name__ for base in obj.__mro__]
    descriptor = inspect.getattr_static(obj, "__init__", None)
    if isinstance(descriptor, (staticmethod, classmethod)):
        constructor = callable_info("__init__", descriptor.__func__)
        constructor["binding"] = "staticmethod" if isinstance(descriptor, staticmethod) else "classmethod"
    else:
        constructor = callable_info("__init__", obj.__init__)
        if inspect.isfunction(descriptor):
            constructor["binding"] = "instancemethod"
    info["constructors"] = [constructor]
    new = inspect.getattr_static(obj, "__new__", None)
    if new is not None and new is not object.__new__:
        value = new.__func__ if isinstance(new, staticmethod) else new
        evidence = callable_info("__new__", value)
        evidence["binding"] = "staticmethod"
        info["allocation_constructor"] = evidence
    return info


def namespace(value: Any, name: str, classes: bool = True, only: list[str] | None = None,
              instances: bool = False) -> dict[str, Any]:
    """Capture every non-dunder name, reporting read failures explicitly.

    ``only`` restricts the walk to those names (chunked host captures).
    ``instances`` also records the class of each module-level object, e.g. FL.fl.
    """
    result: dict[str, Any] = {"name": name, "doc": clean_doc(value), "classes": [],
        "functions": [], "attributes": [], "errors": [], "names": []}
    names = _names(value, result["errors"]) if only is None else list(only)
    result["names"] = names
    for member in names:
        try:
            obj = getattr(value, member)
            if classes and inspect.isclass(obj):
                result["classes"].append(class_info(obj, member))
            elif inspect.isclass(obj):
                # Nested enum/type objects are types, not instance methods.
                result["attributes"].append({"name": member, "type": "type", "doc": clean_doc(obj)})
            elif callable(obj):
                descriptor = inspect.getattr_static(value, member, None) if inspect.isclass(value) else None
                if isinstance(descriptor, (staticmethod, classmethod)):
                    info = callable_info(member, descriptor.__func__)
                    info["binding"] = "staticmethod" if isinstance(descriptor, staticmethod) else "classmethod"
                else:
                    info = callable_info(member, obj)
                    if inspect.isfunction(descriptor):
                        info["binding"] = "instancemethod"
                result["functions"].append(info)
            else:
                result["attributes"].append({"name": member, "type": type(obj).__name__, "doc": clean_doc(obj) if inspect.isdatadescriptor(obj) else ""})
                kind = type(obj)
                if instances and classes and kind.__module__ != "builtins" and not inspect.ismodule(obj):
                    result.setdefault("instance_classes", []).append(class_info(kind, kind.__name__))
        except TimeoutError:
            # A host execution deadline is cancellation, not missing API data.
            # Swallowing a tracing timeout can disable the host's trace guard.
            raise
        except Exception as exc:
            result["errors"].append({"name": member, "error": type(exc).__name__})
            result["attributes"].append({"name": member, "type": "Any", "doc": "Native member could not be inspected."})
    return result


def finish_module(scope: dict[str, Any], exports: list[str] | None) -> dict[str, Any]:
    """Make instance classes ordinary classes and record `__all__` for star imports."""
    known = {c["name"] for c in scope["classes"]}
    for info in scope.pop("instance_classes", []):
        if info["name"] not in known:
            known.add(info["name"])
            scope["classes"].append(info)
    scope["classes"].sort(key=lambda c: c["name"])
    if exports is not None:
        scope["exports"] = sorted(exports)
    return scope


def _pythonqt_child(root: Any, child: str, errors: list[dict[str, str]]) -> Any:
    """Prefer root identity, then registered identity, then a qualified import."""
    qualified = f"PythonQt.{child}"
    try:
        value = getattr(root, child, None)
        if value is None:
            value = sys.modules.get(qualified)
        return importlib.import_module(qualified) if value is None else value
    except TimeoutError:
        raise
    except ModuleNotFoundError as exc:
        if exc.name != qualified:
            errors.append({"name": child, "error": type(exc).__name__})
    except Exception as exc:
        errors.append({"name": child, "error": type(exc).__name__})
    return None


def capture(targets: tuple[str, ...] | list[str] = TARGETS) -> dict[str, Any]:
    """Capture FontLab and every discovered PythonQt child, including objects."""
    result: dict[str, Any] = {"schema": 1, "modules": {}}
    for name in targets:
        obj = resolve(name)
        if obj is None:
            result["modules"][name] = {"available": False, "reason": "native module absent", "namespace": {}}
            if name == "PythonQt":
                result["modules"][name]["required_seeds"] = {"discovered": [], "missing": sorted(QT_SEEDS)}
            continue
        if name in FL_SHAPED:
            exports = getattr(obj, "__all__", None)
            scope = finish_module(namespace(obj, name, instances=True), None if exports is None else list(exports))
            item = {"available": True, "namespace": scope, "subpackages": {}}
        else:
            item = {"available": True, "namespace": namespace(obj, name), "subpackages": {}}
        if name == "PythonQt":
            # Snapshot keys: imports may change the process-wide module registry.
            registered = {key.split(".")[1] for key in tuple(sys.modules)
                          if isinstance(key, str) and key.startswith("PythonQt.") and key.split(".")[1]}
            failed = {error["name"] for error in item["namespace"]["errors"]}
            for child in sorted(set(QT_SEEDS) | set(item["namespace"]["names"]) | registered):
                if child in failed:
                    continue  # A failed native getter is evidence, not a retry request.
                value = _pythonqt_child(obj, child, item["namespace"]["errors"])
                if value is not None and not isinstance(value, (str, bytes, int, float, bool)):
                    item["subpackages"][child] = {"namespace": namespace(value, f"{name}.{child}"), "kind": type(value).__name__}
            item["required_seeds"] = {
                "discovered": sorted(set(QT_SEEDS) & item["subpackages"].keys()),
                "missing": sorted(set(QT_SEEDS) - item["subpackages"].keys()),
            }
        result["modules"][name] = item
    return result
