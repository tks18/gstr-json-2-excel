from pathlib import Path
from tkinter import filedialog


def get_paths():
    csv_write_path = filedialog.askdirectory(
        title="Enter the Dir to which the Format CSV Has to be Saved"
    )
    return Path(csv_write_path.lower())