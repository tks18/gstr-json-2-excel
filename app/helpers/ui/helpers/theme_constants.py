BG = "#121212"
FG = "#FFFFFF"
ACCENT = "#e84545"

THEME = {"background": BG, "foreground": FG}

FONTS = {
    "small": ("Arial", 10, "normal"),
    "small_bold": ("Arial", 10, "bold"),
    "medium": ("Arial", 12, "normal"),
    "medium_bold": ("Arial", 12, "bold"),
    "title": ("Arial", 25, "bold"),
    "buttons": {
        "small": ("Arial", 9, "bold"),
        "medium": ("Arial", 11, "bold"),
        "large": ("Arial", 15, "bold"),
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
