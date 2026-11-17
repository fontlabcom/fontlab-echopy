# this_file: tests/test_manual_class_docs.py
"""Check maintained class guidance against captured declarations before refresh."""

import ast
import textwrap
import json
import re
import shutil
from pathlib import Path

import pytest

from fontlab_echopy.tooling.merge import merge

ROOT = Path(__file__).parents[1]
TARGETS = (
    "fontlab.flAnchor",
    "fontlab.flGuideLine",
    "fontlab.flShape",
    "fontlab.FontMetrics",
    "fontlab.flZone",
    "fontlab.CurveEx",
    "fontlab.fgSymbol",
    "fontlab.flObject",
    "fontlab.flPinPoint",
    "fontgate.fgAnchor",
    "fontgate.fgLayer",
    "fontgate.fgShape",
    "fontgate.fgKerning",
    "fontgate.fgKerningGroups",
    "fontgate.fgKerningObject",
    "fontgate.fgKerningObjectPair",
    "fontlab.Interval",
    "fontlab.PaintBrush",
    "fontlab.flInstance",
    "fontlab.flStem",
    "fontlab.flTTHCommand",
    "fontlab.AccentInfo",
    "fontlab.GlyphComponent",
    "fontlab.flEvent",
    "fontlab.flLayerAttributes",
    "fontlab.SmartCornerParameters",
    "fontgate.fgGroup",
    "fontgate.fgMatrix",
    "fontgate.fgPen",
    "fontgate.fgStem",
    "fontgate.fgZone",
    "fontgate.fgAxes",
    "fontgate.fgCaret",
    "fontgate.fgDesignPosition",
    "fontgate.fgDeviceRecord",
    "fontgate.fgAnchors",
    "fontlab.flSnaps",
    "fontlab.PaintBrushShape",
    "fontlab.flMouseEvent",
    "fontlab.flModel",
    "fontlab.ExportControl",
    "fontgate.fgAxis",
    "fontgate.fgMaster",
    "fontgate.fgMasters",
    "fontgate.fgBitmaps",
    "fontgate.fgCMaps",
    "fontgate.fgCarets",
    "fontgate.fgContours",
    "fontgate.fgCuspPoints",
    "fontgate.fgDeviceRecords",
    "fontgate.fgGaspRecords",
    "fontgate.fgGlyphs",
    "fontgate.fgGlyphDict",
    "fontgate.fgGlyphIDsSet",
    "fontgate.fgGuide",
    "fontgate.fgComponent",
    "fontgate.fgBrush",
    "fontgate.fgCmapRecord",
    "fontgate.fgCoding",
    "fontgate.fgCuspPoint",
    "fontgate.fgGaspRecord",
    "fontgate.fgHintCommand",
    "fontgate.fgLib",
    "fontgate.fgMaxP",
    "fontgate.fgMetricsClass",
    "fontgate.fgOtValue",
    "fontgate.fgContour",
    "fontgate.fgFont",
    "fontgate.fgGlyph",
    "fontgate.fgPoint",
    "fontlab.flContour",
    "fontlab.flGlyph",
    "fontlab.flLayer",
    "fontlab.flNode",
    "fontlab.FaBasicPtr",
    "fontlab.FontLayer",
    "fontlab.LocationValue",
    "fontlab.flLocation",
    "fontlab.flHintingParameters",
    "fontlab.flAxis",
    "fontlab.flSticker",
    "fontlab.flTransform",
    "fontlab.flPaper",
    "fontlab.flProperty",
    "fontlab.TransformFrame",
    "fontlab.fgSymbolList",
    "fontlab.YPanelManager",
    "fontlab.flGraphicsInfo",
    "fontlab.flAuditInfo",
    "fontlab.flPropertyDouble",
    "fontlab.flPropertyPoint",
    "fontlab.flSearchInfo",
    "fontlab.flModelProducer",
    "fontlab.flBasicTool",
    "fontlab.flObjectsList_flGuideLine_",
    "fontlab.flObjectsList_flShape_",
    "fontlab.flShapeData",
    "fontlab.flAbstractEditor",
    "fontlab.flVisualItem",
    "fontlab.flAbstractVectorNode",
    "fontlab.flVectorNode",
    "fontlab.flTextBlock",
    "fontlab.flWorkspace",
    "fontlab.Info",
    "fontlab.YPanelWidget",
    "fontlab.flCanvas",
    "fontlab.flItems",
    "fontlab.flPackage",
    "fontlab.flPreferences",
    "fontlab.flExpression",
    "fontlab.flMarkerPoint",
    "fontlab.flShapeBuilder",
    "fontlab.flSnapLine",
    "fontlab.flSnapObject",
    "fontlab.flContourInfo",
    "fontlab.flLayerInfo",
    "fontlab.flNodeInfo",
    "fontlab.flShapeInfo",
    "fontlab.flGlyphInfo",
)


