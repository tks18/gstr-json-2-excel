import tkinter as tk

from app.helpers.ui.helpers.base import base_ui
from app.helpers.ui.sub_windows.check_box_window import check_box_window


class gst_utils_ui(base_ui):
    def __init__(self, window_title, title, commands, start_button):
        super(gst_utils_ui, self).__init__(
            window_title=window_title, title=title, menu=False, logo=False
        )
        self.app_generation_mode_label = self.elements.small_lbl(
            self, text="Select App Working Mode", bold=False
        )
        self.app_generation_mode_label.grid(row=3, column=0, columnspan=4)
        self.app_generation_mode_var = tk.StringVar(self.ui, "single")
        app_generation_modes = {
            "Single": {"value": "single", "row": 4, "column": 0, "span": 2},
            "Directory": {"value": "directory", "row": 4, "column": 2, "span": 2},
        }
        for (modes, mode_vals) in app_generation_modes.items():
            self.elements.radio_btn(
                self,
                text=modes,
                variable=self.app_generation_mode_var,
                value=mode_vals["value"],
                command=commands["app_generation"],
            ).grid(
                row=mode_vals["row"],
                column=mode_vals["column"],
                columnspan=mode_vals["span"],
            )

        self.app_processing_mode_label = self.elements.small_lbl(
            self, text="Select File Processing Mode", bold=False
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
            self.elements.radio_btn(
                self,
                text=modes,
                variable=self.app_processing_mode_var,
                value=mode_vals["value"],
                command=commands["app_processing"],
            ).grid(row=mode_vals["row"], column=mode_vals["column"])

        self.invoice_config_button = self.elements.small_btn(
            self,
            label="Select Invoices to Extract",
            command=self.wait_for_checkbox_selector,
        )

        self.invoice_extract_options_selected = commands["invoice_extract_options"][
            "default_vals"
        ]
        self.invoices_config_options = commands["invoice_extract_options"]["options"]

        self.invoice_config_button.grid(row=7, column=0, columnspan=4)

        self.source_dir_label = self.elements.small_lbl(
            self, text="Source: ", bold=False
        )
        self.source_dir_label.grid(row=8, column=0, columnspan=1, pady=(10, 0))
        self.source_dir_entry = tk.Entry(
            self.ui,
            state="disabled",
            width=40,
            **self.theme,
            disabledbackground=self.bg,
            disabledforeground=self.fg,
            insertbackground=self.fg,
            highlightcolor=self.fg,
            highlightbackground=self.fg,
        )
        self.source_dir_entry.grid(row=8, column=1, columnspan=3, pady=(10, 0))

        self.final_dir_label = self.elements.small_lbl(self, text="Dest: ", bold=False)
        self.final_dir_label.grid(row=9, column=0, columnspan=1, pady=(0, 10))
        self.final_dir_entry = tk.Entry(
            self.ui,
            state="disabled",
            width=40,
            **self.theme,
            disabledbackground=self.bg,
            disabledforeground=self.fg,
            insertbackground=self.fg,
            highlightcolor=self.fg,
            highlightbackground=self.fg,
        )
        self.final_dir_entry.grid(row=9, column=1, columnspan=3, pady=(0, 10))

        self.start_gstr_1_process_button = self.elements.medium_btn(
            self,
            label="Start Processing",
            command=start_button,
        )
        self.start_gstr_1_process_button.grid(row=10, column=0, columnspan=4)

        self.open_final_dir_var = tk.BooleanVar(self.ui, False)
        self.open_final_dir_checkButton = self.elements.check_btn(
            self,
            text="Open the Destination Directory after Finish",
            variable=self.open_final_dir_var,
        )
        self.open_final_dir_checkButton.grid(row=11, column=0, columnspan=4)

        self.app_status_text = self.elements.small_lbl(
            self, text="Status - Ready to Process", bold=True
        )
        self.app_status_text.grid(row=12, column=0, columnspan=4)

    def wait_for_checkbox_selector(self):
        self.check_box_ui = check_box_window(
            self,
            "Select Invoices to Extract",
            self.invoices_config_options,
            self.invoice_extract_options_selected,
        )
        self.ui.wait_window(self.check_box_ui.ui)
        self.invoice_extract_options_selected = self.check_box_ui.result
