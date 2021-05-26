from app.reco.gstr_9c.paths import get_paths, get_file
from app.reco.gstr_9c.generators.initializer import initialize_new_project
from app.reco.gstr_9c.generators.project_configs import load_toml_config

from app.common.ui.text_box_window import text_box_window
from app.common.ui.reco import gst_reco_ui


def initialize_project():
    global project_config, gstr_9c_ui

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
        gstr_9c_ui.project_init_status.config(text="Project: Initialized Successfully")
        gstr_9c_ui.hide_pre_load_buttons()


def load_saved_project():
    global project_config, gstr_9c_ui

    paths = get_file()
    project_config = load_toml_config(path=paths)
    if project_config["valid"]:
        gstr_9c_ui.project_init_status.config(text="Project: Initialized Successfully")
        gstr_9c_ui.hide_pre_load_buttons()


def reset_project_init():
    global project_config, gstr_9c_ui

    project_config = None
    gstr_9c_ui.reset_initialization()


def start_window_app():
    global gstr_9c_ui

    command_config = {
        "project_commands": [
            {
                "Inititalize 9C Project": {
                    "command": initialize_project,
                    "row": 5,
                    "column": 0,
                }
            },
            {
                "Load Saved Project": {
                    "command": load_saved_project,
                    "row": 5,
                    "column": 4,
                }
            },
        ],
        "reset_button": {
            "title": "Reset Initialization",
            "command": reset_project_init,
            "row": 5,
            "column": 0,
        },
    }
    gstr_9c_ui = gst_reco_ui(
        window_title="GSTR 9C Reco Utility",
        title="GSTR 9C Utility",
        button_commands=command_config,
        menu=True,
    )
    gstr_9c_ui.initialize_engine()

    return True


gstr_9c_ui = None
project_config = None