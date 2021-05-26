import tkinter as tk
from app.common.ui.common import BG, FG


class text_box_window:
    def __init__(self, master, title, label):
        self.ui = tk.Toplevel(master=master)
        self.ui.title(title)
        self.ui.config(bg=BG, padx=15, pady=7)

        self.label = tk.Label(self.ui, text=f"{label}: ", bg=BG, fg=FG)
        self.label.grid(row=0, column=0, columnspan=1, padx=5, pady=5)

        self.text_box = tk.Entry(
            self.ui,
            width=40,
            bg=BG,
            fg=FG,
            insertbackground=FG,
            highlightcolor=FG,
            highlightthickness=2,
            highlightbackground=FG,
        )
        self.text_box.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        self.text_box.focus()
        self.text_box.bind("<Return>", self.accept_action)
        self.text_box.bind("<Escape>", self.cancel_action)
        self.ui.protocol("WM_DELETE_WINDOW", self.cancel_action)

        self.accept_button = tk.Button(
            self.ui, text="Accept", command=self.accept_action, bg=BG, fg=FG
        )
        self.accept_button.grid(row=1, column=0, columnspan=2)

        self.cancel_button = tk.Button(
            self.ui, text="Cancel", command=self.accept_action, bg=BG, fg=FG
        )
        self.cancel_button.grid(row=1, column=1, columnspan=2)

        self.result = {"success": True, "text": ""}

    def accept_action(self, event=None):
        project_text = self.text_box.get()
        if len(project_text) < 5:
            self.result["success"] = False
        else:
            self.result["success"] = True
        self.result["text"] = project_text
        self.ui.destroy()

    def cancel_action(self, event=None):
        self.result["success"] = False
        self.ui.destroy()
