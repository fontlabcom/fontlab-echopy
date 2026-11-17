---
this_file: src_docs/md/installation.md
---

# Installation

Use arm64 Python 3.11 for the FontLab host; this documentation build uses Python 3.13. Host installation and native acceptance are separate gates.

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

`fontpr` is captured separately; its tool functions take keyword arguments only.
Echopy ships no `fontlabpr` shim: the current FontLab source registers no such
module, only `fontpr`. PythonQt includes every discovered child, including
Config, Debug, private and BoolResult, even when the child cannot be imported as
a real Python module. C++ nested/template names have sanitized source aliases;
original names remain available through `getattr`.
