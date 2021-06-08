import app.utils.gstr_1 as gstr_1_utils
import app.utils.gstr_2 as gstr_2_utils
import app.reco.gstr_9c.main as gstr_9c_utils

from app.helpers.ui.main_ui import main_window
from app.helpers.font_loader import initialize_fonts


def main_ui_window():
    global main_ui

    main_ui = main_window(
        window_title="GSTR Utilities",
        title="GST Utilities",
        buttons={
            "utility_buttons": [
                {
                    "title": "GSTR 1",
                    "command": open_gstr_1_window,
                    "row": 4,
                    "column": 0,
                },
                {
                    "title": "GSTR 2",
                    "command": open_gstr_2_window,
                    "row": 4,
                    "column": 2,
                },
            ],
            "reco_buttons": [
                {
                    "title": "GSTR 9C",
                    "command": open_gstr_9c_window,
                    "row": 6,
                    "column": 0,
                }
            ],
        },
        menu=False,
    )

    main_ui.initialize_engine()


def open_gstr_1_window():
    global main_ui

    main_ui.close_window()
    close_app = gstr_1_utils.start_window_app()
    if not close_app:
        main_ui = None
        main_ui_window()


def open_gstr_2_window():
    global main_ui

    main_ui.close_window()
    close_app = gstr_2_utils.start_window_app()
    if not close_app:
        main_ui = None
        main_ui_window()


def open_gstr_9c_window():
    global main_ui

    main_ui.close_window()
    close_app = gstr_9c_utils.start_window_app()
    if not close_app:
        main_ui = None
        main_ui_window()


main_ui = None

if __name__ == "__main__":
    initialize_fonts()
    main_ui_window()