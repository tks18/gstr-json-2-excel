from pathlib import Path
from tkinter import filedialog


def get_paths():
    init_proj_dir = filedialog.askdirectory(
        title="Select a Directory to Initialize the 9C Project"
    )
    return Path(init_proj_dir.lower())