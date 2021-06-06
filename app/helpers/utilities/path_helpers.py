import json
from tkinter import filedialog
from pathlib import Path
from os import path as osPath
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
        sub_path = "gstr-utils-"
    except Exception:
        base_path = osPath.abspath(".")
        sub_path = ""

    return osPath.join(base_path, f"{sub_path}{relative_path}")


def get_json_sales_data(path_to_json):
    with open(file=path_to_json, mode="r") as json_data:
        sales_data = json.load(json_data)
        return sales_data


def get_user_json_directory(
    app_generation_mode, source_dir_entry, final_dir_entry, status_text
):

    if len(app_generation_mode) > 1:
        status_text.config(text="Status - Getting Directories")

        if app_generation_mode == "single":
            source_directory = filedialog.askopenfilename(
                title="Select the JSON File You want to Process",
                filetypes=[("Json", "*.json")],
            )
        elif app_generation_mode == "directory":
            source_directory = filedialog.askdirectory(
                title="Select the Folder where all the JSON Files are Located",
            )

        if len(source_directory) > 2:
            source_dir_entry.config(state="normal")
            source_dir_entry.delete(0, "end")
            source_dir_entry.insert(0, source_directory.lower())
            source_dir_entry.config(state="disabled")

            final_directory = filedialog.askdirectory(
                title="Select the Destination Directory to Store the Excel Files after Processing"
            )

            if len(final_directory) > 2:
                final_dir_entry.config(state="normal")
                final_dir_entry.delete(0, "end")
                final_dir_entry.insert(0, final_directory.lower())
                final_dir_entry.config(state="disabled")

            corrected_source_dir = (
                Path(source_directory.lower())
                if app_generation_mode == "single"
                else source_directory.lower() + "\\*.json"
            )

            ready_to_process = (
                True
                if len(source_directory) > 2 and len(final_directory) > 2
                else False
            )

            return {
                "ready_to_process": ready_to_process,
                "source_dir": corrected_source_dir,
                "final_dir": final_directory.lower(),
            }

        else:
            status_text.config(text="Status - Ready to Process")
            return {"ready_to_process": False, "source_dir": "", "final_dir": ""}