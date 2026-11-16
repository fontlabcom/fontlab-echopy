# this_file: tests/test_method_bindings.py
"""Known descriptors retain their binding through capture and declaration merge."""
import inspect
import types
import pytest
from fontlab_echopy.tooling.capture import namespace
from fontlab_echopy.tooling.generate import generate
from fontlab_echopy.tooling.merge import merge


class Parent:
    @staticmethod
    def static(value=3, /, *, label="a,b"):
        raise AssertionError("Capture must not call methods")

    @classmethod
    def factory(owner, value=3, /, *, label="a,b"):
        raise AssertionError("Capture must not call methods")

    def ordinary(self, value=3):
        raise AssertionError("Capture must not call methods")


class Child(Parent):
    pass


@pytest.mark.parametrize("cls", [Parent, Child])
@pytest.mark.parametrize("stage", ["generated", "merged"])
def test_descriptors_preserve_binding_defaults_and_inheritance(cls, stage, tmp_path):
    native = types.SimpleNamespace(Widget=cls)
    captured = namespace(native, "absent_method_fixture")
    methods = {item["name"]: item for item in captured["classes"][0]["methods"]}
    assert methods["static"].get("binding") == "staticmethod"
    assert methods["factory"].get("binding") == "classmethod"
    assert methods["ordinary"].get("binding") == "instancemethod"
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    generate({"modules": {"absent_method_fixture": {"namespace": captured}}}, raw)
    merge(raw, merged, [])
    path = raw / "absent_method_fixture.py" if stage == "generated" else merged / "absent_method_fixture.pyi"
    values = {"__name__": "owned_method_fixture"}
    exec(compile(path.read_text(), str(path), "exec"), values)
    generated = values["Widget"]
    assert isinstance(inspect.getattr_static(generated, "static"), staticmethod)
    assert isinstance(inspect.getattr_static(generated, "factory"), classmethod)
    for name in ("static", "factory", "ordinary"):
        expected, actual = inspect.signature(getattr(cls, name)), inspect.signature(getattr(generated, name))
        assert [(p.name, p.kind, p.default) for p in actual.parameters.values()] == [(p.name, p.kind, p.default) for p in expected.parameters.values()], name
    for original, emitted in ((cls, generated), (object.__new__(cls), object.__new__(generated))):
        for name in ("static", "factory", "ordinary"):
            expected = inspect.signature(getattr(original, name))
            actual = inspect.signature(getattr(emitted, name))
            assert [(p.name, p.kind, p.default) for p in actual.parameters.values()] == [(p.name, p.kind, p.default) for p in expected.parameters.values()], name
    assert methods["factory"]["signature"].startswith("(owner,"), "Capture the unbound receiver"


def test_unclassified_descriptor_keeps_legacy_instance_method_fallback():
    from fontlab_echopy.tooling.generate import module_source

    class Descriptor:
        def __get__(self, instance, owner):
            return lambda value=3: None

    class Widget:
        unknown = Descriptor()

    captured = namespace(types.SimpleNamespace(Widget=Widget), "absent_method_fixture")
    record = captured["classes"][0]["methods"][0]
    assert record["name"] == "unknown" and "binding" not in record
    values = {"__name__": "owned_unknown_fixture"}
    exec(module_source("absent_method_fixture", captured, True), values)
    assert list(inspect.signature(values["Widget"].unknown).parameters) == ["self", "value"]


class ReceiverParent:
    def __init__(receiver, payload=3, /, *, label="a,b"):
        raise AssertionError("Capture must not construct objects")

    def ordinary(receiver, value=5, /, *, label="a,b"):
        raise AssertionError("Capture must not call methods")


class ReceiverChild(ReceiverParent):
    pass


