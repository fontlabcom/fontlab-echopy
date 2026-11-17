# this_file: tests/test_installed_class_overlays.py
"""The six C14 class overlays must survive an ordinary wheel and sdist install.

Builds the package with ``uv build`` (genuine hatch-vcs version), installs each artifact
into a fresh virtual environment and reads the installed stubs: the shipped ``fontlab.pyi``
and ``fontgate.pyi`` must equal the source bytes, match the installed ``_provenance.json``
hashes and carry each overlay's guidance in the class docstring.
"""

import ast
import hashlib
import json
import shutil
import stat
import subprocess
import tarfile
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
PACKAGE = ROOT / "src/fontlab_echopy"
TARGETS = (
    "fontlab.flAnchor",
    "fontlab.flGuideLine",
    "fontlab.flShape",
    "fontgate.fgAnchor",
    "fontgate.fgLayer",
    "fontgate.fgShape",
)
STUBS = ("fontlab.pyi", "fontgate.pyi")
UV = shutil.which("uv")


def uv() -> str:
    """Return the uv executable, or skip with a reason before any call can receive None."""
    path = UV
    if path is None:
        pytest.skip("uv is required to build and install the package")
    return path


def run(*args: str) -> str:
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    assert result.returncode == 0, (
        f"{' '.join(args)} failed:\n{result.stdout}\n{result.stderr}"
    )
    return result.stdout.strip()


@pytest.fixture(scope="module")
def artifacts(tmp_path_factory) -> dict[str, Path]:
    out = tmp_path_factory.mktemp("dist")
    run(uv(), "build", "--sdist", "--wheel", "--out-dir", str(out), str(ROOT))
    wheels, sdists = list(out.glob("*.whl")), list(out.glob("*.tar.gz"))
    assert len(wheels) == 1 and len(sdists) == 1, (
        f"unexpected build output: {sorted(out.iterdir())}"
    )
    return {"wheel": wheels[0], "sdist": sdists[0]}


def installed_package(artifact: Path, venv: Path) -> Path:
    """Install one artifact into a new venv and return its installed fontlab_echopy directory."""
    run(uv(), "venv", "--quiet", "--python", "3.11", str(venv))
    python = venv / "bin/python"
    run(uv(), "pip", "install", "--quiet", "--python", str(python), str(artifact))
    location = run(
        str(python),
        "-I",
        "-c",
        "import fontlab_echopy, pathlib; print(pathlib.Path(fontlab_echopy.__file__).parent)",
    )
    package = Path(location)
    assert venv in package.parents, (
        f"fontlab_echopy imported from outside the venv: {package}"
    )
    return package


def class_doc(stub: Path, name: str) -> str:
    tree = ast.parse(stub.read_text())
    cls = next(
        (n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == name), None
    )
    assert cls is not None, f"{stub.name}: class {name} is missing"
    return ast.get_docstring(cls) or ""


def check_installed(package: Path) -> None:
    provenance = json.loads((package / "_provenance.json").read_text())
    assert provenance == json.loads((PACKAGE / "_provenance.json").read_text()), (
        "installed provenance differs"
    )
    for stub in STUBS:
        installed = (package / stub).read_bytes()
        assert installed == (PACKAGE / stub).read_bytes(), (
            f"installed {stub} differs from source"
        )
        assert (
            hashlib.sha256(installed).hexdigest() == provenance["merged_outputs"][stub]
        ), f"{stub}: provenance hash"
    patches = json.loads((ROOT / "patches/manual.json").read_text())
    for target in TARGETS:
        module, name = target.split(".")
        guidance = patches[target]["doc"]
        assert guidance in class_doc(package / f"{module}.pyi", name), (
            f"installed {target} lost its overlay"
        )


@pytest.mark.parametrize("kind", ["wheel", "sdist"])
def test_installed_package_when_built_and_installed_then_six_overlays_ship(
    kind, artifacts, tmp_path
):
    check_installed(installed_package(artifacts[kind], tmp_path / f"venv-{kind}"))


def test_sdist_when_built_then_required_source_test_inputs_ship(artifacts):
    inputs = [*sorted((ROOT / "generated").rglob("*.py")),
              ROOT / "generated/coverage.json", ROOT / "tools/capture_fl.py"]
    assert len(inputs) == 19, "review the complete shipped-test input list when it changes"
    with tarfile.open(artifacts["sdist"]) as archive:
        prefix = archive.getnames()[0].split("/")[0]
        for source in inputs:
            member = archive.getmember(prefix + "/" + source.relative_to(ROOT).as_posix())
            assert member.isfile(), source
            assert archive.extractfile(member).read() == source.read_bytes(), source
            assert member.mode == stat.S_IMODE(source.stat().st_mode), source
        installer = archive.getmember(prefix + "/install.vfpy")
        assert archive.extractfile(installer).read() == (ROOT / "install.vfpy").read_bytes()
        assert installer.mode == stat.S_IMODE((ROOT / "install.vfpy").stat().st_mode)


def test_check_installed_when_overlay_missing_then_rejected(tmp_path):
    package = tmp_path / "fontlab_echopy"
    shutil.copytree(
        PACKAGE,
        package,
        ignore=shutil.ignore_patterns("tooling", "PythonQt", "__pycache__"),
    )
    stub = package / "fontgate.pyi"
    guidance = json.loads((ROOT / "patches/manual.json").read_text())[
        "fontgate.fgShape"
    ]["doc"]
    stub.write_text(stub.read_text().replace(guidance, ""))
    with pytest.raises(AssertionError, match="differs from source"):
        check_installed(package)


def test_check_installed_when_stub_absent_then_rejected(tmp_path):
    package = tmp_path / "fontlab_echopy"
    shutil.copytree(
        PACKAGE,
        package,
        ignore=shutil.ignore_patterns("tooling", "PythonQt", "__pycache__"),
    )
    (package / "fontlab.pyi").unlink()
    with pytest.raises(FileNotFoundError):
        check_installed(package)


@pytest.mark.parametrize("target", TARGETS)
def test_installed_wheel_when_help_rendered_outside_fontlab_then_overlay_shown(
    target, artifacts, tmp_path_factory
):
    """Offline `pydoc` (what `help()` renders) shows the overlay through the stub path.

    Inside FontLab the classes are the native builtins and show only native text
    (live reports 32 and 32b), so this offline route is the delivery path.
    """
    venv = tmp_path_factory.mktemp("help") / "venv"
    installed_package(artifacts["wheel"], venv)
    module, name = target.split(".")
    guidance = json.loads((ROOT / "patches/manual.json").read_text())[target]["doc"]
    rendered = run(
        str(venv / "bin/python"),
        "-I",
        "-c",
        f"import pydoc, fontlab_echopy.{module} as m; print(pydoc.render_doc(m.{name}))",
    )
    assert "Supplemental documentation" in rendered, f"{target}: no overlay in help()"
    assert guidance.splitlines()[0] in rendered, f"{target}: guidance text missing"
