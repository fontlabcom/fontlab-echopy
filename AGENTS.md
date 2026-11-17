---
this_file: AGENTS.md
---

## Owner priority: functional progress first (2026-11-15)

Future agents must make large, swift advances in working functionality. Prioritize visible user problems and useful, coherent feature increments. This instruction sets the work order and supersedes older requirements to complete exhaustive testing or build test infrastructure before ordinary implementation.

Keep packages coherent and compatible. Check shared APIs, imports and lazy aliases, data formats, dependency direction, object ownership and lifetime, installers, launchers and examples. Update affected providers and consumers together; preserve existing supported behavior and avoid dependency cycles.

During implementation, use the smallest meaningful smoke checks and focused regression tests for the changed behavior and affected package boundaries. Detailed testing, exhaustive coverage, broad performance studies and full acceptance matrices can follow in a later testing pass. Do not let test harnesses, sandbox/supervisor design, repeated unchanged suites, evidence machinery or review paperwork become the main project. Build such infrastructure only when a concrete functional defect or necessary safety constraint requires it.

Record deferred checks and known limits plainly. Do not call untested native, installed or published behavior verified. Keep existing mandatory delivery hooks, preservation rules, licence/privacy obligations, repository exclusions and explicit native/publication holds intact. When one action is held, continue other authorized functional work instead of expanding unrelated infrastructure.

Choose the next substantial useful feature or shared fix and carry its affected providers and consumers together. Timebox supporting investigation; once focused checks establish a usable increment, continue functionality work. Queue detailed testing for a later pass with its concrete remaining checks instead of letting test infrastructure displace product delivery.

## Current scope — 2026-11-05

Issue 230 documentation reconciliation is current. Issue 123 remains paused. The qualified Issue 207 isolated candidate is separate from canonical source, installed artifacts, native acceptance and publication. Reconcile that candidate with later work before integration. Issue 210 specifies future architecture; Issue 211 retains unfinished follow-up checks. Retained dated receipts describe their original source and acceptance surface only.

Remote source inspected for this variant: `48e39a8a5758783980400d99d576ec77dced7b0e`. This is a dated source observation, not an installed or native acceptance claim.

Reconcile the Issue 207 enriched candidate and its five catalogues with current producers before a reviewed regeneration.

Qualify exact captures, aliases, docstrings, identities/provenance and ordinary installed consumers; document absent native APIs without inventing support.

## Organization and checks

`src/` contains runtime routing and tooling; `generated/` contains raw declarations. `patches/`, `enrichment/` and `reports/` hold maintained overlays, inputs and reports. `tests/` checks source contracts.

Run `uv sync --extra test --extra enrich`, then `./test.sh`. The wrapper runs `uv run --extra test python -m pytest -q`. Build artifacts with `uv build`; capture requires a separate owned-host session.

The default source suite includes a fast real-sdist input payload check using the shared build fixture. From a checkout, packaging changes and releases additionally require `uv run --extra test python -m pytest -q tests_artifacts/test_sdist.py`; this separate gate builds an sdist and runs every shipped source test from its extracted inputs. Run both commands. The full artifact gate stays outside default test discovery to keep routine source tests quick.

# Agent guidance: fontlab-echopy

## Owner priority: functional progress first (2026-11-15)

Future agents must make large, swift advances in working functionality. Prioritize visible user problems and useful, coherent feature increments. This instruction sets the work order and supersedes older requirements to complete exhaustive testing or build test infrastructure before ordinary implementation.

Keep packages coherent and compatible. Check shared APIs, imports and lazy aliases, data formats, dependency direction, object ownership and lifetime, installers, launchers and examples. Update affected providers and consumers together; preserve existing supported behavior and avoid dependency cycles.

During implementation, use the smallest meaningful smoke checks and focused regression tests for the changed behavior and affected package boundaries. Detailed testing, exhaustive coverage, broad performance studies and full acceptance matrices can follow in a later testing pass. Do not let test harnesses, sandbox/supervisor design, repeated unchanged suites, evidence machinery or review paperwork become the main project. Build such infrastructure only when a concrete functional defect or necessary safety constraint requires it.

Record deferred checks and known limits plainly. Do not call untested native, installed or published behavior verified. Keep existing mandatory delivery hooks, preservation rules, licence/privacy obligations, repository exclusions and explicit native/publication holds intact. When one action is held, continue other authorized functional work instead of expanding unrelated infrastructure.

Choose the next substantial useful feature or shared fix and carry its affected providers and consumers together. Timebox supporting investigation; once focused checks establish a usable increment, continue functionality work. Queue detailed testing for a later pass with its concrete remaining checks instead of letting test infrastructure displace product delivery.


## Live font testing in FontLab (owner instruction, 2026-11-10)

