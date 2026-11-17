---
this_file: src_docs/md/declarations-and-tooling.md
---

# Declarations and tooling

## Scope

Echopy shims only FontLab's native bindings: `fontlab`, `fontgate`, `fontpr`,
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

## Document the actual native names

The enriched Python source is also the documentation authority for the live
`fontlab`, `fontgate`, `fontpr` and `PythonQt.*` namespaces.
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
