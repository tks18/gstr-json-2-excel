import gstr_1_utils

from tkinter import *
from tkinter import messagebox

main_ui = Tk()
main_ui.title("GSTR Utils by Shan.tk")
main_ui.config(padx=50, pady=50)

main_title = Label(text="GSTR 1 & 2 Utilities", font=("Courier New", 20, "bold"))
main_title.grid(row=0, column=0, columnspan=2)


def display_message():
    messagebox.showinfo(
        title="Work in Progress", message="GSTR 2 Utility is under Progress."
    )


ui_buttons = [
    {
        "title": "GSTR 1",
        "command": gstr_1_utils.start_window_app,
        "row": 1,
        "column": 0,
    },
    {"title": "GSTR 2", "command": display_message, "row": 1, "column": 1},
]

for btn in ui_buttons:
    new_btn = Button(text=btn["title"], command=btn["command"])
    new_btn.grid(row=btn["row"], column=btn["column"])

main_ui.mainloop()