Test, verify and edit in the font that is open in FontLab 9. Don't hold back
because the owner might be working on it. Just work in it. If no font is open,
open a VFJ from `~/Desktop` first (File > Open, or `fontlab.flPackage(path)`
and `flWorkspace.instance().addPackage`). Those VFJs are for agents. Add glyphs,
kerning pairs, elements, contours, masters or anything else the test needs,
and save the files when that helps. This replaces older rules that required an
empty FontLab session or forbade editing open fonts. `fl-native.sh --mutating`
now runs with fonts open (`FL_REQUIRE_EMPTY=1` restores the old check). The
serialized lock still applies: one native run at a time. Don't quit or restart
FontLab, and don't close fonts from Python, because that has crashed the host.

Source-readable facades (`.py` + `.pyi` sidecars) for FontLab's native modules, from which fontlab-python-docs is built. Read the workspace AGENTS.md and DECISIONS.md first; this file adds repo rules only.

## Layout and ownership

- `generated/`: raw output of `fontlab-echopy generate`. `src/fontlab_echopy/` (and `src/echopy/`): merged output. Never hand-edit either; change `patches/manual.json` or the tooling, then regenerate. Manual overlays beat upstream enrichment. Merge with the four overlays in README order (qt5, fontlab-proteus, fontpr-mcp, manual); after merge restore `_identities.json` from git and keep `capture_identity` in `_provenance.json` unless a new capture is in hand. Rebuild the reference overlays with `proteus-docs`/`mcp-docs` from `vendor/` (local links, not committed) and `llms` after a merge.
- `enrichment/qt5.json`, `reports/`, `_provenance.json`, `_identities.json`: regenerated artifacts; keep them in step with the code that produced them.
- `legacy/` and `MIGRATION.json` are hash-recorded archives. Leave unchanged.
- Scope (issue 201): shim only the native bindings `fontlab`, `fontgate`, `fontpr`, `FL` (captured declarations; full pipeline provenance qualification remains separate) and `PythonQt.*`. Do not add emulations of other APIs here: Glyphs/Cocoa/vanilla belong to fontlab-glyport, `fontlabapp_shim` to fontlab-fontlabapp, `aidus_code_tools` to fontlab-aidus-code. `fontlab_echopy.MOVED` makes those names raise `ImportError` with the new home.

## Commands

- Tests: `./test.sh` (= `uv run --extra test python -m pytest -q`). Generation deps: `uv sync --extra test --extra enrich`. Build: `uv build`.
- Python 3.11, arm64 (`cpython-3.11-macos-aarch64-none`; check with `lipo -archs`).

## Host rules that apply here

- `run_python` has a fixed 5 s deadline. Keep `.py` facades tiny and lazy; full declarations stay in `.pyi` (RULINGS.md ruling 5). Capture large namespaces in bounded calls, not one MCP call.
- Captures are API-only. Never read property values generically: `QSvgRenderer.currentFrame` on an empty renderer segfaults FontLab. Use class-level lookup or `indexOfProperty`.
- Never read `flPackage.fgPackage` on an unregistered package (raises once, then segfaults).
- PythonQt has no `QtWidgets`; widgets are in `PythonQt.QtGui`. Never construct a `QApplication` or load PySide2/PyQt/Qt 6 binaries in the host. PySide2 wheels are reference metadata only.
- `fontlabpr` does not exist in FontLab (Issue 257: no registration in the FontLab source; the shim was removed). Do not re-add it or invent its API (DECISIONS.md D8).
- `flLayer.isMasterLayer`/`isMaskLayer`/`isService` are boolean properties on 9784, not methods (older declarations say otherwise). Recheck against the actual build before overlaying; do not generalize older measurements.
- Do not mutate user-open fonts, preferences or the Output panel during capture. Native checks use owned fixtures through `verification/issue-104/fl-native.sh`.

## Proof and git

- Offline tests, imports and `.pyi` checks are not native proof. Run the installed wheel inside FontLab through Remopy (`examples/native_smoke.py`).
- The canonical checkout is editable-installed into the owner's FontLab: preserve it and use an isolated successor for the current task. Do not move or re-create `v0.2.*` tags; releases are the controller's.

## Milestones and delivery

Read [PLAN.md](PLAN.md), [TODO.md](TODO.md) and [WORK.md](WORK.md) before work.
Make the smallest complete MVP for one named acceptance task. Find all callers,
tests, fixtures, exports and documentation first. Use graph impact before source
symbol edits; confirm stale or unknown graph results against current source.
Keep product work in isolated successors and preserve the owner's checkout.

Run this repository's exact checks and the unchanged 80% gate for each complete
changed production module. Use an independent review before a milestone commit.
Under the current owner task, commit and push reviewed, passing milestones;
verify remote heads rather than inferring delivery from local tracking refs.
Before main integration, reconcile concurrent work and all consumers, run graph
change analysis and repeat the required acceptance on the combined source.

Before removing obsolete branches or files, prove integration, retain recoverable
unique work and check fresh owner/worktree attachments. Preserve sealed reports,
licences, archives and private data. Do not rewrite history by implication.
Remove verified completed work from PLAN/TODO and record scoped evidence in
CHANGELOG. Keep implemented-only native/artifact checks open in TODO. Issue 123
remains paused; no instruction here authorizes driving the owner's FontLab,
installing into its user folder or publishing a site.

