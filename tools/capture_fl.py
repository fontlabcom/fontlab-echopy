#!/usr/bin/env python3
# this_file: tools/capture_fl.py
"""Capture FontLab's FL module (FontLab 5 API) read-only through remopy.

Run from this checkout with both packages importable, for example:

    uv run --with ../fontlab-remopy python tools/capture_fl.py

Opens no fonts and changes no preferences: it lists names, classes and
signatures only. If FL is absent the output records that. With --base the FL
entry is added to an existing full capture so the pipeline can consume one file.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from fontlab_remopy import FontLab, NativeExecutionError, ResultTransportError  # noqa: E402

from fontlab_echopy.tooling.chunked import capture_module  # noqa: E402


def load_base(parser: argparse.ArgumentParser, path: Path | None) -> dict:
    """The capture to extend, or an empty one; a missing or malformed file is a usage error."""
    if path is None:
        return {"schema": 1, "modules": {}}
    try:
        data = json.loads(path.read_text())
    except (OSError, ValueError) as error:
        parser.error(f"--base {path}: cannot read a capture JSON ({error})")
    if not isinstance(data, dict) or not isinstance(data.get("modules"), dict):
        parser.error(f"--base {path}: not a capture (expected an object with a 'modules' object)")
    return data


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--output", type=Path, default=ROOT / "generated/capture-FL.json")
    parser.add_argument("--base", type=Path, help="Existing capture JSON to add FL to")
    parser.add_argument("--timeout", type=float, default=30)
    args = parser.parse_args(argv)
    data = load_base(parser, args.base)  # Checked first: a bad --base must not cost a host session.
    # ValueError is remopy's 32 KiB code limit; a chunk that trips it is split like any failed call.
    failures = (NativeExecutionError, ResultTransportError, ValueError)
    with FontLab(timeout=args.timeout) as fl:
        item = capture_module(fl.run, "FL", failures)
    data["modules"]["FL"] = item
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
    scope = item["namespace"]
    print(json.dumps({"output": str(args.output), "available": item["available"],
                      "names": len(scope.get("names", [])), "classes": len(scope.get("classes", [])),
                      "errors": len(scope.get("errors", []))}))


if __name__ == "__main__":
    main()
