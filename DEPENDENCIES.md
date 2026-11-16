---
this_file: DEPENDENCIES.md
---

## Conditional installer requirements

Only conditional installer requirements use `packaging==26.3` in an external uv-managed Python environment. FontLab itself imports only the standard library; no permanent project dependency was added. An unavailable helper fails before sibling execution.



# Dependencies

The native facade and capture/generate/merge tools use the Python standard
library. Native FontLab modules are supplied by FontLab, not PyPI dependencies.
Beautiful Soup 4 parses official Qt HTML for the optional enrichment command.
Markdownify preserves its paragraphs, lists, links, tables and code blocks in
readable Markdown docstrings. It is an enrichment dependency, not a native
runtime dependency; its MIT-licensed upstream is
https://github.com/matthewwithanm/python-markdownify.
Pytest runs fixture, runtime-boundary, generation and annotation checks.
Griffe verifies canonical source/stub resolution without runtime inspection;
it is a test/documentation dependency, not a native runtime requirement.
Documentation builds load `tooling/griffe_native.py`, so Griffe is declared
in the `docs` extra (`pip install fontlab_echopy[docs]`) as well as `test` (R046).
The optional source-only NativeNamespaceExtension uses Griffe's public visit
and package hook APIs to preserve captured class/empty-namespace collisions.
Hatchling builds wheel/sdist; hatch-vcs derives versions from tags.

Official sources consulted: https://hatch.pypa.io/1.13/config/build/,
https://pypi.org/project/hatch-vcs/,
https://docs.python.org/3/library/importlib.html,
https://mkdocstrings.github.io/griffe/guide/users/loading/,
https://mkdocstrings.github.io/griffe/reference/api/loaders/,
https://pypi.org/pypi/PySide2/json,
https://doc.qt.io/archives/qt-5.15/qwidget.html.

PySide2 is a downloaded documentation input, never an imported runtime dependency.
Upstream wheel/page SHA256 hashes are in reports/qt-enrichment.json.

## Documentation build

A separate Python 3.13 docs environment uses the 31-package hash lock at `src_docs/requirements.txt`: ProperDocs 1.6.7, MkDocs 1.6.1, MaterialX 10.1.8 and PyMdown 11.0.1. Search is the sole plugin; light fltheme26 assets provide the shared menu/footer. Runtime dependencies and locks remain separate.