## Archive preservation in this delivery

This remote branch retains `legacy/README.md`, `legacy/source.tar.gz` and
`licenses/aidus-legacy-LICENSE` byte-for-byte. A later canonical cleanup does
not delete them here. The source/runtime/tooling matches that canonical checkpoint.
No generation, native capture, package release or archive removal is part of this variant.

Qualified integration targets `main`. Refresh actual remote refs first.
Keep the installed pre-push gate active. Stage only reviewed guide bytes after
preimage checks, then run graph change analysis before committing.

## Private source/build-only documentation

Author pages under `src_docs/md` and use the separate hash-locked docs environment with `sh src_docs/build.sh`. Generated `docs` is immutable output. The main workflow qualifies direct source/output lineage and full ignored-output parity. Twelve private P/L operations remain owner-held; no Pages request or permission belongs here. Preserve runtime sources and native boundaries.

## Integration rounds

After each round of important changes, integrate it into `main` and upstream:
fetch `origin/main`, build the change on top of it in an isolated branch or
worktree, and resolve conflicts by keeping both our work and teammates' work.
Never discard upstream commits, and never force-push. Run the repository's
checks on the merged result, then push to `origin main`. Record the change in
CHANGELOG.md, move verified-solved TODO.md items into CHANGELOG.md, update
PLAN.md, and continue with the next TODO.md item until the list is clear.
`install.vfpy` is shared: keep it byte-identical in every installer repository.

## Isolated successors

Overrides generic bootstrap/MCP.

For graph work in an isolated successor, use the qualified installed CLI or backend with both `GITNEXUS_HOME` and `GITNEXUS_STORAGE_PATH` set to separate task-owned locations before the first invocation, including index discovery and analysis. A private storage path alone can still register the successor in global control files. During ordinary analysis, do not fall back to global MCP defaults, global `list-repos` or global setup/bootstrap, and do not make unreviewed global registry edits. Retain exact command/selected environment and before/after owned metadata; record expected task-owned `.git/info/exclude` additions and preserve unrelated state. If discovery or indexing escapes the owned scope, preserve evidence and obtain independent bounded control-file review before integration. Any necessary recovery must be separately reviewed, use fresh guarded current bytes and reviewed writer coordination, and change only the proven task-owned entry while preserving all other current records and bytes; never restore an old whole global registry.

## Agent workflow (Issue 250, 2026-11-10)

- Plan with `superpowers:subagent-driven-development`: one fresh implementer per task, a separate read-only reviewer, then the controller runs the gates and commits.
- Send bulk, well-specified work to Codex via the `codex-delegate` skill (`node ~/.agents/skills/codex-delegate/scripts/relay.mjs --brief BRIEF --cd WORKTREE`, in the background). Use `claude-delegate` or `cursor-delegate` for second opinions or independent lanes. Delegates never commit, push or tag.
- Work in a fresh worktree of `origin/main` on the workspace data volume; never pull, switch or reset the owner checkout. Merge `origin/main` again before pushing, keep both sides' CHANGELOG/PLAN/TODO entries, rerun the full suite, lint and graph change analysis, push through the pre-push hook where one is installed (never force), verify the remote SHA and the CI run where a workflow is configured. Held private Pages operations (workspace D41) stay held.
- Release: tag the next semver above the latest tag and publish a GitHub release. Install released, gated packages into `~/Library/Application Support/FontLab/FontLab 9/` and test live in FontLab 9. This owner route (Issue 250) supersedes, for released packages only, every older line in this guide that forbids installing into the FontLab user folder or its site-packages, owner-managed editable installs, or starting FontLab for a live test (the owner's canonical editable checkouts themselves stay owner-managed): record the previous installed distribution first so it can be restored, and never touch FontLab preferences (owner fonts and documents: see live font editing below); native work goes through the workspace `verification/issue-104/fl-native.sh` gate.
- Documents: CHANGELOG holds verified completed work; TODO only open or to-verify items; PLAN the major remaining changes; WORK.md the current round only (older WORK bytes are archived on the owner's workspace data volume, not public).
- Native defects: issues at github.com/fontlab/fl; fixes as pull requests to fontlab/Proteus, fontlab/FontGate or fontlab/pyfontgate. Never commit to the local C++ snapshot.
- Older "work directly" or "no delegation" lines in this guide are superseded by this section (Issue 250).
- Live font editing (owner, 2026-11-10; workspace D44): test, verify and edit the font open in FontLab 9, and do not stop because the owner might be working in it. Open a VFJ from `~/Desktop` first (those files are for agents), then add glyphs, kerning pairs, elements, contours, masters or whatever the test needs, and save them freely. This supersedes, for live testing, every older line here that forbids mutating owner fonts or documents or requires owned fixtures only. FontLab preferences, Output folders and global update queues stay untouched. Keep the serialized host lock (`fl-native.sh`, one native run at a time; `--mutating` now allows open fonts); do not quit or restart FontLab and do not close fonts from Python, which has crashed the host.