@pytest.mark.parametrize("cls", [ReceiverParent, ReceiverChild])
@pytest.mark.parametrize("stage", ["generated", "merged"])
@pytest.mark.parametrize("member", ["ordinary", "__init__"])
def test_known_instance_receiver_is_not_duplicated(cls, stage, member, tmp_path):
    captured = namespace(types.SimpleNamespace(Widget=cls), "absent_receiver_fixture")
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    generate({"modules": {"absent_receiver_fixture": {"namespace": captured}}}, raw)
    merge(raw, merged, [])
    path = raw / "absent_receiver_fixture.py" if stage == "generated" else merged / "absent_receiver_fixture.pyi"
    values = {"__name__": "owned_receiver_fixture"}
    exec(compile(path.read_text(), str(path), "exec"), values)
    emitted = values["Widget"]
    for original, generated in ((cls, emitted), (object.__new__(cls), object.__new__(emitted))):
        expected = inspect.signature(getattr(original, member))
        actual = inspect.signature(getattr(generated, member))
        assert [(p.name, p.kind, p.default) for p in actual.parameters.values()] == [
            (p.name, p.kind, p.default) for p in expected.parameters.values()
        ], "Known function receivers must not depend on their spelling"
    record = captured["classes"][0]
    item = record["constructors"][0] if member == "__init__" else next(
        method for method in record["methods"] if method["name"] == member
    )
    assert item["binding"] == "instancemethod"


class StaticConstructor:
    @staticmethod
    def __init__(value=3, /, *, label="a,b"):
        """Owned static constructor documentation."""
        raise AssertionError("Capture must not invoke constructors")


class ClassConstructor:
    @classmethod
    def __init__(owner, value=3, /, *, label="a,b"):
        """Owned class constructor documentation."""
        raise AssertionError("Capture must not invoke constructors")


class StaticConstructorChild(StaticConstructor):
    pass


class ClassConstructorChild(ClassConstructor):
    pass


@pytest.mark.parametrize("cls,kind", [
    (StaticConstructor, staticmethod), (StaticConstructorChild, staticmethod),
    (ClassConstructor, classmethod), (ClassConstructorChild, classmethod),
])
@pytest.mark.parametrize("stage", ["generated", "merged"])
def test_constructor_descriptor_preserves_binding(cls, kind, stage, tmp_path):
    captured = namespace(types.SimpleNamespace(Widget=cls), "absent_constructor_binding_fixture")
    record = captured["classes"][0]["constructors"][0]
    original_descriptor = inspect.getattr_static(cls, "__init__")
    assert record.get("binding") == kind.__name__, "Constructor binding must be captured before bound access"
    assert record["signature"] == str(inspect.signature(original_descriptor.__func__))
    assert record["doc"] == original_descriptor.__func__.__doc__
    if kind is classmethod:
        assert record["signature"].startswith("(owner,"), "Keep the unbound class receiver"
    raw, merged = tmp_path / "raw", tmp_path / "merged"
    generate({"modules": {"absent_constructor_binding_fixture": {"namespace": captured}}}, raw)
    merge(raw, merged, [])
    path = raw / "absent_constructor_binding_fixture.py" if stage == "generated" else merged / "absent_constructor_binding_fixture.pyi"
    values = {"__name__": "owned_constructor_binding_fixture"}
    exec(compile(path.read_text(), str(path), "exec"), values)
    emitted = values["Widget"]
    descriptor = inspect.getattr_static(emitted, "__init__")
    assert isinstance(descriptor, kind), "Generation and merge must preserve the descriptor"
    assert descriptor.__func__.__doc__ == original_descriptor.__func__.__doc__
    assert str(inspect.signature(descriptor.__func__).return_annotation) == "None"
    for original, generated in ((cls, emitted), (object.__new__(cls), object.__new__(emitted))):
        expected = inspect.signature(original.__init__)
        actual = inspect.signature(generated.__init__)
        assert [(p.name, p.kind, p.default) for p in actual.parameters.values()] == [
            (p.name, p.kind, p.default) for p in expected.parameters.values()
        ], "Preserve class/instance access, positional-only arguments and keyword defaults"
