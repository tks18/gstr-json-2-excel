import tkinter as tk
from tkinter import ttk
from app.helpers.utilities.path_helpers import resource_path

from app.helpers.ui.helpers.theme_constants import *
from app.helpers.ui.elements.init_class import tk_elements


class base_ui:
    def __init__(self, window_title, title, menu, logo, maxcol=4):
        self.bg = BG
        self.fg = FG
        self.FONTS = FONTS
        self.theme = THEME

        self.ui = tk.Tk()
        self.ui.title(window_title)
        self.ui.config(padx=20, pady=20, bg=self.bg)
        self.icon = tk.PhotoImage(file=resource_path("images/logo.png"))
        self.ui.iconphoto(False, self.icon)
        self.elements = tk_elements()

        if menu:
            self.menu_button = self.elements.small_btn(
                self, label="Menu", command=self.close_window
            )
            self.menu_button.grid(
                row=0,
                column=0,
            )

            self.about_button = self.elements.small_btn(
                self, label="About", command=self.close_window
            )
            self.about_button.grid(row=0, column=1)

        self.main_title = self.elements.medium_lbl(self, text=title, bold=True)
        self.main_title.grid(row=1, column=0, columnspan=maxcol, pady=(10, 10))
        self.ui.focus_force()

        if logo:
            self.canvas = tk.Canvas(
                self.ui, height=100, width=100, highlightthickness=0, bg=self.bg
            )
            self.canvas.create_image(50, 50, image=self.icon)
            self.canvas.grid(row=2, column=0, columnspan=maxcol, pady=(0, 20))

        self.style = ttk.Style()

        self.style.theme_create(
            "gstr_theme",
            parent="alt",
            settings=TTK_THEME,
        )
        self.style.theme_use("gstr_theme")

        self.developer_label_head = self.elements.small_lbl(
            self, text="Developed by", bold=False
        )
        self.developer_label_head.grid(
            row=20, column=0, columnspan=maxcol, pady=(20, 0)
        )

        self.developer_label_value = self.elements.small_lbl(
            self, text="Shan.tk", bold=True
        )
        self.developer_label_value.grid(
            row=21, column=0, columnspan=maxcol, pady=(0, 0)
        )

    def close_window(self):
        self.ui.destroy()

    def initialize_engine(self):
        self.ui.mainloop()