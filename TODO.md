---
this_file: TODO.md
---

## FontLab 9.1 API — 2026-11-16

- [ ] live-verify 9.1 JSON/stroke/inktrap declarations in `fontlab_echopy.api91` on FontLab 9.1.9812 (serialized native lane, owned fixture): presence and the QByteArray round trip pass; `penParameters` writes, `expandStroke`, `makeStroke`, `inktrap_len`, presentation overrides and the refresh call remain.
- [ ] Run `examples/capture_in_fontlab.py` on 9.1.9812, regenerate `generated/` and the stubs, refresh identities/provenance, then promote the `api91` records into the stubs and `patches/manual.json`.
- [ ] Check the pyfontgate source for fgBrush/fgCapParams/fgShape.makeStroke signatures; it is not in the local C++ snapshot.


## Shared installer qualification — 2026-11-15

- [ ] Review and deliver the shared-installer candidate through fresh-main reconciliation, required gates, exact-SHA CI and genuine release/download qualification.
- [ ] After admission, verify installed provider/consumer identity and the applicable Script/Extension/native workflows without clearing existing holds by inference.



## Sdist test-input qualification — 2026-11-14

- [ ] Diagnose the existing docs filename-only diff failure with index refresh disabled; preserve the complete 55-file byte/mode oracle.
- [ ] Review the expanded Ruff 0.14.10 scope and 7,374 existing diagnostics without changing generated declarations to manufacture a green result.

# Open tasks

- [ ] Continue remaining FontGate guidance from captured declarations and reconcile overlays, aliases and provenance with pythonqtside/Fly consumers before the later full capture and installed-cohort pass.

- [ ] Reconcile the Issue 207 enriched candidate and its five catalogues with current producers before a reviewed regeneration.
- [ ] Qualify exact captures, aliases, docstrings, identities/provenance and ordinary installed consumers; document absent native APIs without inventing support.
- [ ] Run the exact repository checks on the integrated source, obtain independent review, commit/push the scoped milestone and verify its remote head.
- [ ] After qualified main integration, inventory obsolete branches/files, preserve unique work and remove only proven stale items with recovery evidence.

- [ ] Finish direct review and genuine source/wheel/complete-sdist installed tests for the normal-gated discovery repair; then commit/push the reviewed isolated feature.
- [ ] After D29/D30 clearance, capture actual native namespaces and qualify completeness/behavior; source fixtures do not close this task.

- [ ] Root review, normal80% gate, genuine matching manager-state archives and both complete ordinary provider/consumer/example tuples; source577pass/zero skips and31new controls are in CHANGELOG.md. Preserve actual defaults/CF/CG/CT/native, full original workflows and generated/publication holds.

- [ ] Fold FL into the next full pipeline run (identities, provenance, reports; PLAN item 1).
- [ ] Add maintained guidance to the 74 stub-only `fontgate` classes (73 + 46 are maintained today; structural coverage is already 100%). Next check: write it from captured declarations only, with no external text unless its licence is checked, and raise `MAINTAINED` in `tests/test_manual_class_docs.py`.
- [ ] Qualify source-repaired generation, text-signature provenance, distinct allocation/MRO evidence and required Qt seed diagnostics with a fresh native capture and generated refresh.
- [ ] Confirm fontlab-python-docs renders glyport, fontlabapp and aidus-code modules from their new homes.
- [ ] Qualify the installed-tested global Unicode source-derived shim in native/generated workflows.

- [ ] Qualify artifact-tested decorator-name isolation in consumers and native/generated workflows. Fresh wheel/sdist and authored examples pass; evidence is in WORK.md.

- [ ] Run the docs short rebuild against the current producer-derived shims after controller integration.
- [ ] After the next producer API change, regenerate the13source-derived shims again; this presentation-cohort source checkpoint is recorded in CHANGELOG.md.
- [ ] If App's public API changes, refresh `fontlabapp_shim` separately with `fontlabapp.shimgen` and a real FontLab capture; retain the applicable installed-artifact/native gates.

- [ ] Qualify static/class constructor binding repair with fresh native capture and generated refresh;166source tests and66installed checks per artifact pass, native acceptance remains separate.

- [ ] Qualify installed-tested generation collision preflight in native capture/generated refresh;82selected tests per artifact pass, reserved-identifier/duplicate-record behavior remains separate.

