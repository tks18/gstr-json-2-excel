from app.helpers.ui.elements.button import small_button, medium_button, large_button
from app.helpers.ui.elements.label import small_label, medium_label, title_label
from app.helpers.ui.elements.checkbutton import check_btn
from app.helpers.ui.elements.radiobutton import radio_btn


class tk_elements:
    def __init__(self):
        # Buttons
        self.small_btn = small_button
        self.medium_btn = medium_button
        self.large_btn = large_button

        # labels
        self.small_lbl = small_label
        self.medium_lbl = medium_label
        self.title_lbl = title_label

        # others
        self.check_btn = check_btn
        self.radio_btn = radio_btn
