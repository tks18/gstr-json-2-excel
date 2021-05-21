import tkinter as tk
from app.common.helpers import resource_path

BG = "#121212"
FG = "#FFFFFF"


class gst_utils_ui:
    def __init__(self, window_title, title, commands, start_button):
        self.ui = tk.Tk()
        self.ui.title(window_title)
        self.ui.config(padx=40, pady=40, bg=BG)
        self.icon = tk.PhotoImage(file=resource_path("images/logo.png"))
        self.ui.iconphoto(False, self.icon)

        self.menuButton = tk.Button(
            self.ui, text="Menu", command=self.close_window, fg=FG, bg=BG
        )
        self.menuButton.grid(row=0, column=0)
        self.canvas = tk.Canvas(
            self.ui, height=200, width=200, highlightthickness=0, bg=BG
        )
        self.canvas.create_image(100, 100, image=self.icon)
        self.canvas.grid(row=1, column=0, columnspan=4)
        self.main_title = tk.Label(
            master=self.ui,
            text=title,
            font=("Courier new", 23, "bold"),
            pady=40,
            bg=BG,
            fg=FG,
        )
        self.ui.focus_force()
        self.main_title.grid(row=2, column=0, columnspan=4)

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

        self.source_dir_label = tk.Label(
            self.ui, text=" ", bg=BG, fg=FG, wraplength=450
        )
        self.source_dir_label.grid(row=7, column=0, columnspan=4)
        self.final_dir_label = tk.Label(self.ui, text=" ", bg=BG, fg=FG, wraplength=450)
        self.final_dir_label.grid(row=8, column=0, columnspan=4)

        self.start_gstr_1_process_button = tk.Button(
            self.ui, text="Start Processing", command=start_button, bg=BG, fg=FG
        )
        self.start_gstr_1_process_button.grid(row=9, column=0, columnspan=4)

        self.app_status_text = tk.Label(
            self.ui,
            text="Status - Ready to Process",
            bg=BG,
            fg=FG,
            padx=5,
            pady=5,
        )
        self.app_status_text.grid(row=10, column=0, columnspan=4)

        self.developer_label_head = tk.Label(self.ui, text="Developed by", bg=BG, fg=FG)
        self.developer_label_head.grid(row=11, column=0, columnspan=4)

        self.developer_label_value = tk.Label(
            self.ui, text="Shan.tk", font=("Courier New", 12, "bold"), bg=BG, fg=FG
        )
        self.developer_label_value.grid(row=12, column=0, columnspan=4)

    def close_window(self):
        self.ui.destroy()

    def initialize_engine(self):
        self.ui.mainloop()