import gstr_1 as gstr_1_utils
import gstr_2 as gstr_2_utils

from tkinter import *
from helpers import resource_path


def main_ui_window():
    global main_ui

    main_ui = Tk()
    icon = PhotoImage(file=resource_path("images/logo.png"))
    main_ui.iconphoto(False, icon)
    main_ui.title("GSTR Utils by Shan.tk")
    main_ui.config(padx=50, pady=50)

    main_title = Label(
        text="GSTR 1 & 2 Utilities", font=("Courier New", 20, "bold"), padx=10, pady=20
    )
    main_title.grid(row=0, column=0, columnspan=2)

    ui_buttons = [
        {
            "title": "GSTR 1",
            "command": open_gstr_1_window,
            "row": 2,
            "column": 0,
        },
        {"title": "GSTR 2", "command": open_gstr_2_window, "row": 2, "column": 1},
    ]

    utility_label = Label(text="Select the utility which you want to open:")
    utility_label.grid(row=1, column=0, columnspan=2)
    for btn in ui_buttons:
        new_btn = Button(text=btn["title"], command=btn["command"])
        new_btn.grid(row=btn["row"], column=btn["column"])

    developer_label = Label(
        text="Shan.tk", font=("Courier New", 10, "bold"), padx=10, pady=30
    )
    developer_label.grid(row=3, column=0, columnspan=2)

    main_ui.mainloop()


def open_gstr_1_window():
    global main_ui

    main_ui.destroy()
    gstr_1_utils.start_window_app()


def open_gstr_2_window():
    global main_ui

    main_ui.destroy()
    gstr_2_utils.start_window_app()


def restart_window():
    main_ui_window()


main_ui = None

main_ui_window()