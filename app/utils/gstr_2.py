import glob
from os import error, mkdir, startfile
from pathlib import Path
from tkinter import messagebox
from openpyxl import Workbook

# Other Imports
from app.helpers.ui.main_windows.utils_ui import gst_utils_ui
from app.helpers.ui.sub_windows.loader_window import loader_window
from app.helpers.utilities.invoice_writer import invoices_writer
from app.helpers.utilities.path_helpers import (
    get_user_json_directory,
    get_json_sales_data,
)
from app.helpers.utilities.basic_data_writer import write_basic_data_sheet
from app.helpers.utilities.archive import make_archive

# heading map imports
from app.helpers.heading_maps.gstr_2 import *


def generate_basic_data(path_to_json):

    not_required_keys = [
        "b2b",
        "cdn",
        "b2ba",
    ]
    data = get_json_sales_data(path_to_json)
    for key in not_required_keys:
        if key in data:
            data.pop(key)

    return data


def write_all_invoices(
    config_map,
    gen_excel,
    gen_json,
    path_to_json,
    basic_data,
    work_book,
    file_directory,
    file_name,
    zip_it,
    zip_file_name,
):

    invoice_config_list = []

    b2b_config = {
        "title": "B2B",
        "list_name": "b2b",
        "invoice_item_name": "inv",
        "heading_map": b2b_heading_map,
        "file_name": file_directory + "/" + file_name + "_GSTR_2A_b2b_sales.json",
    }
    b2b_cdnr_config = {
        "title": "B2B Credit Notes",
        "list_name": "cdn",
        "invoice_item_name": "nt",
        "heading_map": b2b_credit_notes_headings_map,
        "file_name": file_directory
        + "/"
        + file_name
        + "_GSTR_2A_b2b_sales_returns.json",
    }
    b2ba_config = {
        "title": "B2B-Amendments",
        "list_name": "b2ba",
        "invoice_item_name": "inv",
        "heading_map": b2ba_heading_map,
        "file_name": file_directory + "/" + file_name + "_GSTR_2A_b2ba_sales.json",
    }

    if config_map["b2b"]:
        invoice_config_list.append(b2b_config)
    if config_map["b2b_cdnr"]:
        invoice_config_list.append(b2b_cdnr_config)
    if config_map["b2ba"]:
        invoice_config_list.append(b2ba_config)

    if gen_excel:
        write_basic_data_sheet(
            work_book=work_book,
            basic_data=basic_data,
            heading_map=basic_data_heading_map,
        )

    for config in invoice_config_list:
        invoices_writer(
            work_book=work_book,
            sheet_name=config["title"],
            file_name=config["file_name"],
            sales_data_list_name=config["list_name"],
            invoice_item_name=config["invoice_item_name"],
            gen_excel=gen_excel,
            gen_json=gen_json,
            heading_map=config["heading_map"],
            path_to_json=path_to_json,
        )

    if gen_excel:
        work_book.save(file_directory + "/GSTR_2A_" + file_name + ".xlsx")

    if zip_it:
        try:
            make_archive(path_to_files=file_directory, file_name=zip_file_name)
        except error:
            print(error)


