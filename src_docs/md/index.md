---
this_file: src_docs/md/index.md
---

# Echopy for FontLab


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


## Documentation map

Read [installation](installation.md), [declarations and tooling](declarations-and-tooling.md), [development and limits](development-and-limits.md), and [component licences](licence.md).
