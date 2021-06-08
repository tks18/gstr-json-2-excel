import tkinter as tk
from app.helpers.ui.base import base_ui


class main_window(base_ui):
    def __init__(self, window_title, title, buttons, menu):
        super(main_window, self).__init__(
            window_title=window_title, title=title, menu=menu, logo=True
        )

        self.ui.config(padx=60, pady=60)

        utility_label = tk.Label(
            text="General Utilities", **self.theme, font=self.FONTS["small"]
        )
        utility_label.grid(row=3, column=0, columnspan=4)
        for btn in buttons["utility_buttons"]:
            new_btn = tk.Button(
                text=btn["title"],
                **self.theme,
                command=btn["command"],
                font=self.FONTS["buttons"]["small"]
            )
            new_btn.grid(row=btn["row"], column=btn["column"], pady=10, columnspan=2)

        reco_label = tk.Label(
            text="Reconciliation Utilities", **self.theme, font=self.FONTS["small"]
        )
        reco_label.grid(row=5, column=0, columnspan=4)
        for btn in buttons["reco_buttons"]:
            new_btn = tk.Button(
                text=btn["title"],
                **self.theme,
                command=btn["command"],
                font=self.FONTS["buttons"]["small"]
            )
            new_btn.grid(row=btn["row"], column=btn["column"], pady=10, columnspan=4)
