import tkinter as tk
from tkinter.ttk import Progressbar
from app.helpers.threader import threader
from app.helpers.utilities.path_helpers import resource_path


class loader_window:
    def __init__(self, master, title, text, function, **function_args):
        self.ui = tk.Toplevel(master=master.ui)
        self.ui.title(title)
        self.ui.config(bg=master.bg, padx=15, pady=7)
        self.icon = tk.PhotoImage(file=resource_path("images/logo.png"))
        self.ui.iconphoto(False, self.icon)

        self.function = function
        self.function_args = function_args

        self.loader = Progressbar(
            self.ui,
            orient="horizontal",
            length=400,
            mode="indeterminate",
            takefocus=True,
            maximum=100,
        )
        self.loader.pack()

        self.label = tk.Label(
            master=self.ui, text=text, **master.theme, font=master.FONTS["small_bold"]
        )
        self.label.pack()
        self.loader.start()
        self.ui.focus_force()
        self.ui.after(200, self.start_function)

    def start_function(self):
        self.thread = threader(function=self.function, **self.function_args)
        self.thread.start()
        self.check_alive()

    def check_alive(self):
        try:
            thread_status = self.thread.get_status()

            if thread_status["alive"] and thread_status["error"] is None:
                self.ui.after(200, self.check_alive)
            else:
                self.ui.destroy()
        except Exception:
            self.ui.destroy()
