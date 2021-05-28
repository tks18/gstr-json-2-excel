import tkinter as tk
from tkinter.ttk import Progressbar
from app.common.threader import threader

from app.common.ui.common import BG, FG


class loader_window:
    def __init__(self, master, title, text, function, **function_args):
        self.ui = tk.Toplevel(master=master)
        self.ui.title(title)
        self.ui.config(bg=BG, padx=15, pady=7)

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

        self.label = tk.Label(master=self.ui, text=text, fg=FG, bg=BG)
        self.label.pack()
        self.loader.start()
        self.ui.focus_force()
        self.ui.after(200, self.start_function)

    def start_function(self):
        self.thread = threader(function=self.function, **self.function_args)
        self.thread.start()
        self.check_alive()
    
    def check_alive(self):
        
        if self.thread.is_alive():
            self.ui.after(200, self.check_alive)
        else:
            self.ui.destroy()