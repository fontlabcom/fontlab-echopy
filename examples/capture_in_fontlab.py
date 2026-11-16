# this_file: examples/capture_in_fontlab.py
"""Run this code inside FontLab after installing Echopy into its Python path."""
from pathlib import Path
from fontlab_echopy.tooling.cli import main

# Keep host captures outside your publishable source tree.
main(["capture", str(Path.home() / ".cache/fontlab-echopy/native.json")])
