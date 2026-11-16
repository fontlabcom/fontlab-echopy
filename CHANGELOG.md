---
this_file: CHANGELOG.md
---

## 1.1.16 (2026-11-16)

- `install.vfpy` is now the short fontlab-instamix stub. It installs
  fontlab-instamix from PyPI when it is missing, then installs this checkout from
  its `[tool.fontlab-install]` table. The large legacy installer is gone.
- README describes the stub install.

## 2026-11-16 — FontLab 9.1 API records (source-derived)

Also verified live (read only): `penParameters` returns a plain dict with string `join` and caps; `fgBrush()` defaults are recorded in `FGBRUSH_DEFAULTS`/`CAP_PARAMS_DEFAULTS`. `expandStroke` and `makeStroke` remain unverified. Focused checks: `tests/test_api91.py` 50 passed.

Added `fontlab_echopy.api91`: `NEW_IN_9_1` and `REMOVED_IN_9_1` record each FontLab 9.1.9812 Python API change with its signature, C++ source location and notes (flModelProducer clipboard JSON, flShape `penParameters`/`expandStroke`, `SmartCornerParameters.inktrap_len`, `flAxis.extrapolate`, flGlyphInfo/fgSymbol presentation overrides, Font Info `nametablePath`/`otherData`, two preferences, fgBrush stroke members, `fgCapParams`, `fgShape.makeStroke`; `fgBrush.size` removed). `PenParameters` is a TypedDict of the stroke dict. `detect(font=None)` uses `hasattr`, never the build number; `flPackage.info` entries are `None` (not checked) unless a font is passed, then `font.info` is checked. `objects_from_json()` wraps `bytes`/`bytearray`/`str` in a QByteArray before calling `getObjectsFromJsonData`, because passing `bytes` crashes FontLab 9.1.9812 (SIGBUS, verified live by the controller). `qbytearray_bytes()` uses `data()` because `bytes(qbytearray)` raises TypeError in PythonQt. The generated stubs are unchanged: they come from a 9.0 capture, and `tests/test_api91.py` fails once a 9.1 capture contains a recorded name, so it can be promoted.

