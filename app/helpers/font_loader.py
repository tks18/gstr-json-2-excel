from pyglet import font
from glob import glob
from pathlib import Path
from app.helpers.utilities.path_helpers import resource_path


def initialize_fonts():
    fonts_path = resource_path("fonts")
    for file in glob(f"{fonts_path}/**.ttf"):
        corrected_path = str(Path(file))
        font.add_file(corrected_path)
