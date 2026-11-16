# this_file: src/fontlab_echopy/tooling/enrich.py
"""Fetch verified PySide2 stubs and official Qt 5 docs; intersect native names.

Downloads stay in the caller's cache, outside installable packages. PySide2 is
never imported or installed into FontLab. Reference signatures are labeled as
upstream evidence rather than asserted as PythonQt calling conventions.
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin
from urllib.request import Request, urlopen

from .generate import scopes, source_name

PYPI = "https://pypi.org/pypi/PySide2/json"
QT_DOCS = "https://doc.qt.io/archives/qt-5.15/"


def download(url: str, path: Path, sha256: str | None = None) -> str:
    """Cache an upstream resource; validate wheel digest before parsing content."""
    path = Path(path)
    if not path.exists():
        request = Request(
            url,
            headers={"User-Agent": "fontlab-echopy/0.1 (API documentation enrichment)"},
        )
        with urlopen(request, timeout=30) as response:
            content = response.read()
        actual = hashlib.sha256(content).hexdigest()
        if sha256 and actual != sha256:
            raise ValueError("Upstream SHA256 mismatch")
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + ".part")
        temporary.write_bytes(content)
        temporary.replace(path)
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if sha256 and actual != sha256:
        raise ValueError("Cached upstream SHA256 mismatch")
    return actual


def fetch_pyside(cache: Path) -> tuple[Path, dict[str, Any]]:
    """Resolve latest PyPI metadata and choose a wheel solely for .pyi extraction."""
    cache = Path(cache)
    with urlopen(PYPI, timeout=30) as response:
        metadata = json.load(response)
    wheels = [item for item in metadata["urls"] if item["packagetype"] == "bdist_wheel"]
    if not wheels:
        raise ValueError("PySide2 release contains no wheel")
    # Linux wheel stubs are architecture independent; smaller macOS wheels are
    # preferred because no compiled library will be loaded.
    item = min(
        wheels, key=lambda item: ("macosx" not in item["filename"], item["size"])
    )
    path = cache / item["filename"]
    digest = download(item["url"], path, item["digests"]["sha256"])
    manifest = {
        "project": "PySide2",
        "version": metadata["info"]["version"],
        "metadata_url": PYPI,
        "wheel": item["filename"],
        "url": item["url"],
        "sha256": digest,
    }
    (cache / "pyside-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return path, manifest


def parse_stubs(wheel: Path) -> dict[str, Any]:
    """Extract every PySide2 class and overloaded member signature from a wheel."""
    result = {}
    with zipfile.ZipFile(wheel) as archive:
        for filename in sorted(archive.namelist()):
            if not filename.startswith("PySide2/") or not filename.endswith(".pyi"):
                continue
            tree = ast.parse(archive.read(filename).decode())
            for cls in tree.body:
                if not isinstance(cls, ast.ClassDef):
                    continue
                info = {"module": Path(filename).stem, "members": {}, "types": {}}
                for member in cls.body:
                    if isinstance(member, ast.FunctionDef):
                        definition = ast.unparse(member).splitlines()
                        line = next(
                            line for line in definition if line.startswith("def ")
                        )
                        info["members"].setdefault(member.name, []).append(
                            line.removeprefix("def ").removesuffix(":")
                        )
                        types = {
                            arg.arg: ast.unparse(arg.annotation)
                            for arg in member.args.args
                            if arg.annotation
                        }
                        types["return"] = (
                            ast.unparse(member.returns) if member.returns else "Any"
                        )
                        info["types"].setdefault(member.name, []).append(types)
                result.setdefault(cls.name, info)
    return result


def parse_qt(html: str, *, source_url: str = QT_DOCS) -> dict[str, Any]:
    """Read class description and every documented method/property section."""
    from bs4 import BeautifulSoup
    from markdownify import markdownify

    # Upstream illustrative user/temporary paths are normalized in redistributed
    # docs. Original, hash-verified HTML remains unchanged in the local cache.
    html = html.replace("/Users/", "/example-users/").replace("/tmp/", "/temporary/")
    soup = BeautifulSoup(html, "html.parser")
    for link in soup.select("[href]"):
        link["href"] = urljoin(source_url, link["href"])
    for image in soup.select("img[src]"):
        image["src"] = urljoin(source_url, image["src"])

    def markdown(element: Any) -> str:
        return markdownify(
            str(element),
            heading_style="ATX",
            bullets="-",
            wrap=True,
            wrap_width=88,
            table_infer_header=True,
            escape_misc=True,
        ).strip()

    description = soup.select_one(".descr")
    result: dict[str, Any] = {
        "doc": markdown(description) if description else "",
        "members": {},
    }
    for heading in soup.select("h3.fn"):
        member = heading.get("id", "").removesuffix("-prop")
        member = re.sub(r"-\d+$", "", member)
        if not member:
            continue
        content = [markdown(heading)]
        for sibling in heading.next_siblings:
            if getattr(sibling, "name", None) in {"h2", "h3"}:
                break
            if getattr(sibling, "name", None):
                content.append(markdown(sibling))
        result["members"][member] = (
            result["members"].get(member, "") + "\n\n" + "\n\n".join(content)
        ).strip()
    return result


def enrich(
    data: dict[str, Any], cache: Path, output: Path, max_classes: int = 0
) -> dict[str, Any]:
    """Enrich all intersecting classes by default; report every gap explicitly."""
    cache, output = Path(cache), Path(output)
    wheel, manifest = fetch_pyside(cache)
    stubs = parse_stubs(wheel)
    native = [
        (module, cls)
        for module, scope, _, _ in scopes(data)
        if module.startswith("PythonQt.")
        for cls in scope.get("classes", [])
    ]
    matched = sorted({cls["name"] for _, cls in native if cls["name"] in stubs})
    candidates = sorted(
        {
            cls["name"]
            for _, cls in native
            if cls["name"] in stubs or cls["name"].startswith("Q")
        }
    )
    requested = candidates[:max_classes] if max_classes else candidates
    documents, failures, revisions = {}, {}, {}

    def fetch_class(name: str):
        filename = name.lower().replace("::", "-") + ".html"
        url = QT_DOCS + filename
        path = cache / "qt5" / filename
        try:
            digest = download(url, path)
            return (
                name,
                parse_qt(path.read_text(), source_url=url),
                {"url": url, "sha256": digest},
                None,
            )
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            return name, None, None, str(exc)

    with ThreadPoolExecutor(max_workers=8) as pool:
        for name, doc, revision, error in pool.map(fetch_class, requested):
            if error:
                failures[name] = error
            else:
                documents[name], revisions[name] = doc, revision
    patches = {}
    counts = {
        "native_class_occurrences": len(native),
        "native_unique_classes": len({cls["name"] for _, cls in native}),
        "stub_classes": len(stubs),
        "matched_unique_classes": len(matched),
        "qt_docs_fetched": len(documents),
        "enriched_member_occurrences": 0,
    }
    for module, cls in native:
        name = cls["name"]
        if name not in stubs and name not in documents:
            continue
        doc = documents.get(name, {})
        target = module + "." + source_name(name)
        source = QT_DOCS + name.lower().replace("::", "-") + ".html"
        if doc.get("doc"):
            patches[target] = {
                "doc": "Qt 5 reference:\n\n" + doc["doc"],
                "source": source,
            }
        for member in cls.get("methods", []) + cls.get("attributes", []):
            key = member["name"]
            signatures = stubs.get(name, {}).get("members", {}).get(key, [])
            member_doc = doc.get("members", {}).get(key)
            if signatures or member_doc:
                patch = {"signatures": signatures, "source": source + "#" + key}
                # Only unanimous primitive types are binding-independent enough
                # to strengthen a native declaration automatically.
                types = stubs.get(name, {}).get("types", {}).get(key, [])
                if types:
                    common = {
                        arg: typ
                        for arg, typ in types[0].items()
                        if typ in {"int", "str", "bool", "float", "bytes", "None"}
                        and all(other.get(arg) == typ for other in types)
                    }
                    if "return" in common:
                        patch["returns"] = common.pop("return")
                    patch["parameter_types"] = common
                if member_doc:
                    patch["doc"] = "Qt 5 reference:\n\n" + member_doc
                patches[target + "." + source_name(key)] = patch
                counts["enriched_member_occurrences"] += 1
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(patches, indent=2, sort_keys=True) + "\n")
    report = {
        "upstream": manifest,
        "coverage": counts,
        "unmatched_native_classes": sorted(
            {cls["name"] for _, cls in native} - stubs.keys()
        ),
        "qt_document_failures": failures,
        "not_requested": sorted(set(candidates) - set(requested)),
        "documents": revisions,
    }
    (cache / "enrichment-report.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n"
    )
    return report