def backticked_names(doc):
    """Return the identifiers a guidance string puts in backticks, without call parens."""
    return re.findall(r"`(\w+)(?:\(\))?`", doc)


def names_outside_capture(doc, class_name, members):
    """Backticked names that are neither captured members nor the class's own name."""
    return set(backticked_names(doc)) - members - {class_name}


@pytest.fixture(scope="module")
def merged_docs(tmp_path_factory):
    output = tmp_path_factory.mktemp("manual-class-docs")
    merge(ROOT / "generated", output, [ROOT / "patches/manual.json"])
    return output


@pytest.mark.parametrize("target", TARGETS)
def test_manual_class_guidance_names_only_captured_members(target):
    module, name = target.split(".")
    patch = json.loads((ROOT / "patches/manual.json").read_text())[target]
    source = ROOT / "generated" / f"{module}.py"
    tree = ast.parse(source.read_text())
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == name)
    members = {
        n.target.id if isinstance(n, ast.AnnAssign) else n.name
        for n in cls.body
        if isinstance(n, (ast.AnnAssign, ast.FunctionDef))
    }
    assert backticked_names(patch["doc"]), (
        "Class guidance must identify useful captured members"
    )
    assert not names_outside_capture(patch["doc"], name, members)
    assert patch["source"] == f"generated/{module}.py: {name} captured declaration"


@pytest.mark.parametrize("target", TARGETS)
def test_manual_class_guidance_merges_without_changing_native_declarations(
    target, merged_docs
):
    module, name = target.split(".")
    patch = json.loads((ROOT / "patches/manual.json").read_text())[target]
    raw = ast.parse((ROOT / "generated" / f"{module}.py").read_text())
    merged = ast.parse((merged_docs / f"{module}.pyi").read_text())
    original = next(n for n in raw.body if isinstance(n, ast.ClassDef) and n.name == name)
    enriched = next(n for n in merged.body if isinstance(n, ast.ClassDef) and n.name == name)
    doc = ast.get_docstring(enriched)
    assert ast.get_docstring(original) in doc
    assert patch["doc"] in doc
    assert "Source: " + patch["source"] in doc
    extensions = patch.get("extensions", [])
    assert len(enriched.body) == len(original.body) + len(extensions)
    prefix = enriched.body[: len(original.body)]
    tail = enriched.body[len(original.body) :]
    declared = [ast.parse(textwrap.dedent(src)).body[0] for src in extensions]

    def shape(node):
        return (
            type(node).__name__,
            node.name,
            ast.dump(node.args),
            ast.dump(node.returns),
            ast.get_docstring(node),
            ast.dump(node.decorator_list[0]) if node.decorator_list else None,
        )

    assert [shape(n) for n in tail] == [shape(n) for n in declared], (
        "Appended members must be exactly the declared extensions"
    )
    assert [getattr(n, "name", None) for n in prefix] == [
        getattr(n, "name", None) for n in original.body
    ]
    for before, after in zip(original.body, enriched.body):
        if isinstance(before, ast.FunctionDef):
            assert ast.dump(before.args) == ast.dump(after.args)
            assert ast.dump(before.returns) == ast.dump(after.returns)
            assert [ast.dump(d) for d in before.decorator_list] == [
                ast.dump(d) for d in after.decorator_list
            ]
        elif isinstance(before, ast.AnnAssign):
            assert ast.dump(before) == ast.dump(after)


