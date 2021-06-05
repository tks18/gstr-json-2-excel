import tkinter as tk
from app.helpers.ui.common import BG, FG


class text_box_window:
    def __init__(self, master, title, labels):
        self.ui = tk.Toplevel(master=master)
        self.ui.title(title)
        self.ui.config(bg=BG, padx=15, pady=7)

        self.label_props = labels
        self.label = {}
        self.text_box = {}
        row_no = 0
        for (label_key, label_text) in labels.items():
            self.label[label_key] = tk.Label(
                self.ui, text=f"{label_text}: ", bg=BG, fg=FG
            )
            self.label[label_key].grid(
                row=row_no, column=0, columnspan=1, padx=5, pady=5
            )

            self.text_box[label_key] = tk.Entry(
                self.ui,
                width=40,
                bg=BG,
                fg=FG,
                insertbackground=FG,
                highlightcolor=FG,
                highlightthickness=1,
                highlightbackground=FG,
            )
            self.text_box[label_key].grid(
                row=row_no, column=1, columnspan=2, padx=5, pady=5
            )
            if row_no == 0:
                self.text_box[label_key].focus()
            self.text_box[label_key].bind("<Return>", self.accept_action)
            self.text_box[label_key].bind("<Escape>", self.cancel_action)
            row_no += 1

        self.ui.protocol("WM_DELETE_WINDOW", self.cancel_action)

        self.accept_button = tk.Button(
            self.ui, text="Accept", command=self.accept_action, bg=BG, fg=FG
        )
        self.accept_button.grid(row=row_no + 1, column=0, columnspan=2)

        self.cancel_button = tk.Button(
            self.ui, text="Cancel", command=self.accept_action, bg=BG, fg=FG
        )
        self.cancel_button.grid(row=row_no + 1, column=1, columnspan=2)

        self.result = {"success": True}

    def accept_action(self, event=None):
        for label_key in self.label_props:
            project_text = self.text_box[label_key].get()
            if len(project_text) < 5:
                self.result["success"] = False
            else:
                self.result["success"] = True
            self.result[label_key] = project_text
        self.ui.destroy()

    def cancel_action(self, event=None):
        self.result["success"] = False
        self.ui.destroy()
