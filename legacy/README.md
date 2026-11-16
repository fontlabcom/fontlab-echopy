---
this_file: legacy/README.md
---

# Immutable migration archive

`source.tar.gz` retains 1434 original source, generator, merger, overlay, test,
and RST files byte-for-byte. These are archival snapshots, not active maintained
source; original this_file headers remain unchanged as provenance. File SHA256
hashes and source revisions are in ../MIGRATION.json. Source checkouts remain
untouched, including uncommitted changes.

Extract the archive into a scratch directory to inspect or build the original
RST documentation. The migrated active implementation is under ../src/.
Neither this archive nor runtime captures are included in wheel or sdist.
Original code-shadow is Apache-2.0; the Aidus introspector remains proprietary;
licenses are preserved at repository root and under ../licenses/.
