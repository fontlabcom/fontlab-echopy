---
this_file: PLAN.md
---

## FontLab 9.1 API promotion — 2026-11-16

`fontlab_echopy.api91` records the 9.1.9812 changes from source. Next: capture 9.1 in FontLab, regenerate and refresh provenance, move the records into the generated stubs and manual class guidance, and keep `api91` as the version-change record with its QByteArray guard. Member presence, `fgBrush.size` absence and the QByteArray wrap round trip are verified live on 9.1.9812; live-verify the behavior of each record (`penParameters` writes, `expandStroke`, `makeStroke`, presentation overrides) before promotion.


## Shared installer: remaining delivery qualification — 2026-11-15

Review the exact shared-installer candidate against fresh main, run the required combined package gates, and qualify genuine release/archive/download inputs. Preserve the existing package-specific dependency and distribution contracts. Then qualify the coherent provider/consumer and Script/Extension cohort through the admitted root installer and native lane; source checks do not establish those outcomes. Keep every existing ownership, native, publication and paused-work limit.



## Sdist test-input qualification — 2026-11-14

Source tests and archive inputs are recorded in CHANGELOG; native capture, provenance, installer and full-provider acceptance remain separate. Diagnose the existing docs filename-only diff failure with refresh disabled, retaining full output bytes/modes. Review the existing expanded Ruff findings without changing source or lint policy merely to obtain green.

# Forward plan

## Functional work order — 2026-11-14

Prioritize missing maintained guidance and concrete capture or routing defects using captured declarations and existing overlays. Keep generated namespaces, aliases, identities and provenance synchronized with pythonqtside and Fly consumers; do not invent absent native APIs.

Use small smoke checks and focused regressions for changed behavior and package boundaries. Keep the existing detailed acceptance tasks for a later testing pass; mandatory delivery hooks and current holds remain in force.

Issue 230 reconciliation is current. Issue 123 implementation remains paused; its acceptance backlog below is preserved, not resumed. Keep qualified Issue 207 candidates distinct from canonical source, ordinary installed artifacts, native acceptance and publication. Issue 210 defines the future plugin split; Issue 211 retains follow-up checks. The owner corrected the preparation catalogue reference to Issue 214.

## Current enrichment and capture

Fold the separately captured FL declarations into the next full pipeline so `_identities.json`, `_provenance.json` and `reports/` cover them. Consume the six C14 evidence-backed `fontlab` and `fontgate` manual class overlays in the next reviewed regeneration, then qualify installed documentation and native behavior. Additional enrichment must retain captured-source citations. Keep Qt5 enrichment distinct from absent `fontlabpr` and unsupported host Qt6. Never invent emulation APIs for bindings that the host does not ship.

Qualify decorator isolation, collision preflight, top-level aliases, receiver names and static/class constructor binding in a fresh owned native capture and generated refresh. Preserve missing offline values and unknown binding classifications. Cover top-level and member collisions, later-scope failure preservation, valid aliases, reserved identifiers and duplicate records as separate contracts. Forward sanitized live reads/writes/deletes to their original spelling. Source and selected installed tests are not native proof.

Qualify the source-reconciled text-signature provenance, distinct allocation
constructor/MRO evidence and required Qt seed diagnostics in that same future
owned native capture and reviewed generated refresh. Preserve unresolved evidence
and separate constructor roles; ordinary fake-host checks do not close this gate.

## Producer and installed-cohort acceptance

Reconcile the latest reviewed namespace/discovery and manager-state source with current Glyport/App/Aidus producers before choosing one exact source tuple. The dated 325/329/350/356/370/424/433/451/495/546/577/600 test stages are distinct receipts in CHANGELOG/WORK; do not rerun an earlier implementation plan or combine their counts as current acceptance.

