from os import error, mkdir, startfile
from pathlib import Path
from tkinter import messagebox
from app.reco.gstr_9c.generators.csv_template import generate_csv_template
from app.reco.gstr_9c.generators.project_configs import generate_project_config


def initialize_new_project(base_folder_path, project_name, year):
    modified_proj_name = f"{project_name} 9C-Project"
    all_paths = [
        {
            "path": Path(base_folder_path, modified_proj_name),
            "name": "base-folder",
            "text": False,
        },
        {
            "path": Path(base_folder_path, modified_proj_name, "GSTR 1 JSON"),
            "name": "gstr-1-json-folder",
            "text": True,
            "text_filename": Path(
                base_folder_path,
                modified_proj_name,
                "GSTR 1 JSON",
                "here_goes_gstr_1_json_files.txt",
            ),
            "text_content": "Paste all your GSTR 1 JSON Files in this Folder. Files can be named anything. Ensure it is Directly Downloaded from GST Portal",
        },
        {
            "path": Path(base_folder_path, modified_proj_name, "GSTR 3B JSON"),
            "name": "gstr-3b-json-folder",
            "text": True,
            "text_filename": Path(
                base_folder_path,
                modified_proj_name,
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
    generate_csv_template(Path(base_folder_path, modified_proj_name))
    project_config = generate_project_config(
        project_title=project_name,
        base_path=all_paths[0]["path"],
        year=year,
        paths=all_paths,
    )

    return project_config
