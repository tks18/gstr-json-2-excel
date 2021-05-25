from app.reco.gstr_9c.paths import get_paths
from app.reco.gstr_9c.generate_folder_structure import generate_folder_structure

from app.common.ui.reco import gst_reco_ui


def initialize_project():
    paths = get_paths()
    generate_folder_structure(paths)


def start_window_app():
    gstr_9c_ui = gst_reco_ui(
        window_title="GSTR 9C Reco Utility",
        title="GSTR 9C Utility",
        button_commands=[{"Inititalize a 9C Project": initialize_project}],
        menu=True,
    )

    gstr_9c_ui.initialize_engine()

    return False