def start_gstr_2_process():
    global basic_data, app_mode, app_generation_mode, extract_invoice_config, force_close
    global create_file_dir_modes, create_excel_dir_modes, gstr_2_ui
    global work_book, file_name, file_directory, loader_sub_window

    user_input_dirs = get_user_json_directory(
        app_generation_mode=app_generation_mode,
        source_dir_entry=gstr_2_ui.source_dir_entry,
        final_dir_entry=gstr_2_ui.final_dir_entry,
        status_text=gstr_2_ui.app_status_text,
    )

    if user_input_dirs["ready_to_process"]:
        user_confirmation_dialog = messagebox.askyesno(
            title="Confirm Proceed",
            message="Are You Sure with the Details you have Provided ?",
        )

        if user_confirmation_dialog:
            json_files = []
            if app_generation_mode == "single":
                json_files.append(user_input_dirs["source_dir"])
            elif app_generation_mode == "directory":
                gstr_2_ui.app_status_text.config(
                    text="Status - Batch Processing the Files"
                )
                for json_file in glob.glob(user_input_dirs["source_dir"]):
                    json_files.append(Path(json_file.lower()))

            for json_file in json_files:

                work_book = Workbook()
                work_book.active

                basic_data = generate_basic_data(
                    path_to_json=json_file,
                )

                file_name = basic_data["gstin"] + "_" + basic_data["fp"]
                file_directory = (
                    user_input_dirs["final_dir"] + "/" + file_name
                    if app_mode in create_file_dir_modes
                    else user_input_dirs["final_dir"]
                )

                try:
                    if app_mode in create_file_dir_modes:
                        corrected_dest_file = Path(
                            user_input_dirs["final_dir"] + "/" + file_name
                        )
                        mkdir(corrected_dest_file)
                except OSError:
                    gstr_2_ui.app_status_text.config(text="Status - Folder Error - ")
                else:
                    config_map = gstr_2_ui.invoice_extract_options_selected

                    gen_json = app_mode in create_file_dir_modes
                    gen_excel = app_mode in create_excel_dir_modes
                    zip_it = app_mode == "zipped"

                    gstr_2_ui.ui.withdraw()

                    loader_sub_window = loader_window(
                        master=gstr_2_ui,
                        title=f"Processing - {basic_data['fp']}",
                        text="Please Wait while we Process the Data, Take a Sip of Coffee till we finish",
                        function=write_all_invoices,
                        config_map=config_map,
                        gen_excel=gen_excel,
                        gen_json=gen_json,
                        path_to_json=json_file,
                        basic_data=basic_data,
                        work_book=work_book,
                        file_directory=file_directory,
                        file_name=file_name,
                        zip_it=zip_it,
                        zip_file_name=Path(
                            user_input_dirs["final_dir"] + "/GSTR_2A_" + file_name
                        ),
                    )

                    gstr_2_ui.ui.wait_window(loader_sub_window.ui)

                    open_final_dir = gstr_2_ui.open_final_dir_var.get()
                    if open_final_dir:
                        if (
                            app_mode in ["json", "excel-json"]
                            and app_generation_mode == "single"
                        ):
                            startfile(
                                user_input_dirs["final_dir"] + "/" + file_name, "open"
                            )
                        else:
                            startfile(user_input_dirs["final_dir"], "open")
            gstr_2_ui.ui.deiconify()

            restart_app_input = messagebox.askyesno(
                title="Restart App",
                message="App has Finished Processing the Files\n\nDo you like to Restart the App ?",
            )
            if restart_app_input:
                gstr_2_ui.source_dir_entry.config(state="normal")
                gstr_2_ui.final_dir_entry.config(state="normal")
                gstr_2_ui.source_dir_entry.delete(0, "end")
                gstr_2_ui.final_dir_entry.delete(0, "end")
                gstr_2_ui.source_dir_entry.config(state="disabled")
                gstr_2_ui.final_dir_entry.config(state="disabled")
            else:
                force_close = True
                gstr_2_ui.close_window()

        else:
            gstr_2_ui.app_status_text.config(text="Status - Ready to Process")
            gstr_2_ui.source_dir_entry.config(state="normal")
            gstr_2_ui.final_dir_entry.config(state="normal")
            gstr_2_ui.source_dir_entry.delete(0, "end")
            gstr_2_ui.final_dir_entry.delete(0, "end")
            gstr_2_ui.source_dir_entry.config(state="disabled")
            gstr_2_ui.final_dir_entry.config(state="disabled")


def set_app_generation_mode():
    global app_generation_mode

    app_generation_mode = gstr_2_ui.app_generation_mode_var.get()


def set_app_processing_mode():
    global app_mode

    app_mode = gstr_2_ui.app_processing_mode_var.get()


def set_extract_invoice_config(event=None):
    global gstr_2_ui, extract_invoice_config, extract_invoice_options

    option_selected = gstr_2_ui.invoice_config_var.get()

    for (option_key, option_value) in extract_invoice_options.items():
        if option_value == option_selected:
            extract_invoice_config = option_key


def initiate_force_close():
    global gstr_2_ui, force_close

    gstr_2_ui.close_window()
    force_close = True


def start_window_app():
    global gstr_2_ui, force_close, extract_invoice_options, extract_invoice_default_options

    gstr_2_ui = gst_utils_ui(
        window_title="GSTR 2A Utilities",
        title="Convert GSTR 2A JSON to Excel or Consumable JSON",
        commands={
            "app_generation": set_app_generation_mode,
            "app_processing": set_app_processing_mode,
            "invoice_extract_options": {
                "options": extract_invoice_options,
                "default_vals": extract_invoice_default_options,
                "default": "All Invoices",
                "command": set_extract_invoice_config,
            },
        },
        start_button=start_gstr_2_process,
    )

    gstr_2_ui.ui.protocol("WM_DELETE_WINDOW", initiate_force_close)

    gstr_2_ui.initialize_engine()

    return force_close


gstr_2_ui = None
loader_sub_window = None

basic_data = {}
force_close = False

app_mode = "excel"
app_generation_mode = "single"

extract_invoice_config = "all"
extract_invoice_options = {
    "b2b": "B2B Invoices",
    "b2b_cdnr": "B2B Credit Notes",
    "b2ba": "B2B Amendments",
}
extract_invoice_default_options = {
    "b2b": True,
    "b2b_cdnr": True,
    "b2ba": True,
}

create_file_dir_modes = ["excel-json", "zipped", "json"]
create_excel_dir_modes = ["excel-json", "zipped", "excel"]

work_book = None

file_name = ""
file_directory = ""
