---
this_file: src_docs/md/development-and-limits.md
---

# Development and limits

## Regeneration

The inputs and outputs are independent:

- `generated/`: raw source generated from native metadata.
- `patches/manual.json`: maintained docs, typing, and explicit extensions.
- `enrichment/qt5.json`: fetched and parsed upstream documentation/signatures.
- `src/fontlab_echopy/`: merged, installable output and supporting runtime/tools.
- `reports/`: native coverage and upstream URLs, hashes and coverage gaps.
- `legacy/`: verbatim migration archive, including generators, overlays and RST
  documentation. It is excluded from wheels and source distributions.

Discovery unions advertised names with direct namespace dictionary keys, retaining
public API names hidden by a custom `__dir__`. PythonQt child discovery also
uses a snapshot of loaded module names and qualified imports for children absent
from root attributes. Root objects take precedence over registry/import objects;
nested registry paths identify their immediate child. Ordinary discovery failures
remain explicit in capture and generation reports; an absent optional child is
distinguished from a missing dependency. Failed root getters are not retried,
and execution deadlines/interrupts propagate. This tooling repair does not
refresh the retained captures or establish native completeness. Existing native
capture and publication holds remain applicable.

First run `examples/capture_in_fontlab.py` inside FontLab. It writes an API-only
capture to your user cache, with no member limits and no method calls. Captures
are local inputs, not distribution contents. Then, from this checkout:

```sh
fontlab-echopy generate ~/.cache/fontlab-echopy/native.json generated
fontlab-echopy enrich ~/.cache/fontlab-echopy/native.json enrichment/qt5.json \
  --cache .cache/upstream
fontlab-echopy merge generated src/fontlab_echopy \
  --overlay enrichment/qt5.json --overlay patches/manual.json
```

The repeatable one-command equivalent captures inside FontLab if `--capture`
is omitted. Outside FontLab, supply a previously captured file:

```sh
fontlab-echopy pipeline --capture ~/.cache/fontlab-echopy/native.json \
  --raw generated --output src/fontlab_echopy --qt-cache .cache/upstream \
  --qt-overlay enrichment/qt5.json --overlay patches/manual.json --reports reports
```

The pipeline also writes `_identities.json` into the merged package: every
captured scope, name, class member and constructor, the capture hash, the
native spelling of each sanitized identity (`QPainter::PixmapFragment` →
`QPainter__PixmapFragment`, `QWidget.raise` → `QWidget.raise_`), maintained
extensions, unmatched overlay targets and enrichment gaps. Documentation builds
reconcile their coverage against it without the raw capture. To refresh or
check it against a capture without regenerating sidecars:

```sh
fontlab-echopy identities path/to/native.json src/fontlab_echopy
fontlab-echopy verify-identities path/to/native.json src/fontlab_echopy
```

Both refuse a capture other than the generation input recorded in
`_provenance.json`, and fail when two native names map to one source name.

The pipeline never edits overlays. Regenerating raw output also leaves merged
output untouched until merge. Manual overlays take precedence over upstream
material. Unmatched overlay targets are reported instead of silently counted.
The CLI accepts older `pseudopackages_api_docs.json` captures as well.
Host execution deadlines propagate as errors. Large captures should run from
FontLab’s scripting surface; MCP users must split introspection into bounded
namespace calls to respect its fixed execution deadline.

Qt enrichment queries official PyPI for the latest PySide2 release, downloads
one wheel for architecture-independent `.pyi` extraction, checks its SHA256,
then fetches official Qt 5 class/member documentation. It intersects native
names and includes QtWidgets definitions under PythonQt.QtGui where present.
Downloads stay in the supplied cache. All matching classes are processed by
default; `enrich --max-classes N` is only for limited experiments, recorded in
the coverage report. PySide6 needs separate Qt6 mappings and native Qt-version
checks; changing the package name alone would not be a valid transition.

## Verification and building

```sh
./test.sh
uv build
# Inside FontLab against the installed wheel:
# execute examples/native_smoke.py
```

Versioning uses Git tags through hatch-vcs. `WORK.md` records local checks;
`CHANGELOG.md` records delivered behavior. `MIGRATION.json` retains source
revision/file hashes, including uncommitted source, and accounts for excluded
build/cache artifacts. Source originals have not been removed.

Griffe (also used by mkdocstrings) resolves the canonical source and stub pairs:

```python
import griffe
api = griffe.load("fontlab_echopy", allow_inspection=False, prefer_stubs_docs=True)
print(api.get_member("PythonQt.QtGui.QWidget.resize").docstring.value)
```

Source-only consumers that ignore `.pyi` files see the runtime facade; configure
stub support as above to retain the complete enriched documentation.

## Status

Issue 101 migration is complete and released as verified v0.2.0 (RELEASE.md):
source and licence provenance, capture of every native namespace and PythonQt child,
the capture/generate/enrich/merge pipeline, native-identity facades with `.pyi`
sidecars, PySide2/Qt 5 enrichment with coverage reports, deterministic
regeneration, and installed-wheel checks in FontLab.

v0.2.1 to v0.2.3 added generator-v3 static shims for Glyphs, Cocoa/vanilla, Aidus
and Fontlabapp; issue 201 removed them again (see Scope). They also added
structured Qt Markdown and separate overload source lines in
enrichment; `docnames` aliases that let mkdocstrings render the native
`fontlab`/`fontgate`/`fontpr`/`PythonQt` identities; and the BoolResult
class/namespace collision handling, each proven by strict source-only rendering.
`fontlabpr` is absent in FontLab 9.0.9780; capture records that absence.

## Archive preservation in this delivery

This remote branch retains `legacy/README.md`, `legacy/source.tar.gz` and
`licenses/aidus-legacy-LICENSE` byte-for-byte. A later canonical cleanup does
not delete them here. The source/runtime/tooling matches that canonical checkpoint.
No generation, native capture, package release or archive removal is part of this variant.

## Qualification boundary

The maintained acd615697 source and ordinary artifact milestone passed 437 tests. Dated README status below remains historical evidence. Native FontLab execution, current-provider capture and owner installation are separate; this site build performs none of those operations. Source capture, enrichment and generation commands above describe maintenance responsibilities, not actions performed by this build. Private Pages configuration and publication remain owner-held.
