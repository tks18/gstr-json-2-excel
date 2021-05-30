import glob
from os import error, mkdir, startfile
from pathlib import Path
from tkinter import messagebox
from openpyxl import Workbook

# Other Imports
from app.common.ui.utils import gst_utils_ui
from app.common.ui.loader import loader_window
from app.common.helpers import (
    get_user_json_directory,
    get_json_sales_data,
    write_basic_data_sheet,
    generate_invoices_list,
    write_invoices_to_excel,
    make_archive,
)

# heading map imports
from app.common.heading_maps.gstr_2 import *


def generate_basic_data(path_to_json):

    # not_required_keys = [
    #     "b2b",
    #     "cdnr",
    #     "exp",
    #     "b2cs",
    #     "b2cl",
    #     "b2ba",
    #     "hsn",
    #     "cdnur",
    #     "b2csa",
    #     "cdnra",
    #     "expa",
    #     "doc_issue",
    # ]

    not_required_keys = [
        "b2b",
        "cdn",
        "b2ba",
        "cdnur",
        "b2csa",
        "cdnra",
        "expa",
        "doc_issue",
    ]
    data = get_json_sales_data(path_to_json)
    for key in not_required_keys:
        if key in data:
            data.pop(key)

    return data


def write_basic_data(work_book, basic_data):

    basic_data_sheet = work_book["Sheet"]
    basic_data_sheet.title = "Basic Data"

    write_basic_data_sheet(
        work_sheet=basic_data_sheet,
        basic_data=basic_data,
        heading_map=basic_data_heading_map,
    )


def write_b2b_invoices(
    work_book,
    file_name,
    gen_json,
    gen_excel,
    path_to_json,
    destination,
):

    invoice_list = []
    b2b_heading_list = [heading for heading in b2b_heading_map]

    sales_data = get_json_sales_data(path_to_json)
    if "b2b" in sales_data:

        invoice_list = generate_invoices_list(
            sales_data=sales_data,
            sales_type="b2b",
            invoice_term="inv",
            gen_json=gen_json,
            file_name=destination + "/" + file_name + "_GSTR_2A_b2b_sales.json",
        )

        if gen_excel:
            b2b_sheet = work_book.create_sheet("B2B")
            write_invoices_to_excel(
                work_sheet=b2b_sheet,
                invoice_list=invoice_list,
                heading_map=b2b_heading_map,
                heading_list=b2b_heading_list,
            )


def write_b2b_credit_note_invoices(
    work_book,
    file_name,
    gen_json,
    gen_excel,
    path_to_json,
    destination,
):

    invoice_list = []

    b2b_credit_notes_headings_list = [
        heading for heading in b2b_credit_notes_headings_map
    ]

    sales_data = get_json_sales_data(path_to_json)
    if "cdn" in sales_data:

        invoice_list = generate_invoices_list(
            sales_data=sales_data,
            sales_type="cdn",
            invoice_term="nt",
            gen_json=gen_json,
            file_name=destination + "/" + file_name + "_GSTR_2A_b2b_sales_returns.json",
        )

        if gen_excel:
            b2b_credit_notes_sheet = work_book.create_sheet(title="CDNR")
            write_invoices_to_excel(
                work_sheet=b2b_credit_notes_sheet,
                invoice_list=invoice_list,
                heading_map=b2b_credit_notes_headings_map,
                heading_list=b2b_credit_notes_headings_list,
            )


def write_b2ba_invoices(
    work_book,
    file_name,
    gen_json,
    gen_excel,
    path_to_json,
    destination,
):

    invoice_list = []

    b2ba_heading_list = [heading for heading in b2ba_heading_map]
    sales_data = get_json_sales_data(path_to_json)
    if "b2ba" in sales_data:

        invoice_list = generate_invoices_list(
            sales_data=sales_data,
            sales_type="b2ba",
            invoice_term="inv",
            gen_json=gen_json,
            file_name=destination + "/" + file_name + "_GSTR_2A_b2ba_sales.json",
        )

        if gen_excel:
            b2ba_sheet = work_book.create_sheet(title="B2BA")
            write_invoices_to_excel(
                work_sheet=b2ba_sheet,
                invoice_list=invoice_list,
                heading_map=b2ba_heading_map,
                heading_list=b2ba_heading_list,
            )


def write_all_invoices(
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

    if gen_excel:
        write_basic_data(
            work_book=work_book,
            basic_data=basic_data,
        )
    write_b2b_invoices(
        work_book=work_book,
        file_name=file_name,
        gen_excel=gen_excel,
        gen_json=gen_json,
        path_to_json=path_to_json,
        destination=file_directory,
    )
    write_b2b_credit_note_invoices(
        work_book=work_book,
        file_name=file_name,
        gen_excel=gen_excel,
        gen_json=gen_json,
        path_to_json=path_to_json,
        destination=file_directory,
    )
    write_b2ba_invoices(
        work_book=work_book,
        file_name=file_name,
        gen_excel=gen_excel,
        gen_json=gen_json,
        path_to_json=path_to_json,
        destination=file_directory,
    )
    if gen_excel:
        work_book.save(file_directory + "/GSTR_2A_" + file_name + ".xlsx")

    if zip_it:
        try:
            make_archive(path_to_files=file_directory, file_name=zip_file_name)
        except error:
            print(error)


def start_gstr_2_process():
    global basic_data, app_mode, app_generation_mode, force_close
    global create_file_dir_modes, create_excel_dir_modes, gstr_2_ui
    global work_book, file_name, file_directory, loader_sub_window

    user_input_dirs = get_user_json_directory(
        app_generation_mode=app_generation_mode,
        source_dir_label=gstr_2_ui.source_dir_label,
        final_dir_label=gstr_2_ui.final_dir_label,
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
                    gen_json = app_mode in create_file_dir_modes
                    gen_excel = app_mode in create_excel_dir_modes
                    zip_it = app_mode == "zipped"

                    gstr_2_ui.ui.withdraw()

                    loader_sub_window = loader_window(
                        master=gstr_2_ui.ui,
                        title=f"Processing - {basic_data['fp']}",
                        text="Please Wait while we Process the Data, Take a Sip of Coffee till we finish",
                        function=write_all_invoices,
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
                gstr_2_ui.source_dir_label.config(text=" ")
                gstr_2_ui.final_dir_label.config(text=" ")
            else:
                force_close = True
                gstr_2_ui.close_window()

        else:
            gstr_2_ui.app_status_text.config(text="Status - Ready to Process")
            gstr_2_ui.source_dir_label.config(text=" ")
            gstr_2_ui.final_dir_label.config(text=" ")


def set_app_generation_mode():
    global app_generation_mode

    app_generation_mode = gstr_2_ui.app_generation_mode_var.get()


def set_app_processing_mode():
    global app_mode

    app_mode = gstr_2_ui.app_processing_mode_var.get()


def initiate_force_close():
    global gstr_2_ui, force_close

    gstr_2_ui.close_window()
    force_close = True


def start_window_app():
    global gstr_2_ui, force_close

    gstr_2_ui = gst_utils_ui(
        window_title="GSTR 2A Utils",
        title="GSTR 2A Utility",
        commands={
            "app_generation": set_app_generation_mode,
            "app_processing": set_app_processing_mode,
        },
        start_button=start_gstr_2_process,
        menu=True,
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

create_file_dir_modes = ["excel-json", "zipped", "json"]
create_excel_dir_modes = ["excel-json", "zipped", "excel"]

work_book = None

file_name = ""
file_directory = ""