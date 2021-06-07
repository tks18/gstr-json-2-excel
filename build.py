import os
from git import Repo

# from pathlib import Path
# import PyInstaller.__main__


# SPECS = {
#     "BUNDLED": {"file": str(Path(os.getcwd(), "bundled.spec"))},
#     "UNBUNDLED": {"file": str(Path(os.getcwd(), "unbundled.spec"))},
# }

# DEFAULT_ARGS = {"--upx-dir", "upx"}

# for (spec, spec_props) in SPECS.items():
#     PyInstaller.__main__.run(
#         [
#             spec_props["file"],
#             *DEFAULT_ARGS,
#         ]
#     )

repo = Repo(os.getcwd())

commit_msg = ""
for diff_added in repo.untracked_files:
    commit_msg = f"{len(repo.untracked_files)} Changed Files\n  {diff_added}\n Automated Git Commiter by Shan.tk"

repo.git.add(all=True)
repo.git.commit("-m", commit_msg)
