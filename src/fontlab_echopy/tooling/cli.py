# this_file: src/fontlab_echopy/tooling/cli.py
"""Explicit capture, generate, enrich, reference overlays, merge, llms.txt and pipeline."""

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
    for command, flag, default, text in (
        ("proteus-docs", "--api-docs", "vendor/api-docs", "Build the Proteus API overlay"),
        ("mcp-docs", "--mcp-json", "vendor/mcp/fontlab-mcp.json", "Build the fontpr MCP overlay"),
    ):
        ref = sub.add_parser(command, help=text)
        ref.add_argument(flag, type=Path, default=Path(default))
        ref.add_argument("--generated", type=Path, default=Path("generated"))
        ref.add_argument("--output", type=Path, required=True)
    llms = sub.add_parser("llms", help="Write a compact llms.txt API index")
    llms.add_argument("--package", type=Path, default=Path("src/fontlab_echopy"))
    llms.add_argument("--output", type=Path, default=Path("src_docs/md/llms.txt"))
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
    run.add_argument(
        "--retain",
        action="append",
        default=[],
        help="Keep this top-level module's raw files, coverage and identities "
        "from the earlier capture instead of regenerating it",
    )
    args = parser.parse_args(argv)
    if args.command == "pipeline" and args.qt_overlay and not args.qt_cache:
        parser.error("--qt-overlay requires --qt-cache")
    if args.command == "pipeline" and "PythonQt" in args.retain and args.qt_cache:
        # enrich() reads PythonQt from the new capture, which retention removes.
        parser.error("--retain PythonQt cannot be combined with --qt-cache")
    if args.command == "pipeline" and any("." in name for name in args.retain):
        parser.error("--retain takes top-level module names, such as PythonQt")
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
    elif args.command == "proteus-docs":
        from .proteus import write as write_proteus

        result = write_proteus(args.api_docs, args.generated, args.output)
    elif args.command == "mcp-docs":
        from .mcp import write as write_mcp

        result = write_mcp(args.mcp_json, args.generated, args.output)
    elif args.command == "llms":
        from .llms import write as write_llms

        result = write_llms(args.package, args.output)
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
        retained = None
        kept_coverage: dict = {}
        if args.retain:
            old = json.loads((args.raw / "coverage.json").read_text())
            unknown = sorted(set(args.retain) - set(old["modules"]))
            if unknown:
                parser.error(f"--retain: no earlier coverage for modules {unknown}")
            kept_coverage = {
                name: entry
                for name, entry in old["modules"].items()
                if name.partition(".")[0] in args.retain
            }
            data = dict(data, modules={
                name: entry for name, entry in data["modules"].items()
                if name not in args.retain
            })
        identity = {
            "sha256": hashlib.sha256(capture_bytes).hexdigest(),
            "encoding": "original-utf8-file" if args.capture else "canonical-json",
        }
        generation = generate(data, args.raw, identity, tuple(args.retain))
        if args.retain:
            from .identities import retain_scopes

            # Written only after generation succeeds; merge below replaces the manifest.
            retained = retain_scopes(args.output, args.retain)
            generation["modules"].update(kept_coverage)
            generation["modules"] = dict(sorted(generation["modules"].items()))
            generation["retained_scopes"] = retained
            (args.raw / "coverage.json").write_text(
                json.dumps(generation, indent=2, sort_keys=True) + "\n"
            )
        result = {"capture_identity": identity, "generation": generation}
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
        if retained is not None:
            provenance["retained_scopes"] = retained
        else:
            provenance.pop("retained_scopes", None)
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
