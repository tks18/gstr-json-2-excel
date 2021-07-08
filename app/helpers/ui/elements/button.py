from tkinter import Button


def small_button(master, label, command):
    new_btn = Button(
        master.ui,
        text=label,
        **master.theme,
        command=command,
        font=master.FONTS["buttons"]["small"]
    )

    return new_btn


def medium_button(master, label, command):
    new_btn = Button(
        master.ui,
        text=label,
        **master.theme,
        command=command,
        font=master.FONTS["buttons"]["medium"]
    )

    return new_btn


def large_button(master, label, command):
    new_btn = Button(
        master.ui,
        text=label,
        **master.theme,
        command=command,
        font=master.FONTS["buttons"]["large"]
    )

    return new_btn