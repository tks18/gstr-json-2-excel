import tkinter as tk
from app.common.helpers import resource_path

from app.common.ui.common import BG, FG


class base_ui:
    def __init__(self, window_title, title):
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

    def close_window(self):
        self.ui.destroy()

    def initialize_engine(self):
        self.ui.mainloop()