from app.helpers.ui.helpers.base import base_ui


class main_window(base_ui):
    def __init__(self, window_title, title, buttons, menu):
        super(main_window, self).__init__(
            window_title=window_title, title=title, menu=menu, logo=True
        )

        self.ui.config(padx=60, pady=60)

        utility_label = self.elements.small_lbl(
            self, text="General Utilities", bold=True
        )
        utility_label.grid(row=3, column=0, columnspan=4)
        for btn in buttons["utility_buttons"]:
            new_btn = self.elements.small_btn(
                self, label=btn["title"], command=btn["command"]
            )
            new_btn.grid(row=btn["row"], column=btn["column"], pady=10, columnspan=2)

        reco_label = self.elements.small_lbl(
            self, text="Reconciliation Utilities", bold=True
        )
        reco_label.grid(row=5, column=0, columnspan=4)
        for btn in buttons["reco_buttons"]:
            new_btn = self.elements.small_btn(
                self, label=btn["title"], command=btn["command"]
            )
            new_btn.grid(row=btn["row"], column=btn["column"], pady=10, columnspan=4)
