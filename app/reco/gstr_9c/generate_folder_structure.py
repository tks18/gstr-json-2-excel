from os import error, mkdir, startfile
from pathlib import Path
from tkinter import messagebox
from app.reco.gstr_9c.generate_csv_template import generate_csv_template


def generate_folder_structure(base_folder_path):
    all_paths = [
        {
            "path": Path(base_folder_path, "GSTR_9C_UTILITY"),
            "text": False,
        },
        {
            "path": Path(base_folder_path, "GSTR_9C_UTILITY", "GSTR 1 JSON"),
            "text": True,
            "text_filename": Path(
                base_folder_path,
                "GSTR_9C_UTILITY",
                "GSTR 1 JSON",
                "here_goes_gstr_1_json_files.txt",
            ),
            "text_content": "Paste all your GSTR 1 JSON Files in this Folder. Files can be named anything. Ensure it is Directly Downloaded from GST Portal",
        },
        {
            "path": Path(base_folder_path, "GSTR_9C_UTILITY", "GSTR 3B JSON"),
            "text": True,
            "text_filename": Path(
                base_folder_path,
                "GSTR_9C_UTILITY",
                "GSTR 3B JSON",
                "here_goes_gstr_3b_json_files.txt",
            ),
            "text_content": "Paste all your GSTR 3B JSON Files in this Folder. Files can be named anything. Ensure it is Directly Downloaded from GST Portal",
        },
    ]

    for gen_path in all_paths:
        try:
            mkdir(gen_path["path"])
        except error:
            messagebox.showerror(
                title="Error Generating Folder",
                message="Error Popped up while Generating the Folder Structure, Try Redoing with proper Folder.",
            )
        else:
            if gen_path["text"]:
                with open(gen_path["text_filename"], mode="w") as gen_path_text:
                    gen_path_text.write(gen_path["text_content"])

    startfile(all_paths[0]["path"])
    generate_csv_template(Path(base_folder_path, "GSTR_9C_UTILITY"))