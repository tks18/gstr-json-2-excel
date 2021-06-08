BG = "#121212"
FG = "#FFFFFF"
ACCENT = "#e84545"

THEME = {"background": BG, "foreground": FG}

FONTS = {
    "small": ("Roboto", 10, "normal"),
    "small_bold": ("Roboto", 10, "bold"),
    "medium": ("Roboto", 12, "normal"),
    "medium_bold": ("Roboto", 12, "bold"),
    "title": ("Roboto", 20, "bold"),
    "title_big": ("Roboto", 25, "bold"),
    "buttons": {
        "small": ("Roboto", 9, "bold"),
        "medium": ("Roboto", 11, "bold"),
        "large": ("Roboto", 15, "bold"),
    },
}

TTK_THEME = {
    "TProgressbar": {
        "configure": {
            "troughcolor": BG,
            "bordercolor": FG,
            "background": ACCENT,
        }
    },
}
