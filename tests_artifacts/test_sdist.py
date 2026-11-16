# this_file: tests_artifacts/test_sdist.py
"""Run all shipped source tests from the real sdist, without checkout inputs.

This checkout-only build regression stays outside ``tests/`` so the extracted
archive can run its complete source suite without recursively building archives.
"""

import os
from pathlib import Path
import shutil
import subprocess
import tarfile


def test_sdist_when_extracted_then_all_shipped_source_tests_pass(tmp_path):
    root = Path(__file__).resolve().parents[1]
    uv = shutil.which("uv")
    assert uv is not None, "uv is required to build and test the source distribution"
    built = subprocess.run(
        [uv, "build", "--sdist", "--out-dir", str(tmp_path / "dist"), str(root)],
        capture_output=True, text=True,
    )
    assert built.returncode == 0, built.stdout + built.stderr
    (sdist,) = (tmp_path / "dist").glob("*.tar.gz")
    with tarfile.open(sdist) as archive:
        archive.extractall(tmp_path / "source", filter="data")
    (source,) = (tmp_path / "source").iterdir()
    env = os.environ.copy()
    env.pop("VIRTUAL_ENV", None)
    env.pop("PYTEST_ADDOPTS", None)
    env["UV_PROJECT_ENVIRONMENT"] = str(tmp_path / "venv")
    qualified = subprocess.run(
        [uv, "run", "--extra", "test", "python", "-c",
         "import importlib.metadata as m, json, platform, sys; "
         "from email.parser import BytesParser; from pathlib import Path; "
         "import fontlab_echopy; root=Path.cwd(); "
         "assert not (root/'.git').exists(); "
         "assert m.version('fontlab-echopy') == "
         "BytesParser().parsebytes((root/'PKG-INFO').read_bytes())['Version']; "
         "assert Path(fontlab_echopy.__file__).resolve().is_relative_to(root/'src'); "
         "print(json.dumps({'python':sys.version,'machine':platform.machine(),"
         "'version':m.version('fontlab-echopy'),'package':fontlab_echopy.__file__}))"],
        cwd=source, env=env, capture_output=True, text=True,
    )
    assert qualified.returncode == 0, qualified.stdout + qualified.stderr
    (tmp_path / "source-runtime.json").write_text(qualified.stdout)
    tested = subprocess.run(
        [uv, "run", "--extra", "test", "python", "-m", "pytest", "-q",
         "--junitxml=" + str(tmp_path / "source-results.xml")],
        cwd=source, env=env, capture_output=True, text=True,
    )
    assert tested.returncode == 0, tested.stdout + tested.stderr