def captured_type_text(module, name, member):
    """Return the captured type words for a member: its return annotation and docstring,
    or the string literal that follows an annotated attribute."""
    tree = ast.parse((ROOT / "generated" / f"{module}.py").read_text())
    cls = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == name)
    for index, node in enumerate(cls.body):
        if isinstance(node, ast.AnnAssign) and node.target.id == member:
            following = cls.body[index + 1] if index + 1 < len(cls.body) else None
            if isinstance(following, ast.Expr) and isinstance(following.value, ast.Constant):
                return str(following.value.value)
            return ""
        if isinstance(node, ast.FunctionDef) and node.name == member:
            returns = ast.unparse(node.returns) if node.returns else ""
            return returns + " " + (ast.get_docstring(node) or "")
    raise AssertionError(f"{name}.{member} is not captured")


TYPE_TOKENS = (
    ("fontlab.flAnchor", "anchorPoint", "QPointF"),
    ("fontlab.flAnchor", "fixHorzDirection", "bool"),
    ("fontlab.flGuideLine", "centerPoint", "QPointF"),
    ("fontlab.flGuideLine", "vectorPoint", "QPointF"),
    ("fontlab.flGuideLine", "linef", "QLineF"),
    ("fontlab.flShape", "boundingBox", "QRectF"),
    ("fontlab.flShape", "getContours", "flContour"),
    ("fontgate.fgLayer", "addContour", "fgContour"),
    ("fontgate.fgShape", "addContour", "fgContour"),
    ("fontgate.fgGlyphIDsSet", "contains", "bool"),
)


@pytest.mark.parametrize(("target", "member", "token"), TYPE_TOKENS)
def test_manual_class_guidance_type_words_match_captured_declaration(
    target, member, token
):
    module, name = target.split(".")
    patch = json.loads((ROOT / "patches/manual.json").read_text())[target]
    assert token in captured_type_text(module, name, member), "capture lost the type"
    assert token in patch["doc"], "overlay must name the captured type"


# Ratchet: classes whose merged docstring carries maintained guidance, and the
# classes that still hold only the generated stub. Raise MAINTAINED when guidance
# is added; the totals must not move unless the captured declarations change.
MAINTAINED = {"fontlab": 73, "fontgate": 46}
TOTAL = {"fontlab": 73, "fontgate": 121}
MAINTAINED_MARK = "Supplemental documentation:"


@pytest.mark.parametrize("module", sorted(MAINTAINED))
def test_class_docstrings_when_merged_then_maintained_count_never_drops(
    module, merged_docs
):
    tree = ast.parse((merged_docs / f"{module}.pyi").read_text())
    docs = [
        ast.get_docstring(n) or ""
        for n in tree.body
        if isinstance(n, ast.ClassDef)
    ]
    maintained = sum(MAINTAINED_MARK in d for d in docs)
    assert len(docs) == TOTAL[module], "captured class count changed; update TOTAL"
    assert maintained >= MAINTAINED[module], (
        f"{module}: maintained class docstrings dropped to {maintained}"
    )
    assert maintained == MAINTAINED[module], (
        f"{module}: {maintained} maintained; raise MAINTAINED to lock the gain"
    )


def test_shipped_provenance_when_compared_to_shipped_files_then_hashes_and_count_agree(
    tmp_path,
):
    """The shipped stubs must equal a fresh merge, and provenance must describe them."""
    import hashlib

    package = ROOT / "src/fontlab_echopy"
    provenance = json.loads((package / "_provenance.json").read_text())
    overlays = [
        ROOT / "enrichment/qt5.json",
        ROOT / "enrichment/fontlab-proteus.json",
        ROOT / "enrichment/fontpr-mcp.json",
        ROOT / "patches/manual.json",
    ]
    fresh = merge(ROOT / "generated", tmp_path, overlays)
    for relative, digest in provenance["merged_outputs"].items():
        shipped = hashlib.sha256((package / relative).read_bytes()).hexdigest()
        assert shipped == digest, f"{relative}: provenance hash is stale"
    assert provenance["overlays"] == [
        {"file": o.name, "sha256": hashlib.sha256(o.read_bytes()).hexdigest()}
        for o in overlays
    ]
    assert provenance["merge"]["applied"] == fresh["applied"]


def test_names_outside_capture_when_class_name_backticked_then_allowed():
    members = {"glyph", "compare"}
    assert names_outside_capture("`fgSymbol()` offers `glyph`.", "fgSymbol", members) == set()
    assert names_outside_capture("The `fgSymbol` class.", "fgSymbol", members) == set()


