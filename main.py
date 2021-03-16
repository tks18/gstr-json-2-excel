import json
from flatten_json import flatten

from pathlib import Path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

work_book = Workbook()
work_book.active

basic_data = {}


def get_user_json_directory():
    directory = input("Enter the Sales Json Directory:  ").lower()
    correct_dir = Path(directory)
    return correct_dir


def get_json_sales_data(path_to_json):
    with open(path_to_json, mode="r") as json_data:
        sales_data = json.load(json_data)
        return sales_data


def write_basic_data(path_to_json):
    global basic_data

    basic_data_heading_map = {
        "gstin": "GSTIN",
        "fp": "Month",
        "filing_typ": "Filing Mode",
        "gt": "GT",
        "cur_gt": "Current GT",
        "fil_dt": "Filing Date",
    }
    basic_data_sheet = work_book["Sheet"]
    basic_data_sheet.title = "Basic Data"
    not_required_keys = ["b2b", "cdnr", "exp"]
    basic_data = get_json_sales_data(path_to_json)
    for key in not_required_keys:
        basic_data.pop(key)

    basic_data_sheet[f"{get_column_letter(4)}3"] = "Particulars"
    basic_data_sheet[f"{get_column_letter(4)}3"].font = Font(bold=True)
    basic_data_sheet[f"{get_column_letter(5)}3"] = "Value"
    basic_data_sheet[f"{get_column_letter(5)}3"].font = Font(bold=True)
    start_column = 4
    basic_data_column = 4
    basic_data_row = 4
    for (detail_heading, detail_value) in basic_data.items():
        for (basic_head, basic_value) in basic_data_heading_map.items():
            if basic_head == detail_heading:
                basic_data_sheet[
                    f"{get_column_letter(basic_data_column)}{basic_data_row}"
                ] = basic_value
                basic_data_sheet[
                    f"{get_column_letter(basic_data_column)}{basic_data_row}"
                ].font = Font(bold=True)
        basic_data_column += 1
        basic_data_sheet[
            f"{get_column_letter(basic_data_column)}{basic_data_row}"
        ] = detail_value
        basic_data_sheet[
            f"{get_column_letter(basic_data_column)}{basic_data_row}"
        ].font = Font(bold=True)
        basic_data_row += 1
        basic_data_column = start_column


def write_b2b_invoices(path_to_json):
    invoice_list = []
    b2b_headings_ref_map = {}
    b2b_heading_map = {
        "chksum": "Check Sum",
        "itms_0_itm_det_iamt": "IGST",
        "rchrg": "Reverse Charge",
        "itms_0_itm_det_csamt": "Cess",
        "idt": "Invoice Date",
        "ctin": "GSTIN",
        "inv_typ": "Invoice Type",
        "itms_0_itm_det_txval": "Taxable Value",
        "cflag": "C-Flag",
        "itms_0_itm_det_camt": "CGST",
        "itms_0_itm_det_rt": "Rate",
        "updby": "Updated by",
        "cfs": "CFS",
        "flag": "Flag",
        "inum": "Invoice No.",
        "itms_0_itm_det_samt": "SGST",
        "pos": "Place of Sale",
        "itms_0_num": "Rate Number",
        "val": "Invoice Value",
    }
    b2b_heading_list = [heading for heading in b2b_heading_map]

    sales_data = get_json_sales_data(path_to_json)
    if "b2b" in sales_data:
        b2b_sheet = work_book.create_sheet(title="B2B")
        for sales in sales_data["b2b"]:
            current_supplier = sales.copy()
            current_supplier.pop("inv")
            for invoice in sales["inv"]:
                # sample_test = {
                #     "no": invoice["inum"],
                #     "value": invoice["itms"][0]["itm_det"]["txval"],
                # }
                flattened_inv = flatten(invoice)
                invoice_list.append({**current_supplier, **flattened_inv})
        with open("b2b_sales.json", mode="w") as b2b_sales_data:
            json.dump(invoice_list, b2b_sales_data)

        heading_column = 1
        heading_row = 1
        for headings in set().union(*(d.keys() for d in invoice_list)):
            if headings in b2b_heading_list:
                for (formatted_keys, formatted_vals) in b2b_heading_map.items():
                    if formatted_keys == headings:
                        b2b_headings_ref_map.update(
                            {headings: f"{get_column_letter(heading_column)}"}
                        )
                        b2b_sheet[
                            f"{get_column_letter(heading_column)}{heading_row}"
                        ] = formatted_vals
                        b2b_sheet[
                            f"{get_column_letter(heading_column)}{heading_row}"
                        ].font = Font(bold=True)
            else:
                b2b_headings_ref_map.update(
                    {headings: f"{get_column_letter(heading_column)}"}
                )
                b2b_sheet[
                    f"{get_column_letter(heading_column)}{heading_row}"
                ] = headings
                b2b_sheet[
                    f"{get_column_letter(heading_column)}{heading_row}"
                ].font = Font(bold=True)
            heading_column += 1

        invoice_column = 1
        invoice_row = 2
        for invoice in invoice_list:
            for (item, value) in invoice.items():
                for (headings, excel_ref) in b2b_headings_ref_map.items():
                    if headings == item:
                        b2b_sheet[f"{excel_ref}{invoice_row}"] = value
                invoice_column += 1
            invoice_column = 1
            invoice_row += 1

    else:
        print("No B2B Invoices")


