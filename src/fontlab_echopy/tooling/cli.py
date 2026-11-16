# this_file: src/fontlab_echopy/tooling/cli.py
"""Explicit capture, generate, enrich, merge, and one-command build pipeline."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from .capture import capture
from .generate import generate
from .merge import merge


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    cap = sub.add_parser(
        "capture", help="Run in FontLab; no native operations are called"
    )
    cap.add_argument("output", type=Path)
    gen = sub.add_parser("generate")
    gen.add_argument("capture", type=Path)
    gen.add_argument("output", type=Path)
    en = sub.add_parser("enrich")
    en.add_argument("capture", type=Path)
    en.add_argument("output", type=Path)
    en.add_argument("--cache", type=Path, required=True)
    en.add_argument(
        "--max-classes", type=int, default=0, help="0 = every matching class"
    )
    mg = sub.add_parser("merge")
    mg.add_argument("raw", type=Path)
    mg.add_argument("output", type=Path)
    mg.add_argument("--overlay", type=Path, action="append", default=[])
    docs = sub.add_parser(
        "docnames",
        help="Export native-named documentation aliases from enriched source",
    )
    docs.add_argument("output", type=Path)
    for command, text in (
        ("identities", "Write the capture identity manifest into a merged package"),
        ("verify-identities", "Fail unless the shipped manifest matches the raw capture"),
    ):
        ids = sub.add_parser(command, help=text)
        ids.add_argument("capture", type=Path)
        ids.add_argument("package", type=Path)
    run = sub.add_parser(
        "pipeline", help="Capture or read metadata, generate, enrich, merge"
    )
    run.add_argument("--capture", type=Path, help="Omit to capture inside FontLab")
    run.add_argument("--raw", type=Path, required=True)
    run.add_argument("--output", type=Path, required=True)
    run.add_argument("--overlay", type=Path, action="append", default=[])
    run.add_argument("--qt-cache", type=Path)
    run.add_argument(
        "--qt-overlay",
        type=Path,
        help="Persist fetched enrichment as a versioned source input",
    )
    run.add_argument(
        "--reports",
        type=Path,
        help="Write current native/upstream/pipeline verification reports",
    )
    args = parser.parse_args(argv)
    if args.command == "pipeline" and args.qt_overlay and not args.qt_cache:
        parser.error("--qt-overlay requires --qt-cache")
    if args.command == "docnames":
        from .docnames import export_docnames

        result = export_docnames(args.output)
        result = {
            "modules": len(result["modules"]),
            "declared_names": sum(
                len(item["declared_names"]) for item in result["modules"].values()
            ),
            "manifest": "docnames-manifest.json",
        }
    elif args.command == "capture":
        result = capture()
        if not any(item["available"] for item in result["modules"].values()):
            parser.error(
                "capture requires native modules inside FontLab; no output was written"
            )
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        result = {
            "modules": {
                name: item["available"] for name, item in result["modules"].items()
            }
        }
    elif args.command in {"identities", "verify-identities"}:
        from .identities import verify_identities, write_identities

        check = verify_identities if args.command == "verify-identities" else write_identities
        manifest = check(args.capture, args.package)
        result = {
            "capture_sha256": manifest["capture_sha256"],
            "scopes": len(manifest["scopes"]),
            "native_spellings": len(manifest["native_spellings"]),
        }
    elif args.command == "generate":
        data = args.capture.read_bytes()
        identity = {"sha256": hashlib.sha256(data).hexdigest(), "encoding": "original-utf8-file"}
        result = generate(json.loads(data), args.output, identity)
    elif args.command == "merge":
        result = merge(args.raw, args.output, args.overlay)
    elif args.command == "enrich":
        from .enrich import enrich

        result = enrich(
            json.loads(args.capture.read_text()),
            args.cache,
            args.output,
            args.max_classes,
        )
        result = {key: value for key, value in result.items() if key != "documents"}
    else:
        data = json.loads(args.capture.read_text()) if args.capture else capture()
        if not args.capture and not any(
            item["available"] for item in data["modules"].values()
        ):
            parser.error(
                "pipeline requires FontLab or --capture; existing output was preserved"
            )
        capture_bytes = (
            args.capture.read_bytes()
            if args.capture
            else json.dumps(data, sort_keys=True).encode()
        )
        result = {
            "capture_identity": {
                "sha256": hashlib.sha256(capture_bytes).hexdigest(),
                "encoding": "original-utf8-file" if args.capture else "canonical-json",
            },
            "generation": generate(
                data,
                args.raw,
                {
                    "sha256": hashlib.sha256(capture_bytes).hexdigest(),
                    "encoding": "original-utf8-file" if args.capture else "canonical-json",
                },
            ),
        }
        overlays = list(args.overlay)
        upstream_report = None
        if args.qt_cache:
            from .enrich import enrich

            qt_overlay = args.qt_overlay or args.qt_cache / "qt-overlay.json"
            upstream_report = enrich(data, args.qt_cache, qt_overlay)
            result["enrichment"] = upstream_report["coverage"]
            overlays.insert(0, qt_overlay)
        result["merge"] = merge(args.raw, args.output, overlays)
        provenance_path = args.output / "_provenance.json"
        provenance = json.loads(provenance_path.read_text())
        provenance["capture_identity"] = result["capture_identity"]
        if upstream_report is not None:
            provenance["qt_enrichment"] = upstream_report
        provenance_path.write_text(
            json.dumps(provenance, indent=2, sort_keys=True) + "\n"
        )
        from .identities import write_identities

        write_identities(capture_bytes, args.output)
        if args.reports:
            args.reports.mkdir(parents=True, exist_ok=True)
            (args.reports / "native-coverage.json").write_text(
                json.dumps(result["generation"], indent=2, sort_keys=True) + "\n"
            )
            if upstream_report is not None:
                (args.reports / "qt-enrichment.json").write_text(
                    json.dumps(upstream_report, indent=2, sort_keys=True) + "\n"
                )
            (args.reports / "pipeline.json").write_text(
                json.dumps(result, indent=2, sort_keys=True) + "\n"
            )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
