from app.helpers.utilities.archive import make_archive
import os
from pathlib import Path
import shutil
import PyInstaller.__main__


def archive_function(path_to_files, file_name):
    shutil.make_archive(base_name=file_name, format="zip", root_dir=path_to_files)


CWD = os.getcwd()
SPECS = {
    "BUNDLED": {"file": str(Path(CWD, "bundled.spec"))},
    "UNBUNDLED": {"file": str(Path(CWD, "unbundled.spec"))},
}

DEFAULT_ARGS = {"--upx-dir", "upx"}

for (spec, spec_props) in SPECS.items():
    PyInstaller.__main__.run(
        [
            spec_props["file"],
            "-y",
            *DEFAULT_ARGS,
        ]
    )
    if spec == "UNBUNDLED":
        make_archive(
            path_to_files=Path(CWD, "dist", "main"),
            file_name=Path(CWD, "dist", "GSTR Utils"),
        )