def write_b2b_credit_note_invoices(path_to_json):
    invoice_list = []
    b2b_credit_notes_headings_ref_map = {}
    b2b_credit_notes_headings_map = {
        "itms_0_itm_det_iamt": "IGST",
        "updby": "Updated by",
        "cfs": "CFS",
        "nt_num": "Invoice No",
        "itms_0_itm_det_samt": "SGST",
        "nt_dt": "Return Date",
        "idt": "Invoice Date",
        "itms_0_itm_det_rt": "Rate",
        "val": "Invoice Value",
        "flag": "Flag",
        "p_gst": "P GST",
        "itms_0_itm_det_camt": "CGST",
        "ntty": "Credit Type",
        "ctin": "GSTIN",
        "itms_0_num": "Rate Number",
        "cflag": "C Flag",
        "itms_0_itm_det_txval": "Taxable Value",
        "inum": "Invoice Number",
        "chksum": "Check Sum",
    }

    b2b_credit_notes_headings_list = [
        heading for heading in b2b_credit_notes_headings_map
    ]

    sales_data = get_json_sales_data(path_to_json)
    if "cdnr" in sales_data:
        b2b_credit_notes_sheet = work_book.create_sheet(title="CDNR")

        for sales_returns in sales_data["cdnr"]:
            current_supplier = sales_returns.copy()
            current_supplier.pop("nt")
            for invoice in sales_returns["nt"]:
                flattened_invoice = flatten(invoice)
                invoice_list.append({**current_supplier, **flattened_invoice})
        with open(file="b2b_sales_returns.json", mode="w") as b2b_sales_returns_data:
            json.dump(obj=invoice_list, fp=b2b_sales_returns_data)

        heading_column = 1
        heading_row = 1
        for headings in set().union(*(d.keys() for d in invoice_list)):
            if headings in b2b_credit_notes_headings_list:
                for (
                    formatted_keys,
                    formatted_vals,
                ) in b2b_credit_notes_headings_map.items():
                    if formatted_keys == headings:
                        b2b_credit_notes_headings_ref_map.update(
                            {headings: f"{get_column_letter(heading_column)}"}
                        )
                        b2b_credit_notes_sheet[
                            f"{get_column_letter(heading_column)}{heading_row}"
                        ] = formatted_vals
                        b2b_credit_notes_sheet[
                            f"{get_column_letter(heading_column)}{heading_row}"
                        ].font = Font(bold=True)
            else:
                b2b_credit_notes_headings_ref_map.update(
                    {headings: f"{get_column_letter(heading_column)}"}
                )
                b2b_credit_notes_sheet[
                    f"{get_column_letter(heading_column)}{heading_row}"
                ] = headings
                b2b_credit_notes_sheet[
                    f"{get_column_letter(heading_column)}{heading_row}"
                ].font = Font(bold=True)
            heading_column += 1

        invoice_column = 1
        invoice_row = 2
        for invoice in invoice_list:
            for (item, value) in invoice.items():
                for (headings, excel_ref) in b2b_credit_notes_headings_ref_map.items():
                    if headings == item:
                        b2b_credit_notes_sheet[f"{excel_ref}{invoice_row}"] = value
                invoice_column += 1
            invoice_column = 1
            invoice_row += 1
    else:
        print("No Credit Note Invoices")


path_to_json = get_user_json_directory()
write_b2b_invoices(path_to_json)
write_basic_data(path_to_json)
write_b2b_credit_note_invoices(path_to_json)
work_book.save(basic_data["gstin"] + "_" + basic_data["fp"] + ".xlsx")