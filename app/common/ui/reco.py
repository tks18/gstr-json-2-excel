import tkinter as tk
from app.common.ui.base import base_ui

from app.common.ui.common import BG, FG


class gst_reco_ui(base_ui):
    def __init__(self, window_title, title, button_commands, menu):
        super(gst_reco_ui, self).__init__(window_title, title, menu)

        for buttons in button_commands:
            for (button_key, button_props) in buttons.items():
                self.generate_csv_button = tk.Button(
                    self.ui,
                    text=button_key,
                    command=button_props["command"],
                    fg=FG,
                    bg=BG,
                )
                self.generate_csv_button.grid(
                    row=button_props["row"],
                    column=button_props["column"],
                    columnspan=4,
                    pady=5,
                )
