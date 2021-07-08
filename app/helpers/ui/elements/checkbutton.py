from tkinter import Checkbutton


def check_btn(master, text, variable, command=None):
    new_checkbtn = Checkbutton(
        master.ui,
        text=text,
        variable=variable,
        **master.theme,
        command=command,
        font=master.FONTS["buttons"]["small"],
        activebackground=master.bg,
        activeforeground=master.fg,
        highlightcolor=master.bg,
        selectcolor=master.bg,
        onvalue=True,
        offvalue=False,
    )
    return new_checkbtn