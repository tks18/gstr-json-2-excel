import tkinter as tk
from app.common.ui.common import BG, FG


class check_box_window:
    def __init__(self, master, title, check_box_options, saved_options=None):
        self.ui = tk.Toplevel(master=master)
        self.ui.title(title)
        self.ui.config(bg=BG, padx=15, pady=7)

        self.check_box_options = [
            {key: prop} for (key, prop) in check_box_options.items()
        ]

        row = 0
        column = 0

        self.check_box_vars = {}
        self.check_boxes = {}
        for options in self.check_box_options:
            for (key, prop) in options.items():
                if saved_options:
                    self.check_box_vars[key] = tk.BooleanVar(
                        self.ui, saved_options[key]
                    )
                else:
                    self.check_box_vars[key] = tk.BooleanVar(self.ui, True)
                self.check_boxes[key] = tk.Checkbutton(
                    self.ui,
                    text=prop,
                    variable=self.check_box_vars[key],
                    fg=FG,
                    command=self.check_box_result_builder,
                    background=BG,
                    activebackground=BG,
                    activeforeground=FG,
                    highlightcolor=BG,
                    selectcolor=BG,
                    onvalue=True,
                    offvalue=False,
                )
                self.check_boxes[key].grid(row=row, column=column, padx=3)
            if column == 2:
                row += 1
                column = 0
            else:
                column += 1

        self.result = {}
        for keys in self.check_box_vars:
            self.result[keys] = self.check_box_vars[keys].get()

        self.select_all_checkbox_var = tk.BooleanVar(self.ui, True)
        for keys in self.result:
            if self.select_all_checkbox_var.get():
                if self.result[keys]:
                    self.select_all_checkbox_var.set(True)
                else:
                    self.select_all_checkbox_var.set(False)
            else:
                break

        self.select_all_checkbox = tk.Checkbutton(
            self.ui,
            text="Select All",
            variable=self.select_all_checkbox_var,
            fg=FG,
            command=self.select_all_command,
            background=BG,
            activebackground=BG,
            activeforeground=FG,
            highlightcolor=BG,
            selectcolor=BG,
            onvalue=True,
            offvalue=False,
        )
        self.select_all_checkbox.grid(row=row + 1, column=0, columnspan=4)
        self.ui.focus_force()

    def select_all_command(self):
        select_var_result = self.select_all_checkbox_var.get()
        for var_key in self.check_box_vars:
            self.check_box_vars[var_key].set(select_var_result)

    def check_box_result_builder(self):
        for keys in self.check_box_vars:
            self.result[keys] = self.check_box_vars[keys].get()

        temp_result = True
        for keys in self.result:
            if self.result[keys]:
                if self.select_all_checkbox_var.get():
                    self.select_all_checkbox_var.set(True)
                else:
                    if temp_result:
                        self.select_all_checkbox_var.set(True)
                    else:
                        break
            else:
                temp_result = False
                self.select_all_checkbox_var.set(False)