Build genuine committed wheel/complete-sdist artifacts; reproduce the wheel from the sdist. Assert installed origins, all catalogue/source hashes and protected declaration/manual/enrichment/legacy bytes. Qualify both ordinary provider/consumer/authored-example tuples. Keep current FontLab fontType/file observers, default/private resources, Foundation/CF/CG/CT ABI and complete original workflows separate from owned source fixtures.

First qualify the tooling in the chosen producer tuple. The historical 13-target
producer-shim route belongs to retained pre-Issue 201 cohorts. For example, the
2026-11-02 manager-state receipt used Glyport `5e04d1168` and recorded 577 source
tests with zero skips. It does not describe the current CLI.

Issue 201 removed `tooling/shims.py` and the `shims` command. The current parser
registers `capture`, `generate`, `enrich`, `merge`, `docnames`, `identities`,
`verify-identities` and `pipeline`. It accepts no `--source` producer argument.
Before a producer refresh, recover and review the exact historical tooling/cohort
or select and qualify the maintained producer tool. Reconcile moved package
layouts and all consumers first. Do not hand-edit generated facades or replace an
unavailable historical capture with a newer hash.

Current `fontlab-echopy docnames OUTPUT` exports native-named documentation aliases
from enriched Echopy source. It does not generate the moved producer shims.
The current native metadata pipeline accepts `--capture FILE` for an existing
approved capture, with required `--raw DIR` and `--output DIR`. Omitting `--capture`
attempts native capture. Use an explicit approved capture for offline work and
retain D29/D30 before any native or generated refresh. Follow README Regeneration
for the supported pipeline options and output identities.

Historical App refresh used `fontlabapp.shimgen` with a real capture. Verify the
command's availability and qualify its replacement or recovery against the chosen
App source before use. Historical availability is not current producer qualification. Keep source, artifact, generated and native gates separate.

## Downstream documentation and delivery

Verify Docs renders Glyport, App and Aidus from their current homes. Then perform the reviewed short rebuild, source-lock/generated reference, routes/archive, browser/accessibility and publication checks. Source-only shim currency does not qualify native fidelity. Namespace discovery errors/deadlines, every original provider workflow and retirement protections remain required.

The old in-progress alias/collision implementation paragraphs are superseded by their recorded source/artifact receipts; their native/generated acceptance remains open. Historical lane-only tagging and blanket generation holds do not override the current owner task; use scoped review/delivery and native safety gates.

## Development checks

Keep the default source suite fast with the shared real-sdist input payload check. Packaging changes and releases also require `uv run --extra test python -m pytest -q tests_artifacts/test_sdist.py`, which runs every shipped source test in the extracted archive. Do not replace that complete gate with the fast payload check.

Run `uv sync --extra test --extra enrich`, then `./test.sh`. The wrapper runs `uv run --extra test python -m pytest -q`. Build artifacts with `uv build`; capture requires a separate owned-host session.

## Review, integration and cleanup

Use the detailed open tasks in [TODO.md](TODO.md) as the acceptance checklist. Complete one scoped MVP, then run the exact repository checks and unchanged 80% gate for each complete changed production module. Keep source, genuine artifacts, ordinary origins and native behavior separate. Obtain independent review before a milestone commit/push and verify the actual remote head. Reconcile concurrent source and all callers before main integration. Preserve recovery/unique work and fresh owner/worktree attachments before obsolete branch/file cleanup. Update TODO/PLAN and record only scoped verified results in CHANGELOG. Do not drive the owner's FontLab, install into its user folder or publish a site from this proposal.

## Private documentation delivery gates

Consume the independently reviewed source-only candidate, rebuild generated output with the actual source commit epoch, and qualify normal repository main Actions and immutable X/Y lineage. Preserve native/owner-install gates. Private Pages configuration and publication remain owner-held.

Optional idea, not committed: a runtime helper such as `fontlab_echopy.doc(cls)` could print the overlay text inside FontLab, where the native classes show only native documentation (live reports 32 and 32b; the editor has no hover or completion route). It needs the owner's interest first; do not build it speculatively.