Live evidence from the controller on FontLab 9.1.9812 (2026-11-16, font Lato): all 33 `NEW_IN_9_1` members exist by `hasattr` (the `info` members on a real font's `info`), `fgBrush.size` is absent, `QtCore.QByteArray(raw)` builds the right bytes, and `getClipboardDataJson` data re-wrapped with `QtCore.QByteArray(raw)` round-trips through `getObjectsFromJsonData` (one flGlyph back, no crash). Behavior is still source-derived and not live-verified: `penParameters` writes, `expandStroke`, `makeStroke`, presentation overrides and refresh calls.

Focused checks: `tests/test_api91.py` 48 passed in 1.06s, module coverage 99%; ruff clean. This agent did not run FontLab.


## 2026-11-15 — Shared installer source alignment

Copied the reviewed shared installer exactly: dependency constraints and managed origins remain protected; inactive conditional dependencies are filtered before sibling execution in the resolver target Python. FontLab imports remain standard-library-only. Package identity, runtime APIs, dependency declarations, scripts, bundles and legal files are unchanged. The real source-archive check now includes the exact root installer; the prior omission was reproduced before the single allowlist addition.

Focused checks: 6 passed in 3.23s. This qualifies the local source candidate only. Independent review, combined-main/full delivery gates, genuine release/downloads, installed provider closure and admitted FontLab/native workflows remain separate. No owner-folder installation or native operation ran.



## 2026-11-14 — Packaging source/main delivery qualified

The shipped-test sdist input fix reached main as source `15c9fdbb9bdc5e29699386b2b4a8e88a05d1821b`, followed by generated child `2061e202099ee894bba1af6b2c958a4c2a8b8560`. Independent source/main delivery review passed with qualifications. The unchanged normal pre-push gate passed 705 cases in 125.89 seconds; no production module changed and no new production coverage claim is made. The separately required extracted-sdist gate passed its outer case and all 705 inner cases. Exact-source Documentation run 43591905194, attempt 1, passed jobs 132438223744 and 132438304361, 36 docs cases each. The generated child changes only sitemap XML/gzip.

This closes only packaging source/main delivery. Local docs remain 35 passed / one inherited filename-only failure, Ruff 0.14.10 retains 7,374 findings, and provenance, licence, provider, installer, native, owner-install and private Pages gates remain separate. No new release or installation is claimed.

The older shipped-input entry below records the source-stage observation; this entry supersedes only its pending packaging delivery statement. Its other qualification limits remain open.

## 2026-11-14 — Shipped source-test inputs retained in the sdist

- The sdist now names the 18 tracked generated Python declarations, coverage.json and tools/capture_fl.py required by its shipped tests. No wheel payload or runtime source changed; raw captures and the legacy corpus stay excluded. Existing legal files remain unchanged.
- A fast source test checks every required sdist input byte and raw mode using the existing build fixture. A separate required packaging/release gate builds and extracts a real sdist, then runs every shipped source test in its own environment. It stays outside default discovery to prevent recursive archive builds and routine duplicate suites. Both commands are documented in AGENTS and README.
- Before the manifest repair, the complete artifact regression reproduced 252 failures and seven errors across the original 704 shipped cases. The earlier full default run passed 705 cases, including the archive gate, with all original 704 extracted-source case IDs and zero skips; its 163-second runtime motivated the separate packaging gate. The final default source recipe passes all original 704 cases plus the fast payload check: 705 passed, zero skips, 77.35 seconds. The fast payload oracle also rejects the original incomplete v1.1.14 sdist. Pre-run source checks assert arm64 Python 3.11.18, genuine VCS metadata, editable origin and Homebrew Git.
- The strict locked documentation build preserves all 55 output bytes, sizes and raw modes. The unchanged docs suite remains 35 passed / one filename-only failure; Ruff 0.14.10 remains at 7,374 existing findings, with none in the new regression. These failures, native/provenance/installer/full-provider qualification and reviewed upstream delivery remain separate.


## 2026-11-12 — D46 documentation pass (Issue 250)

- Landed on `main` this session (Issue 250/254): `5070d4f` and `4c48737` (six C14 overlays consumed), `9543b60`, `3d6ae8f`, `ee448b2`, `66a3468`, `89fda41`, class-guidance batches 7 to 11 (`f3239fa`, `d33a9b9`, `d6b67af`, `e4a42b4`, `173c99f`; all 73 fontlab classes maintained, 46 fontgate classes maintained), `da80ab4` (legacy-8 conversion), `bf90908` and `c3062d0` + `4abc82c` (`install.vfpy` sync, Issue 254). No source changed in this pass.
- New open TODO rows: the Q5 licence audit (SPDX headers, NOTICE marking of PySide2-derived declarations), the `FL.py`/`FL.pyi` provenance gap, and the native check for TODO overlays (0/7 classes).
- `WORK.md` was already a short status note; its current bytes (333 B, SHA-256 `2d412ebea7ee39f8ed669f1dcccbffdaf21fbb12e123c1eb8bfd0ada42f40492`) are archived with the other D46 notes.

## 2026-11-12 — Class guidance for ten stub-only fontgate classes, batch 11 (Issue 250)

- `patches/manual.json` gains captured-member guidance for `fgBitmaps`, `fgCMaps`, `fgCarets`,
  `fgContours`, `fgCuspPoints`, `fgDeviceRecords`, `fgGaspRecords`, `fgGlyphs`, `fgGlyphDict`
  and `fgGlyphIDsSet`. Every name is present in `generated/fontgate.py`; the `del_` spelling note
  and the `fgGlyphIDsSet` constructors follow the capture.
- `tests/test_manual_class_docs.py` pins them (plus a `contains` type-word check and a mutant test
  that an invented member is rejected) and raises `MAINTAINED` for `fontgate` from 36 to 46.
  74 `fontgate` classes remain stub-only.
- `fontgate.pyi` is regenerated by `fontlab-echopy merge`. `_provenance.json` is updated by hand to
  the merge result: `applied` 24083 to 24093 and the new `fontgate.pyi` and `manual.json` hashes.
  The raw merge output would also drop `capture_identity` and `_identities.json` (no raw capture
  here), so those were kept from the previous commit, as in batch 10.

## 2026-11-12 — Class guidance for the last six stub-only fontlab classes, batch 10 (Issue 250)

- `patches/manual.json` gains captured-member guidance for `Info`, `YPanelWidget`, `flCanvas`,
  `flItems`, `flPackage` and `flPreferences`, a selection of members each. Every name is
  present in `generated/fontlab.py`. The shared object members are listed only for
  `flCanvas` and `flPackage`.
- `tests/test_manual_class_docs.py` pins them and raises `MAINTAINED` for `fontlab` from 67
  to 73, so every `fontlab` class is now maintained. 84 `fontgate` classes remain stub-only.

## 2026-11-12 — Class guidance for nine more captured classes, batch 9 (Issue 250)

- `patches/manual.json` gains captured-member guidance for nine `fontlab` classes:
  `flObjectsList_flGuideLine_`, `flObjectsList_flShape_`, `flShapeData`, `flAbstractEditor`,
  `flVisualItem`, `flAbstractVectorNode`, `flVectorNode`, `flTextBlock` and `flWorkspace`.
  Each entry names only members present in `generated/fontlab.py`.
- `tests/test_manual_class_docs.py` pins them in `TARGETS` and raises `MAINTAINED`
  for `fontlab` from 58 to 67. Six `fontlab` and 84 `fontgate` classes remain stub-only.

## 2026-11-12 — Class guidance for ten more captured classes, batch 8 (Issue 250)

- `patches/manual.json` gains captured-member guidance for ten `fontlab` classes:
  `flExpression`, `flMarkerPoint`, `flShapeBuilder`, `flSnapLine`, `flSnapObject`,
  `flContourInfo`, `flLayerInfo`, `flNodeInfo`, `flShapeInfo` and `flGlyphInfo`.
  Each entry names only members present in `generated/fontlab.py`.
- `tests/test_manual_class_docs.py` pins them in `TARGETS` and raises `MAINTAINED`
  for `fontlab` from 48 to 58. Fifteen `fontlab` and 84 `fontgate` classes remain stub-only.

## 2026-11-12 — Class guidance for ten more captured classes, batch 7 (Issue 250)

- `patches/manual.json` gains captured-member guidance for ten `fontlab` classes:
  `TransformFrame`, `fgSymbolList`, `YPanelManager`, `flGraphicsInfo`, `flAuditInfo`,
  `flPropertyDouble`, `flPropertyPoint`, `flSearchInfo`, `flModelProducer` and
  `flBasicTool`. Each entry names only members present in `generated/fontlab.py`.
- `tests/test_manual_class_docs.py` pins them in `TARGETS` and raises `MAINTAINED`
  for `fontlab` from 38 to 48. A mutant adding an invented member to `flBasicTool`
  fails the names-only test. Remaining stub-only: 25 `fontlab`, 84 `fontgate`.
- `sh test.sh`: 632 passed.

## 2026-11-12 — Installer: unreachable blocked skip removed (Issue 250, review M-10)

- `install.vfpy` synced byte-identically from App (sha256 `2eb71691…` → `bbe8104e…`):
  `remove_old_dist` drops the `path.name in blocked` skip. Every blocked top-level
  name is also held, and a non-empty held refuses before anything is deleted, so the
  skip never ran. App's `tests/test_install_superseded.py` pins that invariant.

## 2026-11-12 — Class guidance for ten more captured classes, batch 6 (Issue 250)

- `patches/manual.json` adds supplemental guidance for `fontlab.FaBasicPtr`, `FontLayer`, `LocationValue`, `flLocation`, `flHintingParameters`, `flAxis`, `flSticker`, `flTransform`, `flPaper` and `flProperty`. Each entry names only members present in the captured declaration; the three constructor-only classes say so.
- `tests/test_manual_class_docs.py` lists all ten in `TARGETS` and raises `MAINTAINED["fontlab"]` from 28 to 38.
- Regenerated `fontlab.pyi` and `_provenance.json` with the README merge.

## 2026-11-12 — Eight legacy class guidance entries converted and pinned (Issue 250)

- `patches/manual.json` rewrites the guidance for `fontgate.fgContour`, `fgFont`, `fgGlyph`, `fgPoint` and `fontlab.flContour`, `flGlyph`, `flLayer`, `flNode` in the batch format: only captured members in backticks, and a `source` field naming the captured declaration. The factual claims are unchanged; the `flGlyph` extensions are kept.
- `tests/test_manual_class_docs.py` adds all eight to `TARGETS`, so every maintained overlay class (54) is checked against the captured members and merge output. The merge-shape test now allows for a class's declared `extensions` (`len(original.body) + len(patch.get("extensions", []))`; the appended tail must also equal the declared extensions (name, arguments, return, docstring), which kills a mutant that renames them in `merge.py`); flGlyph's two extension methods were the only reason it could not be pinned. The `MAINTAINED` ratchet is unchanged because these classes already carried guidance.
- Regenerated `src/fontlab_echopy/fontlab.pyi`, `fontgate.pyi` and `_provenance.json` (hashes only; `applied` stays 24028).

## 2026-11-12 — Class guidance for ten more captured classes, batch 5 (Issue 250)

- `patches/manual.json` adds supplemental guidance for `fontgate.fgBrush`, `fgCmapRecord`, `fgCoding`, `fgCuspPoint`, `fgGaspRecord`, `fgHintCommand`, `fgLib`, `fgMaxP`, `fgMetricsClass` and `fgOtValue`. Each entry names only members, constructor forms and math operations that the captured declaration carries.
- `tests/test_manual_class_docs.py` lists all ten in `TARGETS` and raises `MAINTAINED` to `fontlab` 28 and `fontgate` 36. Stub-only classes remaining: 45 `fontlab`, 84 `fontgate`.
- Regenerated `fontgate.pyi` and `_provenance.json` with the README merge; `_identities.json` and the provenance `capture_identity` were kept as shipped.

## 2026-11-12 — Class guidance for ten more captured classes, batch 4 (Issue 250)

- `patches/manual.json` adds supplemental guidance for `fontlab.flSnaps`, `PaintBrushShape`, `flMouseEvent`, `flModel` and `ExportControl`, and `fontgate.fgAxis`, `fgMaster`, `fgMasters`, `fgGuide` and `fgComponent`. Each entry names only members, constructor forms and type words that the captured declaration carries; no external text was used.
- `tests/test_manual_class_docs.py` lists all ten in `TARGETS` and raises `MAINTAINED` to `fontlab` 28 and `fontgate` 26. Stub-only classes remaining: 45 `fontlab`, 94 `fontgate`.
- Regenerated `src/fontlab_echopy/fontlab.pyi`, `fontgate.pyi` and `_provenance.json` with the README merge; `_identities.json` and the provenance `capture_identity` were kept as shipped.

## 2026-11-12 — Captured-member checks cover all twenty new classes (Issue 250)

- `tests/test_manual_class_docs.py` `TARGETS` now lists the twenty classes added in the last two batches, so the names-only-captured-members and merge-unchanged checks apply to them. Mutants that replace one captured member name with `bogusMember` in `fontgate.fgZone`, `fontlab.flStem` and `fontlab.AccentInfo` now fail the captured-member test itself, not only the provenance hash.
- The new check caught `fgAnchors` guidance that backticked the native name `del`, which is not a stub member; the sentence now leaves it unquoted.

## 2026-11-12 — Class guidance for ten more captured classes, batch 3 (Issue 250)

- `patches/manual.json` adds supplemental guidance for `fontlab.AccentInfo`, `GlyphComponent`, `flEvent`, `flLayerAttributes` and `SmartCornerParameters`, and `fontgate.fgAxes`, `fgCaret`, `fgDesignPosition`, `fgDeviceRecord` and `fgAnchors`. Each entry names only members and types present in the captured declaration. The merged `.pyi` stubs and `_provenance.json` were refreshed with the README merge (restoring `capture_identity`, leaving the `FL` entries out). The maintained-class ratchet in `tests/test_manual_class_docs.py` rises to fontlab 23 and fontgate 21; totals stay 73 and 120.

## 2026-11-12 — Overlay delivery check moves to the stub path (Issue 250)

- `tests/test_installed_class_overlays.py` now renders `pydoc` (what `help()` shows) in a fresh environment with the installed wheel for each of the six overlay classes and requires the supplemental text.
- Live reports 32 and 32b: inside FontLab 9 every class is the native builtin, so `help()`, `__doc__`, `inspect.getdoc` and `pydoc` show native text only (0 of 7 checked), and the script editor has no hover or completion route. TODO row 61 is reworded accordingly: overlays reach users through the `.pyi` stubs and offline help, not through the host.

## 2026-11-11 — Class guidance for ten more captured classes (Issue 250)

- `patches/manual.json` adds supplemental guidance for `fontlab.Interval`, `PaintBrush`, `flInstance`, `flStem` and `flTTHCommand`, and `fontgate.fgGroup`, `fgMatrix`, `fgPen`, `fgStem` and `fgZone`. Each entry names only members and types present in the captured declaration, with no inferred behaviour. The merged `.pyi` stubs and `_provenance.json` were refreshed with the README merge (restoring `capture_identity` and leaving the `FL` entries out, as before). The maintained-class ratchet in `tests/test_manual_class_docs.py` rises to fontlab 18 and fontgate 16; totals stay 73 and 120.

## 2026-11-11 — Class guidance test accepts the class's own name (Issue 250)

- `tests/test_manual_class_docs.py` now allows a backticked class name (for example `fgSymbol()`) in class guidance while still rejecting any other backticked name that is not a captured member. The check is a small helper with accept and reject tests; four mutants (drop the member set, drop the class name, add a free name, allow any name) fail.
- Two tests pin the merge contract for `capture_identity`: a merge drops an identity its raw input does not carry (so a refresh from the committed `generated/` must restore it by hand, as the README flow and the last two refreshes did), and records one the raw coverage carries. The drop is deliberate (a merged package documents only its raw input's capture), so no code changed.

## 2026-11-11 — Maintained guidance for ten more classes (Issue 250)

- `patches/manual.json` adds supplemental class guidance for `fontlab.FontMetrics`, `flZone`, `CurveEx`, `fgSymbol`, `flObject` and `flPinPoint`, and `fontgate.fgKerning`, `fgKerningGroups`, `fgKerningObject` and `fgKerningObjectPair`. The classes are the ones App, Scriptmix, Examples, Fontport and Glyport reference by name (FontMetrics 39 files, flPinPoint 12, fgSymbol 10, flObject 6, flZone 3, CurveEx 3; the fgKerning chain is reached through `fgKerning`). Each statement names only members present in the captured declaration; none describes behaviour.
- The shipped `fontlab.pyi` and `fontgate.pyi` and the matching `_provenance.json` entries (`applied` 23988 to 23998, two stub hashes, `manual.json` hash) come from the README merge command; `capture_identity` and `_identities.json` are unchanged.
- The ratchet in `tests/test_manual_class_docs.py` is raised to `MAINTAINED = {"fontlab": 13, "fontgate": 11}` and the ten classes join the captured-member and merge-integrity tests. Before the patch the ratchet and the shipped-provenance test failed; the full suite is 485 passed.
- The `fgSymbol` guidance ends with a caution taken from the filed report: FontLab 9.0.9809 terminates when `fgSymbol()` is called with no arguments (Fontlab/fl#8632). The text does not suggest any creation form.
- Still open in TODO: 60 stub-only `fontlab` and 109 stub-only `fontgate` classes. `flLocation` (no captured members) and `Interval` (no consumer) were skipped.

## 2026-11-11 — Shipped provenance pinned to the shipped stubs (Issue 250)

- `tests/test_manual_class_docs.py` now checks that every `merged_outputs` hash in `_provenance.json` equals the hash of the shipped file, that the overlay hashes equal the current `enrichment/qt5.json` and `patches/manual.json`, and that `merge.applied` equals a fresh merge's count. Reverting `applied`, the `fontlab.pyi` hash or the `manual.json` hash each fails this test (previously all passed at 460).

## 2026-11-11 — Six C14 overlays verified in the installed wheel and sdist (Issue 250)

- `tests/test_installed_class_overlays.py` builds the package with `uv build`, installs the wheel and the sdist into fresh Python 3.11 virtual environments and reads the installed stubs. The installed `fontlab.pyi`, `fontgate.pyi` and `_provenance.json` match the source bytes and recorded hashes, and the `flAnchor`, `flGuideLine`, `flShape`, `fgAnchor`, `fgLayer` and `fgShape` class docstrings carry their `patches/manual.json` guidance.
- Mutants fail: a wheel that excludes `*.pyi` and a stub with the `flShape` overlay removed.
- The FontLab 9 hover help and `help()` check stays open in TODO.

## 2026-11-11 — Six C14 class overlays consumed into the shipped stubs (Issue 250)

- Ran the README merge (`fontlab-echopy merge generated … --overlay enrichment/qt5.json --overlay patches/manual.json`) in a scratch directory and reviewed the result against `src/fontlab_echopy`. The only content change is the supplemental guidance in the `flAnchor`, `flGuideLine`, `flShape`, `fgAnchor`, `fgLayer` and `fgShape` docstrings in `fontlab.pyi` and `fontgate.pyi` (3 lines replaced, 18 added per file). No signature, no `.py` file and no PythonQt file changed.
- `_provenance.json` follows: `merge.applied` 23982 to 23988, the `manual.json` overlay hash and the two `.pyi` output hashes. The capture and Qt enrichment records are untouched, because only the merge step was rerun.
- Installed-package and FontLab 9 checks stay open in TODO.

## 2026-11-11 — Class docstring ratchet (Issue 250)

- `tests/test_manual_class_docs.py` now merges `patches/manual.json` the repo's way and counts class docstrings that carry maintained guidance: 7 of 73 `fontlab` and 7 of 120 `fontgate` classes. It fails if either count drops or the captured class total changes, and asks for the constant to be raised when guidance is added.
- TODO row reworded to the counted target: 66 + 113 stub-only classes.

## 2026-11-11 — C14 captured class documentation overlays

- Added source-cited manual guidance for fontlab flAnchor, flGuideLine and flShape,
  and fontgate fgAnchor, fgLayer and fgShape. Canonical generated declarations,
  native signatures and runtime modules remain unchanged.
- 21 regressions fail before the overlays and pass after: captured member names,
  merged docstring/signature preservation, and a (class, member, type-token) table
  asserting each type word (QPointF, QLineF, QRectF, flContour, fgContour, bool)
  against the captured declaration and the overlay. `fgLayer` wording now says
  `countContours()`/`countShapes()` report contour and shape counts.
- Full Echopy gate run on the merged tree before push (see lander report). No
  production module changed. Generated refresh and native checks remain open.

## 2026-11-10 — live font editing rule (Issue 250, D44)

- AGENTS.md: agents test and edit the font open in FontLab 9, starting from the Desktop VFJs, and may save them.

## 2026-11-10 — isolated graph guidance proposal

Prepare append-only AGENTS guidance for separate task-owned graph HOME and storage, ordinary-analysis scope and independently reviewed bounded recovery. Preserve existing integration rules and acceptance holds. This documentation proposal records no new runtime, test, native, integration or publication result.

## 2026-11-10 — install.vfpy always reinstalls scripts and dependencies

- Every install copies all files from `Scripts/` afresh and replaces any file
  already at the same path. A symlinked script folder is replaced by a real
  folder; the link target is never written. A directory where a script file
  belongs is still refused.
- Required packages are installed on every run. Packages that no package
  index carries (the fontlab-* packages, pythonqtside) are installed from
  checkouts beside this one through their own `install.vfpy`, once per run
  and safe against cycles. uv receives every other requirement, so version
  ranges, markers and extras are enforced. Without uv, sibling checkouts are
  still installed and only the remaining missing requirements are reported.
- The installer is byte-identical across all eleven installer repositories.

## 2026-11-06 — Required legacy capture metadata

- Retain inspected signature provenance and conservative `__text_signature__`
  evidence when inspect cannot describe a callable; reject malformed signatures
  and nonliteral defaults without executing them.
- Capture distinct `__new__` allocation metadata and MRO independently of
  `__init__`; retain allocation/MRO evidence in generated class documentation.
- Report discovered and missing required Qt seeds, including an absent root,
  through the existing capture CLI. Embedded chunked metadata retains its current
  transport and error contracts.
- Fresh current-source baseline 416 passed; final source suite 437 passed with
  zero skips. Actual native capture, generated reference and delivery gates remain
  separate; no retained declarations, archives, source locks or dependencies changed.

## 2026-11-05 — Issue 230 remote documentation variant

Observed remote source: `48e39a8a5758783980400d99d576ec77dced7b0e`.
Prepared the reviewed source/documentation guidance for this remote base.
Retained `legacy/README.md`, `legacy/source.tar.gz` and
`licenses/aidus-legacy-LICENSE` unchanged. Historical cleanup receipts
do not assert archive deletion on this branch. Runtime, tools and tests
match the canonical checkpoint; this variant changes guides only.
Checked guide structure and preservation hashes. No suite, generation,
release, native installation or remote-delivery result is claimed.
Independent review precedes guarded application. Later delivery status
belongs in the external Issue 230 live ledger. Issue 123 remains paused.

---
this_file: CHANGELOG.md
---

## 2026-11-04 — Issue 123 capture discovery

- Capture unions advertised and stored names, discovers PythonQt children from the module
  registry, and documents annotated attributes. The branch's GlyphsApp/objc shim refreshes and
  their 14 shim export tests were not taken: those shims moved to fontlab-glyport in Issue 201.

## 2026-11-03 — installer options, licence and cleanup

- `install.vfpy` reads optional `[tool.fontlab-install]` keys: `name` (the distribution
  record), `packages` (`[]` installs scripts only) and `dependencies` (what FontLab needs,
  instead of `project.dependencies`). Symlinks inside `Scripts/` are not copied.

## 2026-11-03 — install.vfpy fixes from runs inside FontLab 9

Verified by installing all nine packages inside FontLab 9 (Python 3.11.6, arm64).
- Dependencies with console scripts (glyphsLib, fontTools) failed: uv writes them to
  `site-packages/../../../bin`, which resolves through the venv link to the FontLab
  folder. `bin`, `share` and `include` there now link back into `.venv`.
- A failed install appends a `"failed"` record with the traceback and uv's output to
  `install.log`; List/Uninstall ignore failed records.
- Package records include `WHEEL`, so `uv pip check` accepts them.
- Scripts are copied file by file into FontLab's `Scripts` folder, from a package's
  `Scripts/` folder (exact case) and from folders listed in `[tool.fontlab-install] scripts`.
  Folders shared by several packages merge, e.g. two packages' `Scripts/Kerning`. The
  installer refuses to overwrite a file another package or the user put there; uninstall
  removes only its own files, their `.pyc`, and folders left empty. An older install's
  folder link (`Scripts/Aidus Code`) is replaced by copied files.
- `*.vfpyc` (FontLab's compiled `install.vfpy`) is ignored by Git.

## 2026-11-03 — install.vfpy creates FontLab's venv

FontLab's `python/3.11/site-packages` is now always a real folder; packages are
symlinked into it, so no `.pth` processing is needed. `install.vfpy` creates `.venv` with
uv from FontLab's exact Python version and processor type, and links the venv's
site-packages to FontLab's folder, so `uv pip install --python .venv/bin/python` installs
into FontLab. An older layout (FontLab's folder linked into `.venv`) is migrated.

## 2026-11-03 — reverse-domain extension id and install.log

`[tool.fontlab-install] id = "com.fontlab.echopy"` names this extension. `install.vfpy` keeps
`Extensions/com.fontlab.echopy/install.log` (JSON Lines; the last line lists every installed file),
puts copied code in `Extensions/com.fontlab.echopy/lib/`, and adds Scripts > Extensions >
List Extensions and Uninstall com.fontlab.echopy.

## 2026-11-03 — install.vfpy without uv

`install.vfpy` now needs only FontLab's Python. It asks FontLab for its data folder
(`flPreferences().dataPathDefault`), links a Git checkout or copies a plain folder into
`Extensions/`, and writes a `.pth` plus `.dist-info` into `python/3.11/site-packages`.
uv is used only to add missing dependencies. It never replaces folders it does not own.

## 2026-11-03 — release scripts

Added `build.sh` (uv build into dist/), `publish.sh` (`uv publish`; refuses a dirty
tree or an untagged HEAD) and `install.vfpy` (editable install into FontLab's venv
from inside FontLab). Version stays hatch-vcs from `vX.Y.Z` tags.
## Echopy shims only native bindings (issue 201) -- 2026-11-03

Removed the generated `GlyphsApp`, `vanilla`, `AppKit`, `Cocoa`, `Foundation`,
`objc`, `fontlabapp_shim` and `aidus_code_tools` packages, `tooling/shims.py`, the
`fontlab-echopy shims` command and their tests (`test_shims.py`,
`test_standalone.py`). Their new homes are fontlab-glyport, fontlab-fontlabapp
and fontlab-aidus-code. `fontlab_echopy.<name>` raises `ImportError` naming the
home (`fontlab_echopy.MOVED`, tested). The native shims and their captured
identities are unchanged. Stale PLAN, TODO and WORK notes were reduced to the
current state; the full text is in git history.
## Complete namespace discovery source repair — 2026-11-02

Restored useful legacy discovery responsibilities in maintained tooling: union
advertised/direct dictionary names, loaded PythonQt child candidates, qualified
child import fallback, and preservation of other scopes after an ordinary failed
getter. Root identity wins over registry/import identity; nested keys identify an
immediate parent. Registry keys are snapshotted; errors retain name/type without
private values. Missing optional children and broken dependencies stay distinct.
Failed root getters are not retried; deadlines/interrupts propagate.

Eighteen regression-first cases had13failures/5passes before repair. Initial
focused66passes; expanded unchanged normal598passes/zero skips, all4main-relative
modules93.86–98.35%, capture96.40%. Two additional end-to-end owned pipelines now
verify discovered declarations/signatures/docs and dependency errors survive
capture/generate/merge. Final normal600pass/zero skips retains the same coverage;
root review and genuine archives/ordinary tooling qualification follow.
All native/manual/generated/legacy/enrichment/source-lock payloads and inherited
oracles remain unchanged. No actual capture, native/framework import/call, site
or installation mutation. D29/D30 and full native/migration/promotion goals remain.
Exact receipts live beside this isolated checkout in capture-discovery-20261102.


## Manager-state producer companion verified in source — 2026-11-02

Ran the complete actual13-target shim CLI against sealed Glyport5e04d1168.
Only GlyphsApp/_shim.json's catalogue digest/direct info_manager fingerprint
change. The exact class re-export already exposes inherited accessors/ranks,
observation/cache/recovery/dealloc and the actual class font selector; duplicate
stub bodies or generator changes are unnecessary. Every.py/.pyi and inherited
native/generated/manual/legacy/enrichment payload stays unchanged.

Thirty new actual session cases span profiles2/3/4: signature/class/source identity,
raw setters/nil/map identity, lazy sidebar/script ranks/terminal categories/cache,
debug queue/current CPU/group construction and real base-parser adoption,
reinitialization preservation, class/instance access to class font lookup,
global cache ordering/duplicate/release/invalidation, current shared observer and
superclass dealloc, exact error fields/two-code-read recovery and missing-provider
refusal. All process-global cache/shared/session/module/path scopes restore.
One additional real Griffe consumer check loads source without inspection,
resolves the actual class alias and verifies inherited_members, class-method
label/parameters and retained docs. No native/resource imports or fabricated
native defaults. Complete615committed producer graph independently rehashed;
direct-origin catalogue hashes are deliberately not a transitive inventory.

Inherited baseline538pass/8stale-fingerprint failures. Newred27pass/3fingerprint
failures; actual CLI refresh exits0; new30pass, then31pass with the Griffe check.
Full source577pass/zero skips,45.23s. All41old test files and every inherited
assertion remain byte-exact. Scoped RuffE4/E7/E9/F and formatting pass with AST
identity; all3new test/fixture files remain below200lines. Exact expanded argv,
environments/exits/logs/JUnit and preimages: adjacent echo-evidence/.

The exploratory Griffe get_member call does not search inherited members;
its initial KeyError receipt/preimage is retained, and the actual documented
consumer uses inherited_members. No source/declaration rewrite masks this.
Root owns direct review, normal80% gate, genuine committed archives and complete
ordinary provider/consumer/example tuples. No borrowed-env install, sibling/
owner/canonical write, native/framework/MCP request, capture/manual/generated
reference/source-lock/site refresh, commit or push. D16/D29/D30/D31 and the full
original native/scripts/dialog/four-font/Aidus/promotion scope remain open.

## Dynamic sidebar/document producer companion — 2026-11-02

Regenerated all13source-derived shim targets against sealed Glyport788959172.
Only GlyphsApp's catalogue digest/direct manager hash changes; all declarations,
facades, held native/generated/manual/legacy/enrichment bytes and old tests remain.

Added51actual-export cases across Glyphs2/3/4 for dynamic categories, UTF16 and
count filtering, child identity/reparenting, process-once mapping, repeated type
reads, tree/tag/filter order and reload failure state. Current document tests
cover real URL lifecycle, local allocator/parser/sidebar/queue and explicit
missing provider/file/FontLab fontType boundaries. Source546passed/zero skips;
scoped lint passes. Exact receipts: adjacent echo-evidence/REPORT.md. New ordinary
artifacts/consumer tuple, native/full original workflows and publication remain
separate. No dependency change.

## Module value and annotation documentation contracts — 2026-11-02

Forward writes to accepted native _echopy_* attributes and aliases, retaining
three exact internal state fields and import bookkeeping. Preserve captured
module attribute/constant/namespace docs in generation; apply top-level annotated
value doc/type overlays without materializing offline values. Forty-four additive
owned cases include real capture/Griffe and full identity lifecycle. Mandatory
normal gate495passes; three changed modules93.86–98.35% combined coverage.
Retained red27fail/12pass and focused133pass; existing assertions unchanged.
Actual native/generated outputs and captures remain unchanged; no new native
acceptance claim. Adjacent external stage retains exact commands and evidence.


## Complete-generation producer companion — 2026-11-02

Regenerated all13source-derived targets against sealed Glyport5a54b4b68.
Only GlyphsApp/_shim.json changes; direct class re-export declarations and all
native/manual/legacy/enrichment payloads remain unchanged. No dependencies change.

Owned fixtures supply four explicit invented banks and run real complete Chinese
and queued Hangul algorithms. Eighteen added real session cases across profiles
2/3/4 check all fixed positions, actual fields, canonical identity, AC00/AC01 and
finalD7A3 components, current-map reload and missing-bank failure semantics.
Obsolete callback-count oracles are replaced; valid inherited assertions remain.
Full source451passed/zero skips; scoped quality checks pass. Retained preimages,
failed attempts, exact commands and limits: adjacent echo-evidence/REPORT.md.

This qualifies owned source algorithms only. Private/default resources, native
equivalence, ordinary artifacts/consumers, generated reference and publication
remain separate gates.

## Connected local-manager producer companion — 2026-11-02

Regenerated the 13 source-derived targets against reviewed Glyport29efa7f9.
Only GlyphsApp/_shim.json changes: catalogue identity and direct manager-source
fingerprint. Exact GSGlyphsInfo re-export declarations and all other generated,
native, legacy, manual and enrichment payloads remain unchanged.

Added nine real session-export checks across Glyphs2/3/4:17actual lifecycle/
sidebar/control signatures, exact source class, owned constructor/parser/sidebar/
queue behavior, reload identity/pending work and missing-provider refusal. One
obsolete expected capability in an inherited test now names the explicit missing
provider; its refusal/NULL/retained-view assertions remain. Preimages are retained.
Full source433passed/zero skips;81protected payloads and scoped quality checks
pass. Exact evidence: adjacent echo-evidence/REPORT.md. No dependency change.

Source qualification does not establish default-resource or native completeness,
new ordinary artifacts/consumers, generated reference, promotion or publication.

## Ordinary test-origin correction — 2026-11-02

The first installed full suite records395passes/29failures: the inherited compound
fixture asserted sibling-source origins while the runtime correctly came from the
ordinary prefix. It now selects the actual imported Echopy/available Glyport origin,
retaining exact producer-path assertions and every behavior case. New parent tests
also defer optional producer lookup until the fixture, preserving the existing
absent-producer test boundary. Qualified source/ordinary tuples require all cases
and zero producer skips. No packaged runtime, declaration, catalogue or dependency
changed. Exact preimages/red/final gates: adjacent root-review/ and qualification logs.

## Parent-selected manager exports and exact wrapper profiles — 2026-11-02

Regenerated all 13 source-derived shim targets through the existing CLI against
Glyport 97304f34 and the reviewed sibling sources. Only GlyphsApp and objc
sidecars/catalogues change: the exact Glyphs 3 application wrapper, GSGlyphsInfo
manager origin and source hashes, and the owned objc.NULL sentinel. No generated
file was hand-edited; tooling, dependencies and captured native data are unchanged.

All 399 inherited cases remain, with precise obsolete profile/type/provenance and
font-refusal oracle repairs in three test/fixture files. The full source suite
passes 424 tests, zero skips, including 25 new actual ExecutionContext/session
export checks for document/shared manager identity, owned parsed six-field data,
canonical records versus raw frozen snapshots, unknown-source refusal, and exact
Glyphs 2/3/4 keyword, integer, formatting, font and override behavior.

This is source acceptance. Fresh ordinary archives, consumers and native/full
workflows remain separate; no canonical/live, generated-reference or publication
action was performed. Exact preimages, red/green attempts and byte audit are in
adjacent echopy-evidence/REPORT.md.

## Description producer provenance and real exports — 2026-11-02

Regenerated the 13 source-derived targets against Glyport597f4ec and the reviewed
App/Aidus siblings. Only GlyphsApp/_shim.json changes: glyph_info.py fingerprint
and capture digest. All exported entries, Python facades, sidecars, native capture,
legacy and enrichment payloads remain byte-identical. No dependency/runtime code
or declaration was manually changed.

The inherited 385-test suite first records 7 stale-provenance failures / 378 passes.
Current full source passes all 399 tests, including 14 new actual description-export
controls. Against the previous compound source, all 14 new cases fail while the
15 compound controls pass. Current source passes those 29 together. The fixture
checks real class origins, exact re-exports, source dictionaries and session/path/
module restoration. New tests pass pinned Ruff and whitespace checks.

These are source/export checks. Genuine matching committed archives, full ordinary
installed consumers, parent-aware glyph-info manager and native/original workflows
remain separate requirements. No live/canonical, source-lock or generated-site action.


## Compound producer provenance and exported-state checks — 2026-11-02

Regenerated the 13 source-derived shim targets through the existing CLI against
the current reviewed producers. Only GlyphsApp/_shim.json changed: the glyph_info.py
fingerprint and capture digest identify the real compound producer. All exported
entries, Python facades, sidecars, native captures, legacy and enrichment data
remain byte-identical. No runtime dependency or generated declaration changed.

The inherited suite first recorded 7 stale-provenance failures and 363 passes.
The refreshed source passes all 385 tests, including 15 new actual session/export
checks for raw/shared/copy/nested/positional state and owned cleanup. The older
ordinary producer fails 13 new cases while two single-record controls pass.
Pinned Ruff and whitespace checks pass. These are source/export results; new
committed archives, ordinary consumers and native workflows remain pending.


## Production checkpoint review repairs — 2026-11-02

The Glyport review successor retains its raw GSGlyphInfo constructor after a
rejected case override. Regenerated all13source-derived CLI targets after that
rollback; the total14catalogues include the separately generated App shim.
Only GlyphsApp/_shim.json changes, restoring the matching producer hash/digest.
All14catalogues equal the qualified parent and all non-catalogue runtime bytes
stay unchanged. No generated declaration/facade was hand-edited.

The first inventory attempt expected13total catalogues and stopped before CLI
execution; its14catalogue preimages and runner remain retained. The corrected
regeneration exits0. Exact command/environment, before/after hashes and log:
production-checkpoint-20261102/repair-evidence/regeneration-after-rollback*.
Full current source passes370/0skips in18.37s, exit0. No executable production
module changed, so no new module-coverage claim is made. The full current source
command is in production-checkpoint-20261102/repair-evidence/echopy-corrected-raw-
snapshot-plain-command.json. Ordinary/genuine committed-artifact qualification
remains pending. Parent artifacts qualify only their exact source tuple.
Native D30 and all full factory/custom/local/version/original requirements remain.

This is an isolated reviewed source checkpoint candidate. D11authorizes source
commit/push after applicable gates; current main/canonical installs, generated
source-lock/site, native calls, release/tag and publication remain untouched.
Exact source checkpoint hashes, pre-push command exits and further artifact
results belong in the external production-checkpoint report; no passing claim
is made here for an unrun command or a later committed distribution.

## Production Info shim provenance and export regression — 2026-11-01

Regenerated all13source-derived catalogues from the source-qualified production
Info producer. Only GlyphsApp's capture digest and glyph_info.py hash change;
exported entries, runtime executables and declarations remain unchanged.
Fourteen real session-export tests distinguish raw nullable production, shared
exact/alias fills, detached uni/u and shallow/deep copies, empty/explicit/equal
text, suffix helper output, read-only behavior and unavailable-source refusal.
All caller/module/path/source restoration checks pass.

Complete source370passed/zero skips;124protected files and inherited export
controls stay byte-identical. Scoped quality checks pass. Exact commands,
preimages and failed attempts are in the task's adjacent echopy-evidence.
No dependency change. Ordinary artifacts/consumers, native/full workflows,
generated documentation, canonical promotion and publication remain separate.

## Combined Unicode index shim provenance — 2026-11-01

Regenerated all13source-derived shims from the corrected Glyport combined
primary/legacy Unicode index. Only GlyphsApp's capture digest and two producing
source hashes change; exported entries and every executable/declaration stay
unchanged. Global-export regressions now preserve False/0000→NULL and
FE8D/FE80→the corresponding Arabic .isol records without promoting their legacy
encodings into primary Unicode. Existing spelling, integer dispatch, font-local
refusal, override and session/path restoration controls remain.

Full source356passed/zero skips; all13catalogues and124protected files verify.
Scoped quality checks pass. Exact private commands/results and preimage checks are
retained in the cohort's adjacent echopy-evidence directory. This source refresh
does not qualify native bindings or authorize generated documentation,
canonical promotion or publication. No dependency change.

## Legacy/ROS producer-derived shim refresh — 2026-11-01

Regenerated the13source-derived shims against the reviewed legacy/ROS Glyport
candidate. Only GlyphsApp's catalogue digest and glyph_info.py source hash changed
from the presentation input. Existing GSGlyphInfo re-exports expose unicodeLegacy
without duplicate declarations or invented native setters. Four new export checks
cover exact snapshot values, read-only refusal and producer provenance. Full source
suite passes329tests, zero skips, with all actual producer siblings present.
ROS mapping remains explicitly unavailable; global factories ignore active fonts.
Full ROS mapping, custom managers, global Unicode lookup and native workflows
remain unqualified. No native capture, generated-native refresh or publication.

## Presentation-cohort source-derived shim refresh — 2026-11-01

Historical command examples use `FONTLAB_SCRATCH` for the caller-selected external
workspace root; no private volume path is distributed.

Regenerated all13source-derived targets against the reviewed Glyport parameter/
Arabic-presentation candidate and Aidus integration. Only GlyphsApp/_shim.json
changed: its catalogue digest and two producer-source hashes. The exported
catalogue declarations and all .py/.pyi facades remain byte-identical.

The baseline passed324tests and failed the expected stale-producer comparison.
After regeneration the full source suite passes325tests with both actual sibling
producers present and zero skips. All124protected tracked files outside the
allowed shim outputs/documentation remain byte-identical, including native
facades, App shim, manual overlays and historical provenance. This proves source
currency, not native behavior, a new capture or documentation publication.

## Echopy decorator artifacts and guide verified — 2026-11-01

Fresh wheel/sdist installs each pass245selected tooling checks, zero skips.
Same-process tooling origins are installed; all95runtime files match source,
archives and both installs.142sdist files pass inclusion/privacy/licence and
copied-test checks.117protected generated/provenance files remain unchanged.
The prior same-version wheel fails18new checks and passes5controls.

The authored pipeline example now accepts qualified decorators and checks real
raw/merged descriptor identity with captured staticmethod/classmethod members.
Both installs pass10offline examples; all12blocks compile. The earlier wheel
raises NativeUnavailable in the new fixture. Earlier bare-syntax guide failure
is retained; it prompted the behavior-based example update. Only that fixture's
archive hashes changed; other examples retain their own historical hashes.

Exact commands, exit codes, origins, bytes and negative controls are retained in
verification/issue-123/echopy-decorator-artifacts-20261101.json and
verification/issue-123/docs-decorator-resolution-20261101.json. Diff check passes.
The coverage fixture is historical, not a fresh capture. Native/generated,
consumer-cohort, browser and publication acceptance remain open; no canonical
promotion or live installation. D16/D27/D29/D30/D31 remain unchanged.

## Echopy decorator-name resolution repaired in source — 2026-11-01

Generated constructor/method decorators now use a deterministic private builtins
alias absent from normalized module and class names. Captured staticmethod and
classmethod names remain exposed. Existing collision/refusal checks, direct
function-helper behavior, coverage and exports remain intact. Merge retains the
import in sidecars without changes; runtime facades remain lazy.

Regression-first tests failed 16 cases before the repair. Full source suite now
passes 325 with zero skips; focused suite107 and independent root suite99 pass.
Actual module/class helper shadows, repeated occupied aliases, constructors,
raw/merged descriptor identity and signatures are covered. All117 protected
files remain byte-identical. Scoped lint and diff checks pass. Exact commands,
exit codes, preimages and source hashes:
verification/issue-123/echopy-decorator-repair-20261101.json.

Only tooling/generate.py and its new tests changed in implementation; README
explains the behavior. No native calls, generated refresh, canonical promotion
or publication. Fresh wheel/sdist, guide examples and downstream qualification
remain next; full native fidelity and existing owner holds remain open.

## Echopy merged helper conflict repaired and packaged — 2026-11-01

Captured _echopy_unavailable reproduced RecursionError in an owned merged
offline facade. It now joins seven prior explicit helper/state names in the
whole-capture rejection check. Six new cases first failed; full source suite
passes302with zero skips. Fresh wheel/sdist each pass222selected tests; older
wheel fails54reserved-name checks and passes the class-member control.

All95runtime files match source/archives/installs;141sdist files pass audited
inclusion/licence/privacy checks.100protected generated files remain unchanged.
Scoped lint/diff and dependency/origin checks pass. Exact evidence and hashes:
verification/issue-123/echopy-merged-reserved-20261101.json. Eight explicit names
are covered, not exhaustive built-in shadowing; low-level renderer still bypasses
whole-capture preflight. Native, downstream integration and publication remain open.

## Echopy helper-name conflicts refused before writes — 2026-11-01

Captured _bind reproduced a broken raw facade: the declaration replaced the
helper and final binding raised NativeUnavailable. Whole-capture generation now
refuses seven explicit helper/state source names, including normalized spellings,
across declarations and inventories. Class-member controls remain allowed.

New tests48failed/1passed before repair; full source296passed/0skipped. Scoped
lint/diff checks pass and100protected generated files remain unchanged. Evidence:
verification/issue-123/echopy-reserved-names-20261101.json. Low-level module_source
still bypasses preflight; other reserved-name interactions are not claimed covered.
Fresh artifact/native/generation acceptance remains open.

## Echopy deletion downstream integration verified — 2026-11-01

Fresh pinned six-wheel cohort passes2436Examples tests with zero skips. Scriptmix
passes4404, with56failures and6skips; failing identities exactly match the alias
cohort. Both disposable consumer worktrees remain clean. All661installed files
match wheels; only Echopy _runtime.py differs from the prior tuple. Dependency
versions remain identical. No new downstream failure was observed.

Evidence: verification/issue-123/cohort-deletion-20261101.json. These source
consumer suites use owned doubles; they do not establish native acceptance.
D27/D31 failures and D29/D30 holds remain. No canonical changes or publication.

## Echopy deletion repair verified in artifacts — 2026-11-01

Fresh wheel and sdist installs each pass167selected tests with zero skips. All95
runtime files match source, archives and installs;140sdist files pass inclusion,
licence/NOTICE, privacy and exact copied-test checks. Dependency and same-process
origin checks pass. Older alias wheel fails10external-deletion cases and passes
10facade-deletion controls. Negative output is isolated from fresh-origin receipts.

Exact archive hashes, commands and limits:
verification/issue-123/echopy-native-deletion-artifacts-20261101.json. Genuine
dirty version remains0.2.4.dev6+ga4f2fbf48.d20261101; hashes distinguish revisions.
The copied native-coverage report is historical fixture data, not a new capture.
Native acceptance, downstream integration and promotion remain open. No live
installation, generated refresh or publication.

## Echopy ordinary native deletion repaired — 2026-11-01

Ordinary native names now use identity entries in the existing alias mapping.
External native deletion no longer exposes stale copied values through the
facade; dir, repeated deletion and rebinding follow the live namespace. Raw and
merged coverage spans classes/functions/attributes/constants/modules.

Baseline227passed; new regressions10failed/10passed before the repair; full
source suite247passed, zero skips. Scoped syntax/import lint and diff check pass;
all100protected generated files remain unchanged. Commands/JUnit/source hashes:
verification/issue-123/echopy-native-deletion-20261101.json. This is uncommitted
source with owned doubles; existing artifacts lack this fix. Fresh artifacts,
native acceptance and promotion remain open under existing holds.

## Echopy alias repair verified in installed artifacts — 2026-11-01

Fresh wheel/sdist each pass147selected tests, zero skips/errors/failures. All95
runtime files match source/archives/installs;140sdist files pass inclusion,
licence/NOTICE, privacy and exact copied-test checks. Both actual installed
fontlab facades pass owned-module alias lifecycle checks. Dependency checks pass.
The older artifact fails41alias cases and passes12controls as expected.

An origin-receipt basename collision from the negative run made the first audit
fail closed. Older origins are preserved separately; a full147test fresh-wheel
recheck restored unambiguous installed origins and final audit passes. This
attempt is retained, not concealed. Same-version archive hashes remain distinct.

Exact commands, logs, hashes, origin correction and limits:
verification/issue-123/echopy-top-level-alias-artifacts-20261101.json. Native
FontLab capture/execution, generated refresh, downstream build and promotion
remain open. No live installation or publication; D29/D30 unchanged.

## Echopy top-level aliases repaired in source — 2026-11-01

Generation now retains keyword/punctuation spellings across classes, functions,
attributes, constants and modules. Explicit protected alias metadata survives
merge; historical class markers remain supported without treating arbitrary
assignments as aliases. Offline annotation-only values remain absent. Runtime
alias reads/writes/deletes route to the original native spelling, following
reassignment, disappearance and later arrival; dir reflects current aliases.

New regressions first yielded38fail/9pass. Initial full suite had2obsolete syntax
assertions (retained); updated marker checks plus historical compatibility cases
pass. Final full source suite227pass, zero skips;65affected checks pass after
import cleanup. One hundred protected generated/support files are unchanged.
Root tested the actual retained fontlab facade's two flObjectsList aliases with
owned native doubles. This is not real FontLab qualification.

Exact commands, hashes, logs, review and limits:
verification/issue-123/echopy-top-level-aliases-20261101.json. Diff check and
explicit E4/E7/E9/F Ruff checks pass; broader inherited lint findings are retained,
not claimed clear. Fresh artifacts, real native execution, generated refresh and
publication remain open. Source candidate is uncommitted; D29/D30 unchanged.

## Echopy generated-name collisions refused before writes — 2026-11-01

Public generate now checks every scope's captured inventory plus declarations
before mkdir/write/stale cleanup. Distinct native names that sanitize to the same
Python identifier raise a specific owner/name error. The existing identity
validator moved to generate and is reused by identities; no duplicate algorithm.

Seven initial failures became green;46targeted and174full tests pass, zero skips.
Tests cover top-level/member/inventory-only collisions, partial inventories,
later-subpackage preservation of existing files and valid cross-scope aliases.
Ruff/diff checks pass. Root reviewed the shared helper and preflight ordering.
The retained identity manifest has0collisions across241049names/1616owners in
17scopes; that is historical manifest evidence, not a fresh native capture.

Exact commands, failed logs, JUnit, source hashes and limits are retained in
verification/issue-123/echopy-name-collisions-20261101.json. Low-level module_source,
identical-name duplicate records and reserved identifiers are unchanged. Existing
artifacts lack the new preflight. Native/generated refresh and publication remain
open; no canonical or live installation changes. Candidate remains uncommitted.

## Echopy static/class constructor bindings repaired — 2026-11-01

Capture now classifies explicit staticmethod/classmethod __init__ descriptors
before bound lookup, retaining their unbound function signature and binding.
Existing generation/merge then preserves decorators and avoids invented self.
Ordinary receiver repair and unknown-descriptor fallback remain unchanged.

Eight owned regression cases cover static/class, direct/inherited, generated/
merged declarations, class/instance access, positional-only arguments, defaults,
docs and None return annotations. No fixture constructor/method was called.
Eight cases failed before the repair;30targeted checks and full166tests pass,
zero skips. Ruff and diff checks pass. Root reviewed the complete source/test diff.
Exact commands, logs, JUnit, references and hashes are in workspace
verification/issue-123/echopy-constructor-bindings-20261101.json.

Candidate remains uncommitted in echopy-receivers-20261101/fontlab-echopy.
Existing artifacts do not contain this repair. Installed artifacts, native
capture, generated refresh and publication remain open under D29/D30; no live
installation changes, canonical edits or native API equivalence claim.

## Echopy receiver spelling preserved in source — 2026-11-01

Capture marks positively identified Python function descriptors, including
constructors, as instance methods. Generation preserves their receiver rather
than inserting self based on its spelling. Existing unknown native-descriptor
fallback and static/class method decorators remain unchanged. Generated API
files were not refreshed; the change is tooling plus owned fixtures only.

Eight added cases first failed, then passed through capture/generation/merge:
ordinary methods and constructors, direct/inherited, class/instance access,
positional-only receivers and keyword-only defaults. No fixture method or
constructor was called. Baseline150passed; final full158passed, zero skips.
Coverage capture85%/generate98%, total94%, zero exclusions. Ruff and diff checks
pass. Official inspect/data-model references and exact commands are recorded in
verification/issue-123/echopy-receivers-20261101.json.

Isolated echopy-receivers-20261101/fontlab-echopy, basea4f2fbf, is uncommitted.
Installed artifacts, fresh native capture, generated refresh, downstream build
and publication remain open. No live FontLab operations or canonical edits.

## 2026-11-01 — Preserve captured method binding

Capture now records positively identified Python staticmethod/classmethod
descriptors and inspects their unbound callable. Generation retains the matching
decorator without inventing a receiver; merge already preserves decorators.
Unclassified native descriptors retain the previous behavior. Existing generated
files are unchanged pending a fresh native capture and reviewed refresh.

Four owned capture/generate/merge regressions failed before the repair; all150
source tests now pass with sibling producer checks present. Controls compare
ordinary, static and class method parameter names, kinds and defaults, including
inherited descriptors and a nonstandard class receiver name. Class and instance
access are checked; an unknown-descriptor control preserves the legacy fallback. No fixture method
is invoked. Ruff passes for both edited modules and the new test.

Commands from this worktree (external evidence ../red.log and ../full-final.log):
- rtk proxy env PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 $FONTLAB_SCRATCH/issue123/echopy-constructors-20261101/fontlab-echopy/.venv/bin/python -B -m pytest -q tests/test_method_bindings.py: before repair exit1 (4failed).
- Same interpreter/environment, python -B -m pytest -q: exit0 (150passed).
- rtk proxy ruff check --no-cache src/fontlab_echopy/tooling/capture.py src/fontlab_echopy/tooling/generate.py tests/test_method_bindings.py: exit0.

Descriptor lookup semantics checked against the official Python3.11 reference:
https://docs.python.org/3.11/library/inspect.html#inspect.getattr_static
This identifies known Python descriptors, not arbitrary PythonQt wrappers.
Native fidelity, downstream documentation rebuild and publication remain open.

# Changelog

## 2026-11-12 — install.vfpy matches the App's installer, with Extensions bundle support (Issue 254)

- `install.vfpy` is now byte-identical to `fontlab-fontlabapp/install.vfpy` (pushed in App `5cac0d6`).
  The new code places `[tool.fontlab-install] extensions` bundles; this repository declares none, so
  installs behave as before. `tools/check_install_copies.py` in the App compares the copies by sha256.

## 2026-11-11 — install.vfpy synced to the App WP11A installer (Issue 250)

- `install.vfpy` is now byte-identical to fontlab-fontlabapp 79f7485 (WP11A): it records file hashes in `install.log`, removes only superseded files whose current hash matches the logged hash, keeps edited ones and reports them, refuses entries with `..` or outside the data folder and any unowned entry in the old RECORD, and supports `FONTLAB_INSTALL_DRY_RUN`. Verify with `tools/check_install_copies.py` in the App repository. The native reinstall check is owner-run and stays open in the App TODO.

## 2026-11-10 — Issue 250 documentation round

- AGENTS.md describes the delegation, integration and release workflow.
- WORK.md reset to the current round; the earlier bytes are archived on the owner's workspace data volume, not public.

## Global Unicode producer refresh — 2026-11-01

Regenerated the13source-derived shims from the reviewed global Unicode producer.
Only the GlyphsApp catalogue identity and application/Glyph Info source hashes
changed from the inherited legacy candidate. Existing GSApplication re-exports
and the Glyphs annotation already expose glyphInfoForUnicode(String, font=None)
and integer name dispatch; no declaration or native binding was invented.

Added21real-export regressions for wrapper spelling, bool/integer subclasses,
override dispatch, exact synthesis spelling, UTF16 refusal, local-font refusal
order, separate legacy encodings and current provenance. The retained stale
catalogue baseline fails; producer paths are scoped and restored. Native capture,
generated reference refresh, promotion and publication remain separate gates.

## 1.1.16 (2026-11-16)

- Preserve receiver order and defaults when a captured method signature uses positional-only parameters. Nine generated-declaration regressions pass; full suite: 109 passed. Current generated declarations are unchanged; native incidence remains unverified.

## 1.1.16 (2026-11-16)

- Regenerated all 13 producer-derived shims from clean Glyport `6d3d3767`,
  Aidus Code `32523d41` and the supporting App `ccc8314e` sources. All generated
  declarations and provenance remain byte-identical; no generator change needed.
- Baseline and final full suites each pass 100 tests with sibling producers
  present. Before/after producer heads, status and tracked-file hashes match.
- Updated the remaining plan: downstream docs integration and applicable native
  acceptance remain pending. `fontlabapp_shim` and native capture are unchanged.

## 1.1.16 (2026-11-16)

- Shims regenerated from glyport d4d1a96 (issue-122 head; imports fontlabapp 29f4f6e)
  and fontlab-aidus-code: 8 files. New constant `GlyphsApp.LTR = 0`; every other change is
  `_shim.json` source-hash provenance for edited glyport files. Shim set unchanged;
  `aidus_code_tools` unchanged.
- `test_glyport_shims_when_generated_then_match_session_providers` now allows glyport's
  deliberate legacy RoboFab providers (`robofab` … `robofab.interface.all.dialogs`, glyport
  7239e44): they must expose only `AskString`. Any other unshimmed provider must still
  refuse with UnsupportedCapability.

## Issue 106 — completed (lane C3, 2026-10-16)

- [x] Shim classes declare their public members (generator v2: methods, class/static
  methods, properties with setters, attributes; signatures only) with an independent
  member- and class-coverage test (0d48b79, b60b261). X4b findings; X4e and X4f APPROVE.
- [x] Facades read export names lazily from `_shim.json` (generator v3, 3db4bc9): constant
  size as glyport grows (largest facade 1,020 bytes); wheel ships every `_shim.json`.
- [x] Shims regenerated from merged glyport cb611bd (d5c0ba3); unshimmed providers
  (`vanilla.test`) must refuse with UnsupportedCapability. X4f APPROVE (30 files byte-for-byte).
- [x] Downstream docs consolidated rebuild against these shims: final-10, all 16 gates exit 0
  (workspace `verification/issue-106/evidence/C3/final-10/`).

## v0.2.2 (2026-10-16)

Shims regenerated from glyport v1.0.1 and fontlab-aidus-code v0.2.1 (issue 106, lane C3).


- Shims regenerated from glyport v1.0.1 (a81c6f5) and fontlab-aidus-code v0.2.1 (dbd2832): 15 files, no new modules, byte-identical across hash seeds, no local paths (5ce61bf, lane C3).

## v0.2.1 (2026-10-16)

Generator v3 lazy shims (Glyphs, Cocoa/vanilla, Aidus, Fontlabapp facades) regenerated from glyport cb611bd, class coverage checks, standalone-safe tests, docs and audit fixes (issues 101/104/106). Reviews X4e/X4f/X4o APPROVE; release review X5 + X6 fix APPROVE.

Issue 106 release gate (X6):

- Skip the shim class coverage integration check when producer checkouts are
  absent, matching the other producer checks. A standalone shim-suite regression
  keeps the test extra and source distribution independent of Glyport.

## Issue 104 — completed (lane L5, 2026-10-15)

- [x] Capture identity manifest `_identities.json` (every captured identity,
  1,216 native spellings, extensions, merge/enrichment gaps, capture hash),
  shipped in the wheel; `identities` / `verify-identities` commands (R014).
- [x] Every captured symbol, member and alias accounted for in the rebuilt docs
  coverage report: 242,654/242,654 documented, 0 unexplained (R014, G03, G09).
- [x] Static shims: `fontlabapp_shim` (lane L6), and generated from glyport's
  `FontLabSession.adapters()` and the Aidus executor: `GlyphsApp`,
  `GlyphsApp.plugins`, `vanilla`, `vanilla.dialogs`, `AppKit`, `Cocoa`,
  `Foundation`, `objc`, `aidus_code_tools`; regenerated after the L2/L3 merge.
- [x] Review rounds R-L5-echopy, RR-echopy, RR2-echopy fixed test-first; R046
  `docs` extra.
- [x] P11 native check of the built wheel (ab88b0d) inside FontLab: identity,
  constructors, conversion, return types, properties, extensions, full native
  name coverage; every facade/shim import ≤ 1.6 ms (budget 5 s); fontlabapp
  names resolve live; static shims raise AttributeError; Aidus tools give the
  install hint when fontlab-aidus-code is absent. Receipt:
  `verification/issue-101-ecosystem/evidence/docs-104/native-p11/`.

## v0.2.3 (2026-10-16)

- Shims regenerated from glyport v1.0.2 (0f85ada) and Aidus Code v0.2.1: new exports GlyphsApp MIXEDSTATE/OFFSTATE/ONSTATE/WOFF/WOFF2, AppKit/Cocoa/Foundation NSFloatingWindowLevel/NSNormalWindowLevel, objc.signature (11 files, no new modules; byte-identical regeneration).
 — issue 104 review fixes (R-L5-echopy)

- Glyport shims are generated from `FontLabSession.adapters()` (the runtime
  providers), adding `GlyphsApp.plugins`, `vanilla.dialogs` and the Qt-backed
  Cocoa/objc names (`IBOutlet`, `IBAction`, `lookUpClass`, drawing, menus).
- `docnames` exports re-exported names listed in a shim's `__all__`.
- `generate` records the capture identity; `merge` carries it into provenance
  and removes a manifest that may describe another capture.
- Identity derivation falls back to declaration collections when a capture has
  no `names` arrays.
- Shim stubs bind every imported name once (RR-echopy): exports own their
  names, annotation-only types get private aliases, duplicate exports fail, and
  the typing header skips names a module exports (vanilla `List`).
- RR2-echopy: every module-level binding kind (imports, classes, constants,
  functions, aliases, typing helpers) is reserved; type-only imports that would
  rebind one get a private alias, and repeated entry names fail generation.
- `docs` extra declares Griffe for documentation builds (R046).

## 1.1.16 (2026-11-16)

- `fontlabapp_shim` (from fontlab-fontlabapp 9cbaf69, capture 68353ad1),
  `GlyphsApp`, `vanilla`, `AppKit`, `Cocoa`, `Foundation`, `objc` and
  `aidus_code_tools` shims; `fontlab-echopy shims` generator (glyport
  issue-101-ecosystem 8a70179, aidus-code 9c31ac7).
- `docnames` exports documentation namespaces for packages marked `_shim.json`.

## 1.1.16 (2026-11-16)

- `_identities.json` ships in the package: every captured identity, its source
  identity, 1,216 native spellings of sanitized names, maintained extensions,
  merge and enrichment gaps, pinned to capture `5a405eb5…`.
- New `identities` and `verify-identities` commands; the pipeline writes the
  manifest after merge. Derivation rejects a different capture and source-name
  collisions, and never rewrites the sidecars.

## 2026-10-15 — completed checklist (moved from TODO.md)

- Preserve source and license provenance with a migration manifest.
- Capture native APIs and every PythonQt child without invocation or limits.
- Implement capture/generate/enrich/merge/pipeline CLI commands.
- Generate explicit annotations and native-identity-preserving facades.
- Keep manual patches and upstream enrichment independent of regeneration.
- Fetch PySide2 wheel and official Qt5 docs; report coverage and gaps.
- Verify complete deterministic regeneration and source name coverage.
- Build and clean-install wheel and sdist; audit distributed contents.
- Verify installed artifact against the running FontLab host.
- Record iteration 1 evidence and commit the migration.

## 1.1.16 (2026-11-16)

- Preserve upstream reference overloads as separate fenced Python source lines
  when enriching captured native documentation. Native declarations are unchanged.

## Expanded ecosystem — unreleased

- Fresh capture runs inside FontLab before source generation and enrichment.
- Preserve structured Qt prose, code examples, lists, tables and absolute source
  links in readable Python docstrings; retain captured native documentation.
- Export deterministic source-only documentation aliases under actual native
  names, with source/output hashes and no copied declarations.
- Preserve BoolResult's captured class and constructor when Griffe would
  otherwise shadow it with an empty pseudo-namespace.
- Pipeline can persist the enrichment overlay and current verification reports,
  keeping regeneration inputs and documentation coverage synchronized.

## 1.1.16 (2026-11-16)

- Migrated code-shadow source, generators, extension inputs and RST documents
  with original licenses, source revision and file hashes.
- Added hatch-vcs packaging for fontlab_echopy and canonical echopy aliases.
- Replaced object proxies with native-identity-preserving namespace delegation.
- Added complete native metadata capture, deterministic annotated generation,
  independent JSON enrichments and merged installable source.
- Added checked PySide2 wheel extraction, official Qt5 class/member parsing,
  native-name intersection and explicit coverage/absence reports.
- Added native-compatible extension helpers and explicit immutable-class status.
- Added fixture, boundary, source compilation and native smoke checks.

- Verified every captured namespace/class member declaration; 21 tests passed.
- Verified deterministic regeneration and 1,434 original archive file hashes.
- Built and clean-installed wheel and sdist; audited distribution contents.
- Verified native constructors, argument conversion, return types, properties,
  class identity, extension helpers and complete present namespace coverage.
- Fixed eager compatibility alias imports and checked cold native imports under
  FontLab's five-second execution deadline.
- Reject automatic capture outside FontLab before replacing generated outputs.
- Propagate host introspection deadlines; repair a recorded QOpenGLTexture.bind
  capture gap through bounded native re-inspection and regenerate source.
- Separate complete canonical .pyi documentation from small runtime facades;
  native imports avoid compilation of large documentation sources. Offline
  operations still raise clearly. Verify public source resolution with Griffe.

- Execute maintained extension patch bodies through a generated registry, with
  explicit installation and callable fallbacks for immutable native classes.
- Preserve captured constructor, base and descriptor documentation alongside
  enrichment; correct manual examples against actual native members.
- Preserve offline PythonQt.BoolResult class identity on child-module imports.
- Verify a fresh uninterrupted capture in FontLab without nested inspection gaps.

## v0.2.0 publication verified

Actual publication and independent downloaded-asset verification complete.
Three full-project iterations pass; installed tagged wheel/sdist each457tests.
Downloaded native smoke covers all eight packages and both formats, including
production ACP/native UI and TypeRig composition. Exact release URLs, immutable
code commit and asset digests are in RELEASE.md. This follow-up changes only
completion evidence; release code and tag are unchanged.

## 2026-10-15 — merged Glyport shim refresh

- Include GlyphsApp.UI and current Cocoa/Vanilla/Glyphs exports from the real
  merged FontLabSession providers. Resolve provider dependencies inside their
  scoped ExecutionContext and keep facade imports lazy.
- Compact generated name tables to retain the existing4KiB facade limit.
- Fresh regression89passed after the retained stale-output and facade-size
  failures. Downstream docs rebuild and final artifacts remain tracked in PLAN.

## 2026-11-01 — quoted native defaults

Mask complete quoted literals with equal-length spaces only while locating
parameter separators, brackets and trailing prose. Original signature bytes
supply the emitted defaults. Shared native type-template splitting retains its
existing behavior; uncertain/malformed signatures still fall back conservatively.
Python3.11 re.finditer/sub semantics consulted at https://docs.python.org/3.11/library/re.html.
No new runtime dependency; no generated facade/sidecar edited.

Baseline109tests passed with sibling producers present. Initial25case regression:
21failed4passed. Final27cases against old converter in isolated tests:
23failed4passed; a prior PYTHONPATH-only comparison was overridden by project
pytest pythonpath and is not old-code evidence. Final full136passed; scoped
42tests give whole signatures.py91%coverage. Initial coverage commands failed
because autoload disabled and pytest-cov absent; explicit ephemeral plugin works.
Scoped independent review approved; its27focused tests and additional2000
synthetic conversions found no blocker.

Retained-doc audit reconverts144397unambiguous doc signatures across17raw
Python files with old/new converters: zero changes. This does not cover original
capture signature fields or a fresh host. Current generated bytes are unchanged.

Commands through rtk proxy, candidate cwd unless noted:
- env UV_CACHE_DIR=$FONTLAB_SCRATCH/uv-cache TMPDIR=$FONTLAB_SCRATCH/tmp UV_PYTHON=/opt/homebrew/bin/python3.11 PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 PYTHONPATH=../fontlab-fontlabapp/src ./test.sh: baseline/final exit0.
- .venv/bin/python -m pytest -q tests/test_quoted_signatures.py with bytecode/autoload disabled: red exit1, initial repaired25passed exit0.
- uv run --with pytest-cov --extra test python -m pytest -p pytest_cov -q tests/test_quoted_signatures.py tests/test_positional_signatures.py tests/test_pipeline.py --cov=fontlab_echopy.tooling.signatures --cov-branch --cov-report=term-missing with same bytecode/autoload/external-cache environment: exit0,42passed.
Evidence: external issue123/echopy-quoted-defaults-20261101/.

Wait, but: no native capture, binding acceptance, canonical promotion or docs
publication follows from generator tests or retained-data reconversion.

## 2026-11-01 — Preserve captured constructor metadata

Generation previously discarded capture.namespace's constructors records. Reuse
the shared signature conversion for one captured record, preserving documentation,
receiver spelling and None return. Multiple records retain every signature/doc
under an explicitly variadic declaration; absent records retain the legacy output.
No constructor invocation or native behavior is inferred. No dependencies changed.

Nine new regressions include capture/generate/merge, positional and keyword-only
arguments/defaults, absent metadata, capture-input preservation and ambiguous
overload docs. Initial6cases failed; first implementation exposed the dunder-name
normalizer; an additional ambiguous-doc control failed before explicit variadic
handling. Failed receipts retained under external issue123/echopy-constructors-20261101.

Prepared-environment final command: `rtk proxy sh -c 'PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
COVERAGE_FILE=$FONTLAB_SCRATCH/issue123/echopy-constructors-20261101/module.coverage
.venv/bin/python -B -m pytest -q -p pytest_cov --cov=fontlab_echopy.tooling.generate
--cov-branch --cov-report=term-missing
--cov-report=json:$FONTLAB_SCRATCH/issue123/echopy-constructors-20261101/coverage.json'`
exit0:145passed; generation module96%combined coverage, no exclusions. Producer
checks included, using retained producer paths and genuine App159 wheel. Earlier
no-project runs lacked installed Echopy for subprocesses, and first project run
lacked App for producer imports; those failed receipts are preserved.
Scoped Ruff0.14.10 F821/F401 and git diff --check exit0. Independent bounded review
approved; subsequent tests added absent-record and input-immutability assertions.

Current generated declarations and retained captures remain unchanged: no fresh
native capture was authorized under D30. This verifies tooling and owned fixtures,
not current FontLab constructors or downstream generated-site acceptance.

## 2026-11-01 — Consolidate the final candidate

Merged the retained candidate into the consolidated branch, preserving the newer
branch changes. Verification from the workspace root:
`rtk proxy sh .metaswarm/quality.sh coverage "$CHECKOUT" fontlab-echopy`
(`CHECKOUT` is this isolated checkout): 325 passed, all five changed runtime modules above 80% combined coverage; exit 0.
Regenerated source-derived shims from the merged Glyport and Aidus producers;
native captures and generated native facades are unchanged.
No native FontLab operation was run.

## 2026-11-06 — Private documentation candidate

Added the product-specific light ProperDocs/MaterialX source/generated site and every-main source/output qualification workflow without private Pages operations. Runtime products and native acceptance are unchanged.


## 2026-11-07 — Exact frontend notices and English search assets

Added exact upstream frontend notices and source-map provenance for the existing MaterialX 10.1.8 payload. Explicit English configuration and a small build hook reject language, corpus, reference, asset-set or hash drift before omitting the 35 unused language helpers. All nine retained core assets, original product legal files, guides, catalogue rows, media, runtime and dependency/build locks are preserved.

The strict site build and all 35 documentation tests pass. The complete new hook has 100% statement/branch coverage; real Git staging, checkout and archives preserve exact legal bytes. An independently installed matching lock reproduces all 55 output bytes and modes. Existing immutable source/output, epoch, concurrency and full-parity workflow checks remain active. Browser and independent review evidence are separate from these local checks.

Private Pages configuration, grants, requests and publication remain owner-held; this source follow-up adds none.
No product release or installation is claimed. Prior ordinary artifacts remain bound to their recorded revisions; a later Git revision changes genuine hatch-vcs metadata. Full current source archives include these documentation additions; no unchanged-sdist or whole-wheel identity is asserted. Native acceptance and owner installation remain separate.


## 2026-11-07 — installed icon path-tuple inventory refinement

The current HTML/CSS contains 45 distinct ordered SVG path tuples. A complete scan of the four installed MaterialX icon families finds 43 exact installed matches and two unmatched Lucide tuples, refining the earlier known-candidate inventory. The additional installed match is the Font Awesome version caret-down. Its existing CSS header and full notice retain Font Awesome Free 7.1.0, Fonticons and CC-BY-4.0 icon attribution. The official NPM caret SVG has different raw path bytes; no unmodified-primary SVG, whole-geometry or optimizer-recipe equivalence is claimed. The two unmatched Lucide tuples retain their pinned SCSS source attribution.

A new actual-output regression derives these counts and checks installed matches, unmatched CSS references and the caret header. It fails against the prior 42 count and passes with the corrected metadata. All 36 current documentation tests pass; full strict and independent exact-lock builds match every output byte and mode. Only the legal paragraph, corresponding inventory and legal search row change in the site. Runtime, packaging, generators, vendor assets, full notices, existing guidance and the Fly search fix remain exact. Fresh browser verification and independent review are recorded separately. No private Pages operation, delivery, installed-product upgrade or native acceptance is claimed.


## 2026-11-07 — Release-note attribution correction

Removed the Pythonqtside-only relocation and sdist sentence from the Task11 documentation entry. All history before that entry remains byte-exact. The existing documentation checks and normal installed pre-push gate pass; WORK.md records their scope and limits.