def test_names_outside_capture_when_other_name_backticked_then_rejected():
    members = {"glyph", "compare"}
    assert names_outside_capture("`fgSymbol()` offers `invented`.", "fgSymbol", members) == {"invented"}
    assert names_outside_capture("See `otherClass`.", "fgSymbol", members) == {"otherClass"}
    assert names_outside_capture("`fgSymbolList`", "fgSymbol", members) == {"fgSymbolList"}


def test_class_guidance_requires_at_least_one_backticked_member():
    assert backticked_names("No identifiers here.") == []


def test_merge_when_raw_lacks_capture_identity_then_identity_and_identities_kept(tmp_path):
    """Re-merging the committed raw tree keeps the recorded capture and its identities."""
    raw = tmp_path / "raw"
    shutil.copytree(ROOT / "generated", raw)
    coverage = json.loads((raw / "coverage.json").read_text())
    coverage.pop("capture_identity", None)
    (raw / "coverage.json").write_text(json.dumps(coverage) + "\n")
    out = tmp_path / "out"
    merge(raw, out, [ROOT / "patches/manual.json"])
    provenance_path = out / "_provenance.json"
    provenance = json.loads(provenance_path.read_text())
    provenance["capture_identity"] = {"sha256": "old"}
    provenance_path.write_text(json.dumps(provenance) + "\n")
    registry = json.loads((ROOT / "src/fontlab_echopy/_identities.json").read_text())[
        "maintained_extensions"
    ]
    kept = {"kept": True, "maintained_extensions": registry}
    (out / "_identities.json").write_text(json.dumps(kept) + "\n")
    merge(raw, out, [ROOT / "patches/manual.json"])
    assert json.loads(provenance_path.read_text())["capture_identity"] == {"sha256": "old"}
    assert json.loads((out / "_identities.json").read_text()) == kept


def test_merge_when_unmatched_changes_then_identities_removed(tmp_path):
    out = tmp_path / "out"
    merge(ROOT / "generated", out, [ROOT / "patches/manual.json"])
    (out / "_identities.json").write_text("{}\n")
    extra = tmp_path / "extra.json"
    extra.write_text(json.dumps({"fontlab.NoSuchThing": {"doc": "x"}}))
    result = merge(ROOT / "generated", out, [ROOT / "patches/manual.json", extra])
    assert result["unmatched"] == ["fontlab.NoSuchThing"]
    assert not (out / "_identities.json").exists(), "identities embed merge.unmatched"


def test_merge_when_raw_carries_new_capture_identity_then_identities_removed(tmp_path):
    raw = tmp_path / "raw"
    shutil.copytree(ROOT / "generated", raw)
    out = tmp_path / "out"
    merge(raw, out, [ROOT / "patches/manual.json"])
    (out / "_identities.json").write_text("{}\n")
    coverage = json.loads((raw / "coverage.json").read_text())
    coverage["capture_identity"] = {"sha256": "new"}
    (raw / "coverage.json").write_text(json.dumps(coverage))
    merge(raw, out, [ROOT / "patches/manual.json"])
    assert not (out / "_identities.json").exists()


def test_merge_when_raw_carries_capture_identity_then_provenance_records_it(tmp_path):
    raw = tmp_path / "raw"
    shutil.copytree(ROOT / "generated", raw)
    coverage = json.loads((raw / "coverage.json").read_text())
    coverage["capture_identity"] = {"sha256": "owned"}
    (raw / "coverage.json").write_text(json.dumps(coverage))
    out = tmp_path / "out"
    merge(raw, out, [ROOT / "patches/manual.json"])
    provenance = json.loads((out / "_provenance.json").read_text())
    assert provenance["capture_identity"] == {"sha256": "owned"}


def test_batch_11_guidance_when_member_invented_then_rejected():
    """Mutant: a batch 11 doc naming a member the capture lacks must be flagged."""
    patch = json.loads((ROOT / "patches/manual.json").read_text())["fontgate.fgGlyphIDsSet"]
    members = {"asList", "clean", "contains", "del_"}
    assert names_outside_capture(patch["doc"], "fgGlyphIDsSet", members) == set()
    mutant = patch["doc"].replace("`contains`", "`containsAll`")
    assert names_outside_capture(mutant, "fgGlyphIDsSet", members) == {"containsAll"}
