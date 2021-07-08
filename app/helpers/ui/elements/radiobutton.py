from tkinter import Radiobutton


def radio_btn(master, text, variable, value, command):
    new_radiobtn = Radiobutton(
        master.ui,
        text=text,
        variable=variable,
        value=value,
        **master.theme,
        selectcolor=master.bg,
        font=master.FONTS["buttons"]["small"],
        command=command,
    )
    return new_radiobtn