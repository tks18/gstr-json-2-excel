from app.reco.gstr_9c.paths import get_paths
from app.reco.gstr_9c.generators.generate_folder_structure import (
    generate_folder_structure,
)
from app.common.ui.text_box_window import text_box_window

from app.common.ui.reco import gst_reco_ui


def initialize_project():
    project_pop_window = text_box_window(
        master=gstr_9c_ui.ui, title="Enter the Company Name", label="Company Name"
    )
    gstr_9c_ui.ui.wait_window(project_pop_window.ui)

    project_pop_result = project_pop_window.result
    gstr_9c_ui.ui.focus()
    if project_pop_result["success"]:
        paths = get_paths()
        generate_folder_structure(
            base_folder_path=paths, project_name=project_pop_result["text"]
        )


def start_window_app():
    global gstr_9c_ui

    gstr_9c_ui = gst_reco_ui(
        window_title="GSTR 9C Reco Utility",
        title="GSTR 9C Utility",
        button_commands=[{"Inititalize a 9C Project": initialize_project}],
        menu=True,
    )
    gstr_9c_ui.initialize_engine()

    return False


gstr_9c_ui = None