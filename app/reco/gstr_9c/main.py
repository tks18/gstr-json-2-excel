from app.reco.gstr_9c.paths import get_paths, get_file
from app.reco.gstr_9c.generators.initializer import initialize_new_project
from app.reco.gstr_9c.generators.project_configs import load_toml_config

from app.common.ui.text_box_window import text_box_window
from app.common.ui.reco import gst_reco_ui


def initialize_project():
    global project_config
    project_pop_window = text_box_window(
        master=gstr_9c_ui.ui, title="Enter the Company Name", label="Company Name"
    )
    gstr_9c_ui.ui.wait_window(project_pop_window.ui)

    project_pop_result = project_pop_window.result
    gstr_9c_ui.ui.focus()
    if project_pop_result["success"]:
        paths = get_paths()
        project_config = initialize_new_project(
            base_folder_path=paths, project_name=project_pop_result["text"]
        )


def load_saved_project():
    global project_config
    paths = get_file()
    project_config = load_toml_config(path=paths)
    print(project_config)


def start_window_app():
    global gstr_9c_ui

    gstr_9c_ui = gst_reco_ui(
        window_title="GSTR 9C Reco Utility",
        title="GSTR 9C Utility",
        button_commands=[
            {
                "Inititalize 9C Project": {
                    "command": initialize_project,
                    "row": 3,
                    "column": 0,
                }
            },
            {
                "Load Saved Project": {
                    "command": load_saved_project,
                    "row": 4,
                    "column": 0,
                }
            },
        ],
        menu=True,
    )
    gstr_9c_ui.initialize_engine()

    return False


gstr_9c_ui = None
project_config = None