- [ ] Qualify top-level alias repair in real native/generated workflows; fresh installed wheel/sdist checks pass as recorded in WORK.md.

- [ ] Qualify native behavior of the installed-tested ordinary native deletion repair before promotion. Fresh wheel/sdist and downstream checks are recorded in WORK.md.

- [ ] Qualify remaining reserved-name interactions and downstream/native behavior; fresh wheel/sdist helper-name checks pass as recorded in WORK.md.

- [ ] Qualify genuine committed artifacts and full ordinary consumers for the refreshed compound catalogue; native/generated/main/publication acceptance remains separate.

- [ ] Qualify genuine matching description artifacts and the full normal installed provider/consumer/example tuple; source acceptance is separate.

- [ ] Qualify genuine matching ordinary archive/provider/consumer/authored-example tuple for the reviewed, normal-gated dynamic/document companion; retain explicit current-font/file/provider, private/default-resource, native/original, generated-reference, canonical and publication gates.

- [ ] Qualify genuine committed repaired archives, matching ordinary consumers/authored examples, then native/generated workflows under current holds.

- [ ] Root review, normal gate and genuine committed matching ordinary artifacts/consumer tuple for complete-generation consumers; retain private/default-resource, native/original, generated-reference, canonical and publication gates.

- [ ] Qualify genuine matching connected-manager archives and ordinary installed consumer/example tuple (root), then applicable native/full original workflows; preserve resource/generator, generated-reference, canonical and publication gates.

- [ ] Qualify genuine matching parent-aware archives and the ordinary installed consumer tuple, then applicable native/full workflows; preserve generated-reference, canonical and publication gates.

- [ ] Qualify the production Info refresh in ordinary artifacts, the exact consumer/authored-doc tuple (controller), then applicable native/full original workflows.

- [ ] Qualify the installed/cohort-tested combined Unicode index shim in native/generated workflows; preserve full original workflow and publication gates.

- [ ] Qualify reviewed committed receiver-binding tooling, a fresh native capture and generated refresh; unknown native bindings remain unclassified.

- [ ] Qualify the reviewed documentation source through ordinary main Actions and exact source/output lineage.
- [ ] Retain private Pages configuration and publication holds while native and owner-install gates remain separate.
- [ ] Qualify the six consumed C14 class overlays in a type checker or IDE that reads the installed `.pyi` stubs (hover and completion show the supplemental text); the installed wheel and sdist stubs and offline `help()` are verified by `tests/test_installed_class_overlays.py`. Inside FontLab 9 the classes are the native builtins, so `help()`, `__doc__` and the editor show native text only (live reports 32 and 32b); that is by design, not a defect.
- [ ] `generated/coverage.json` lacks `capture_identity`; regenerate with `generate` from a fresh native capture (shipped identity `5a405eb5a8888bc217c9653b606013439483a9ead5c0b9b1b478172c18e521e9`), then remove the manual README-merge restore of `capture_identity` in `_provenance.json`.
- [ ] Licence (Issue 250, owner Q5): `pyproject.toml` reads `Apache-2.0 AND LGPL-3.0-only AND GFDL-1.3-only`. The LGPL/GFDL terms come from PySide2-derived declarations, which the owner keeps as marked third-party. Check that every FontLab-authored file under `src/`, `tools/`, `enrichment/` and `tests/` is Apache-2.0 (no SPDX headers exist today: add them), and that `NOTICE` and `licenses/` mark exactly the PySide2-derived declaration files as third-party. `licenses/Qt-LICENSE.COMMERCIAL` stays a third-party text.
- [ ] Echopy provenance: `src/fontlab_echopy/FL.py` and `FL.pyi` are tracked but `_provenance.json` has no entry for them (none at e4a42b4 or 173c99fd), while `fontlab-echopy merge` lists both. Check whether they ship in the wheel: if so, make provenance hash them; if not, drop them from the merge input. Re-run the merge to confirm `capture_identity` is also preserved or generated. Predates batch 11; accepted as M-1 by reviewer2.
- [ ] Native check (D46): after the row-61 rewording, decide between a documentation-only close and a live recheck of the 7 classes whose overlays show 0/7 in an IDE.
