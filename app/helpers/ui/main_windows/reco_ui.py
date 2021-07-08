from app.helpers.ui.helpers.base import base_ui


class gst_reco_ui(base_ui):
    def __init__(self, window_title, title, button_commands):
        maxcol = 8
        super(gst_reco_ui, self).__init__(
            window_title=window_title,
            title=title,
            menu=False,
            logo=False,
            maxcol=maxcol,
        )

        self.button_commands = button_commands

        self.project_init_status = self.elements.small_lbl(
            self, text="Project: Not Initialized", bold=False
        )
        self.project_init_status.grid(row=3, column=0, columnspan=maxcol, pady=(0, 10))

        self.project_command_label = self.elements.small_lbl(
            self, text="Manage Project", bold=False
        )
        self.project_command_label.grid(row=4, column=0, columnspan=maxcol)

        self.project_command_buttons = {}
        for buttons in button_commands["project_commands"]:
            for (button_key, button_props) in buttons.items():
                self.project_command_buttons[button_key] = self.elements.small_btn(
                    self, label=button_key, command=button_props["command"]
                )
                self.project_command_buttons[button_key].grid(
                    row=button_props["row"],
                    column=button_props["column"],
                    columnspan=int(maxcol / 2),
                    pady=5,
                    padx=5,
                )
        self.reset_button = self.elements.small_btn(
            self,
            label=button_commands["reset_button"]["title"],
            command=button_commands["reset_button"]["command"],
        )
        self.reset_button.grid(
            row=button_commands["reset_button"]["row"],
            column=button_commands["reset_button"]["column"],
            columnspan=maxcol,
        )
        self.reset_button.grid_remove()

        self.start_button = self.elements.medium_btn(
            self,
            label=button_commands["start_button"]["title"],
            command=button_commands["start_button"]["command"],
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