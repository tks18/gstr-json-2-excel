import tkinter as tk
from app.helpers.ui.base import base_ui

from app.helpers.ui.common import BG, FG


class gst_reco_ui(base_ui):
    def __init__(self, window_title, title, button_commands, menu):
        maxcol = 8
        super(gst_reco_ui, self).__init__(
            window_title=window_title, title=title, menu=menu, maxcol=maxcol
        )

        self.button_commands = button_commands

        self.project_init_status = tk.Label(
            self.ui, text="Project: Not Initialized", fg=FG, bg=BG
        )
        self.project_init_status.grid(row=3, column=0, columnspan=maxcol, pady=(0, 10))

        self.project_command_label = tk.Label(
            self.ui, text="Manage Project", fg=FG, bg=BG
        )
        self.project_command_label.grid(row=4, column=0, columnspan=maxcol)

        self.project_command_buttons = {}
        for buttons in button_commands["project_commands"]:
            for (button_key, button_props) in buttons.items():
                self.project_command_buttons[button_key] = tk.Button(
                    self.ui,
                    text=button_key,
                    command=button_props["command"],
                    fg=FG,
                    bg=BG,
                )
                self.project_command_buttons[button_key].grid(
                    row=button_props["row"],
                    column=button_props["column"],
                    columnspan=int(maxcol / 2),
                    pady=5,
                    padx=5,
                )
        self.reset_button = tk.Button(
            self.ui,
            text=button_commands["reset_button"]["title"],
            command=button_commands["reset_button"]["command"],
            fg=FG,
            bg=BG,
        )
        self.reset_button.grid(
            row=button_commands["reset_button"]["row"],
            column=button_commands["reset_button"]["column"],
            columnspan=maxcol,
        )
        self.reset_button.grid_remove()

        self.start_button = tk.Button(
            self.ui,
            text=button_commands["start_button"]["title"],
            command=button_commands["start_button"]["command"],
            fg=FG,
            bg=BG,
        )
        self.start_button.grid(
            row=button_commands["start_button"]["row"],
            column=button_commands["start_button"]["column"],
            columnspan=maxcol,
        )
        self.start_button.grid_remove()

    def hide_pre_load_buttons(self):
        self.project_command_label.grid_remove()
        self.reset_button.grid()
        self.start_button.grid()
        for buttons in self.button_commands["project_commands"]:
            for button_key in buttons:
                self.project_command_buttons[button_key].grid_remove()

    def reset_initialization(self):
        self.project_command_label.grid()
        self.reset_button.grid_remove()
        self.start_button.grid_remove()
        self.project_init_status.config(text="Project: Not Initialized")
        for buttons in self.button_commands["project_commands"]:
            for button_key in buttons:
                self.project_command_buttons[button_key].grid()