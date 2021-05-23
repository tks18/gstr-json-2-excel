from app.utils.gstr_1 import start_window_app
from app.reco.gstr_9c.paths import get_paths
from app.reco.gstr_9c.generate_csv_template import generate_csv_template

from app.common.ui.reco import gst_reco_ui


def generate_csv():
    paths = get_paths()
    generate_csv_template(paths)


def start_window_app():
    gstr_9c_ui = gst_reco_ui(
        window_title="GSTR 9C Reco Utility",
        title="GSTR 9C Utility",
        button_commands={"generate_csv_cmd": generate_csv},
        menu=True,
    )

    gstr_9c_ui.initialize_engine()

    return False