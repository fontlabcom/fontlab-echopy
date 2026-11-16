---
this_file: README.md
---

## Install in FontLab

To install into FontLab 9, open `install.vfpy` from a checkout in FontLab
(double-click it or drop it onto FontLab), then restart FontLab. The file is a
short stub that hands the work to
[fontlab-instamix](https://github.com/fontlabcom/fontlab-python-instamix); if
instamix is not installed yet, the stub installs it from PyPI first. Instamix
installs the package into FontLab's own `site-packages` and records the install
under the extension id `com.fontlab.echopy`.

## Development status — 2026-11-05

Remote source inspected for this variant: `48e39a8a5758783980400d99d576ec77dced7b0e`. This is a dated source observation, not an installed or native acceptance claim.

Reconcile the Issue 207 enriched candidate and its five catalogues with current producers before a reviewed regeneration.

Qualify exact captures, aliases, docstrings, identities/provenance and ordinary installed consumers; document absent native APIs without inventing support.

## Repository and development

`src/` contains runtime routing and tooling; `generated/` contains raw declarations. `patches/`, `enrichment/` and `reports/` hold maintained overlays, inputs and reports. `tests/` checks source contracts.

Run `uv sync --extra test --extra enrich`, then `./test.sh`. The wrapper runs `uv run --extra test python -m pytest -q`. Build artifacts with `uv build`; capture requires a separate owned-host session.

The default source suite includes a fast real-sdist input payload check using the shared build fixture. From a checkout, packaging changes and releases additionally require `uv run --extra test python -m pytest -q tests_artifacts/test_sdist.py`; this separate gate builds an sdist and runs every shipped source test from its extracted inputs. Run both commands. The full artifact gate stays outside default test discovery to keep routine source tests quick.

Keep runtime, ordinary installed artifacts, native workflows and published documentation as separate acceptance results. Track open checks in [TODO.md](TODO.md), the implementation route in [PLAN.md](PLAN.md), and dated evidence in [CHANGELOG.md](CHANGELOG.md).

## Documentation source and build

The product guide starts at [src_docs/md/index.md](src_docs/md/index.md). Build with the separate hash-locked docs environment and `sh src_docs/build.sh`; run `python -m unittest discover -s tests_docs -v`. Every main commit qualifies source/output identity and byte parity. Private Pages configuration and publication remain owner-held.

# FontLab Echopy

Use FontLab's native Python API with source-readable definitions, annotations,
and enriched documentation. `fontlab_echopy` and `echopy` share the same modules.

```python
from echopy import fontlab as fl, fontgate as fg, fontpr
node = fl.flNode(12, 34)  # Inside FontLab: the original native flNode.
```

Install the wheel into a Python directory on FontLab's interpreter path. Python
3.11 or newer is required. No PySide2 runtime is installed into FontLab.

```sh
uv pip install dist/fontlab_echopy-*.whl
# From this checkout, including generation/enrichment dependencies:
uv sync --extra test --extra enrich
```

Generation checks native-to-Python name mappings before writing output. If two
spellings would become the same declaration, it raises a collision error naming
the owner and spellings; it does not replace an existing output tree with partial
results. The preflight also refuses top-level names mapping to `Any`, `globals`, `_bind`,
`_unavailable`, `_echopy_native`, `_echopy_name`, `_echopy_aliases` or
`_echopy_unavailable`, which are
used by generated facades. It covers these conflicts, not every possible write
failure or every reserved-name interaction.

Generated static/class method decorators use a private `builtins` alias selected
to avoid captured module and class-member names, including normalized spellings.
Captured names such as `staticmethod` and `classmethod` remain exposed. This
protects the generated declarations without adding those names to the refusal
list; merged runtime facades remain lazy. Native capture/refresh is a separate gate.

## Runtime contract

Classes, constructors, functions, constants, and results delegate to native
objects. `fl.flNode is fontlab.flNode` and native `isinstance`/argument conversion
keep working. Module attributes remain live; assigning an attribute delegates
back to the native namespace. Deleting a native attribute also removes it from
facade lookup and `dir()`; cached declarations do not restore a deleted value.
Accepted native names beginning `_echopy_` and their sanitized aliases share
current native reads, writes and deletion. The three exact internal state names
`_echopy_native`, `_echopy_name` and `_echopy_aliases` remain local; child facade
installation remains import bookkeeping.
Canonical `.pyi` sidecars contain complete readable
class/member declarations, signatures and documentation. Small `.py` facades
bind native symbols without compiling the large documentation source, keeping
imports within the host execution deadline. The native classes remain
the runtime authority: their `__doc__` and `inspect.signature` are not rewritten.

Outside FontLab, source modules import for documentation. Calling a declared
native function or constructing a native class raises `NativeUnavailable`.
Offline imports materialize the sidecar declarations; this costs more time and
memory than native imports. Static documentation tools can read them directly.
Native-valued attributes are annotated but cannot be read outside the host.
Top-level native spellings that are Python keywords or contain punctuation have
sanitized source aliases in newly generated declarations, including functions
and annotated values. Inside the host, alias reads, writes and deletes use the
original native spelling and follow later native reassignment. Outside the host,
annotation-only values remain absent; aliases do not invent placeholder values.
Existing merged facades retain their alias mappings. This tooling repair still
requires a reviewed capture/generated refresh and native acceptance.

New generation also retains captured documentation for module-level annotated
attributes, constants and namespaces. Maintained overlays can supply their docs
and type through the declared Python identifier, including a sanitized alias.
Those declarations remain annotation-only outside FontLab. This tooling repair
does not refresh the existing native captures or generated reference.

Unknown signatures deliberately use annotated `*args, **kwargs`. PySide2
reference overloads are labeled as upstream signatures because PythonQt calling
conventions differ. Only unanimous primitive types strengthen native signatures.

Generation preserves a single captured constructor signature and its documentation.
Explicit Python static/class constructors retain their descriptor binding and
unbound signatures, including inherited constructors. No constructor is invoked
during capture. Known Python instance methods and constructors retain their actual receiver name;
generation does not add `self` when that receiver is spelled differently. Unknown
native descriptors keep the conservative fallback until their binding is known.
Multiple constructor records retain all evidence under a variadic declaration;
the generator does not choose an overload. Missing constructor metadata keeps the
legacy fallback. This does not qualify constructor behavior in a newer host.

`fontpr` is captured separately. `fontlabpr` was absent in the verified host; its
facade supports runtime delegation when a future host provides it. No invented
`fontlabpr` API is shipped. PythonQt includes every discovered child, including
Config, Debug, private and BoolResult, even when the child cannot be imported as
a real Python module. C++ nested/template names have sanitized source aliases;
original names remain available through `getattr`.

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

## Scope

Echopy shims only FontLab's native bindings: `fontlab`, `fontgate`, `fontpr`,
`fontlabpr` (absent in measured builds; the absence is recorded) and
`FL` and `PythonQt.*`. It does not emulate other APIs. The `FL` module (FontLab 5
compatibility, `from FL import *`) is shipped as `fontlab_echopy.FL` (136
names, 30 classes, from a native FontLab 9 capture). To refresh it, run
`tools/capture_fl.py` in a checkout with fontlab-remopy (read-only, several
short host calls), then generate and merge. The raw capture JSON stays local,
like the other captures.

Packages that earlier releases generated here now belong to their producers:
`GlyphsApp`, `vanilla`, `AppKit`, `Cocoa`, `Foundation`, `objc` to
fontlab-glyport, `fontlabapp_shim` to fontlab-fontlabapp and `aidus_code_tools`
to fontlab-aidus-code. `fontlab_echopy.<name>` for those raises `ImportError`
naming the new home.

The Issue 123 branch's GlyphsApp manager, profile and provenance notes describe those moved shims; they now belong with fontlab-glyport.

## Extensions and immutable classes

```python
from fontlab_echopy.extensions import layer_names, has_layer, install_extensions
names = layer_names(glyph)
status = install_extensions()
```

The layer helpers work on original native objects. Installation adds only absent
methods to mutable native classes and reports immutable classes explicitly.
Maintained patch bodies are compiled into `_patch_extensions.py` by merge;
installation reads that generated registry. For any immutable class, use
`get_extension("fontlab.flGlyph.layer_names")(glyph)` to call its patch directly.
In the tested host, flGlyph cannot receive convenience methods, while QWidget
accepts `echopy_object_name`. The standalone helpers remain available in both
cases. Existing native methods are never replaced by convenience fallbacks.

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

## Document the actual native names

The enriched Python source is also the documentation authority for the live
`fontlab`, `fontgate`, `fontpr`, optional `fontlabpr` and `PythonQt.*` namespaces.
Capture inside FontLab first, then generate/enrich/merge outside it. Qt HTML
becomes structured Markdown docstrings: paragraphs, lists, links, tables and
code examples remain readable in the generated Python sidecars.

```sh
fontlab-echopy docnames /path/to/documentation/.build/native-names
```

This exports explicit Python aliases, with source/output SHA-256 provenance,
instead of copying declarations. Configure the mkdocstrings Python handler with
that directory and Echopy's source/install directory in `paths`,
`allow_inspection: false`, and `preload_modules: [fontlab_echopy]`. Then
`::: fontlab.flNode` documents the actual native name from the enriched source.
Keep these aliases on the documentation loader path; the live runtime continues
to use FontLab's original objects.

Use the Griffe extension
`fontlab_echopy.tooling.griffe_native.NativeNamespaceExtension` in the handler's
`options.extensions`. It preserves native classes such as `PythonQt.BoolResult`
whose empty pseudo-namespace would otherwise shadow their class declaration.
The alias manifest retains that namespace's source evidence. No native import
or method invocation is required to build the reference.

Code-shadow-derived code uses Apache-2.0. Qt reference documentation retains
GFDL-1.3 and PySide2 declarations LGPL-3.0 terms. See `NOTICE` and `licenses/`.
The legacy Aidus introspector retains its original proprietary license and is
archived only; it is not part of either installable distribution.

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
