import tkinter as tk

from app.helpers.ui.base import base_ui
from app.helpers.ui.check_box_window import check_box_window
from app.helpers.ui.common import BG, FG


class gst_utils_ui(base_ui):
    def __init__(self, window_title, title, commands, start_button, menu):
        super(gst_utils_ui, self).__init__(window_title, title, menu)
        self.app_generation_mode_label = tk.Label(
            self.ui, text="Select App Working Mode", bg=BG, fg=FG
        )
        self.app_generation_mode_label.grid(row=3, column=0, columnspan=4)
        self.app_generation_mode_var = tk.StringVar(self.ui, "single")
        app_generation_modes = {
            "Single": {"value": "single", "row": 4, "column": 0, "span": 2},
            "Directory": {"value": "directory", "row": 4, "column": 2, "span": 2},
        }
        for (modes, mode_vals) in app_generation_modes.items():
            tk.Radiobutton(
                self.ui,
                text=modes,
                variable=self.app_generation_mode_var,
                value=mode_vals["value"],
                bg=BG,
                fg=FG,
                selectcolor=BG,
                command=commands["app_generation"],
            ).grid(
                row=mode_vals["row"],
                column=mode_vals["column"],
                columnspan=mode_vals["span"],
            )

        self.app_processing_mode_label = tk.Label(
            self.ui, text="Select File Processing Mode", bg=BG, fg=FG
        )
        self.app_processing_mode_var = tk.StringVar(self.ui, "excel")
        self.app_processing_mode_label.grid(row=5, column=0, columnspan=4)
        app_processing_modes = {
            "Excel Only": {
                "value": "excel",
                "row": 6,
                "column": 0,
            },
            "JSON Only": {
                "value": "json",
                "row": 6,
                "column": 1,
            },
            "Zipped": {
                "value": "zipped",
                "row": 6,
                "column": 2,
            },
            "Excel with JSON": {"value": "excel-json", "row": 6, "column": 3},
        }

        for (modes, mode_vals) in app_processing_modes.items():
            tk.Radiobutton(
                self.ui,
                text=modes,
                variable=self.app_processing_mode_var,
                value=mode_vals["value"],
                bg=BG,
                fg=FG,
                selectcolor=BG,
                command=commands["app_processing"],
            ).grid(row=mode_vals["row"], column=mode_vals["column"])

        self.invoice_config_button = tk.Button(
            self.ui,
            text="Select Invoices to Extract",
            command=self.wait_for_checkbox_selector,
            fg=FG,
            bg=BG,
        )

        self.invoice_extract_options_selected = None
        self.invoices_config_options = commands["invoice_extract_options"]["options"]

        self.invoice_config_button.grid(row=7, column=0, columnspan=4)

        self.source_dir_label = tk.Label(
            self.ui, text="Source: ", bg=BG, fg=FG, wraplength=450
        )
        self.source_dir_label.grid(row=8, column=0, columnspan=1, pady=(10, 0))
        self.source_dir_entry = tk.Entry(
            self.ui,
            state="disabled",
            width=40,
            disabledbackground=BG,
            background=BG,
            disabledforeground=FG,
            foreground=FG,
            insertbackground=FG,
            highlightcolor=FG,
            highlightbackground=FG,
        )
        self.source_dir_entry.grid(row=8, column=1, columnspan=3, pady=(10, 0))

        self.final_dir_label = tk.Label(
            self.ui, text="Dest: ", bg=BG, fg=FG, wraplength=450
        )
        self.final_dir_label.grid(row=9, column=0, columnspan=1, pady=(0, 10))
        self.final_dir_entry = tk.Entry(
            self.ui,
            state="disabled",
            width=40,
            disabledbackground=BG,
            background=BG,
            disabledforeground=FG,
            foreground=FG,
            insertbackground=FG,
            highlightcolor=FG,
            highlightbackground=FG,
        )
        self.final_dir_entry.grid(row=9, column=1, columnspan=3, pady=(0, 10))

        self.start_gstr_1_process_button = tk.Button(
            self.ui, text="Start Processing", command=start_button, bg=BG, fg=FG
        )
        self.start_gstr_1_process_button.grid(row=10, column=0, columnspan=4)

        self.open_final_dir_var = tk.BooleanVar(self.ui, False)
        self.open_final_dir_checkButton = tk.Checkbutton(
            self.ui,
            text="Open the Destination Directory after Finish",
            variable=self.open_final_dir_var,
            fg=FG,
            background=BG,
            activebackground=BG,
            activeforeground=FG,
            highlightcolor=BG,
            selectcolor=BG,
            onvalue=True,
            offvalue=False,
        )
        self.open_final_dir_checkButton.grid(row=11, column=0, columnspan=4)

        self.app_status_text = tk.Label(
            self.ui,
            text="Status - Ready to Process",
            bg=BG,
            fg=FG,
            padx=5,
            pady=5,
        )
        self.app_status_text.grid(row=12, column=0, columnspan=4)

    def wait_for_checkbox_selector(self):
        self.check_box_ui = check_box_window(
            self.ui,
            "Select Invoices to Extract",
            self.invoices_config_options,
            self.invoice_extract_options_selected,
        )
        self.ui.wait_window(self.check_box_ui.ui)
        self.invoice_extract_options_selected = self.check_box_ui.result
