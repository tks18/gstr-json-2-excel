import tkinter as tk
from tkinter import ttk

from app.common.helpers import resource_path

from app.common.ui.common import BG, FG, TTK_THEME


class base_ui:
    def __init__(self, window_title, title, menu, maxcol=4):
        self.ui = tk.Tk()
        self.ui.title(window_title)
        self.ui.config(padx=40, pady=40, bg=BG)
        self.icon = tk.PhotoImage(file=resource_path("images/logo.png"))
        self.ui.iconphoto(False, self.icon)

        if menu:
            self.menuButton = tk.Button(
                self.ui, text="Menu", command=self.close_window, fg=FG, bg=BG
            )
            self.menuButton.grid(row=0, column=0)

        self.canvas = tk.Canvas(
            self.ui, height=100, width=100, highlightthickness=0, bg=BG
        )
        self.canvas.create_image(50, 50, image=self.icon)
        self.canvas.grid(row=1, column=0, columnspan=maxcol)

        self.main_title = tk.Label(
            master=self.ui,
            text=title,
            font=("Courier new", 23, "bold"),
            pady=40,
            bg=BG,
            fg=FG,
        )
        self.ui.focus_force()
        self.main_title.grid(row=2, column=0, columnspan=maxcol)

        self.style = ttk.Style()

        self.style.theme_create(
            "gstr_theme",
            parent="alt",
            settings=TTK_THEME,
        )
        self.style.theme_use("gstr_theme")

        self.developer_label_head = tk.Label(
            self.ui, text="Developed by", font=("Arial", 10, "bold"), bg=BG, fg=FG
        )
        self.developer_label_head.grid(
            row=20, column=0, columnspan=maxcol, pady=(20, 0)
        )

        self.developer_label_value = tk.Label(
            self.ui, text="Shan.tk", font=("Arial", 9, "bold"), bg=BG, fg=FG
        )
        self.developer_label_value.grid(
            row=21, column=0, columnspan=maxcol, pady=(0, 0)
        )

    def close_window(self):
        self.ui.destroy()

    def initialize_engine(self):
        self.ui.mainloop()