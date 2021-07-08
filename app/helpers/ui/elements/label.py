from tkinter import Label


def small_label(master, text, bold):
    font_label = "small_bold" if bold else "small"
    new_label = Label(master.ui, text=text, **master.theme, font=master.FONTS[font_label])
    return new_label


def medium_label(master, text, bold):
    font_label = "medium_bold" if bold else "medium"
    new_label = Label(master.ui, text=text, **master.theme, font=master.FONTS[font_label])
    return new_label


def title_label(master, text):
    new_label = Label(master.ui, text=text, **master.theme, font=master.FONTS["title"])
    return new_label