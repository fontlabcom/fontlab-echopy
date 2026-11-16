#!/bin/sh
# this_file: test.sh
set -eu
uv run --extra test python -m pytest -q
