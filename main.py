import json
from flatten_json import flatten

from pathlib import path

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

work_book = Workbook()
work_book.active


def get_user_json_directory():
    directory = input("Enter the Sales Json Directory").lower()
    correct_dir = path(directory)
    return correct_dir


def get_json_sales_data():
    with open("sales.json", mode="r") as json_data:
        sales_data = json.load(json_data)
        return sales_data


def write_basic_data():
    basic_data_sheet = work_book["Sheet"]
    basic_data_sheet.title = "Basic Data"
    not_required_keys = ["b2b", "cdnr", "exp"]
    basic_data = get_json_sales_data()
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
        basic_data_sheet[
            f"{get_column_letter(basic_data_column)}{basic_data_row}"
        ] = detail_heading
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


def write_b2b_invoices():
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

    b2b_sheet = work_book.create_sheet(title="B2B")

    sales_data = get_json_sales_data()
    for sales in sales_data["b2b"]:
        current_supplier = sales.copy()
        current_supplier.pop("inv")
        for invoice in sales["inv"]:
            # sample_test = {
            #     "no": invoice["inum"],
            #     "value": invoice["itms"][0]["itm_det"]["txval"],
            # }
            flattenedInv = flatten(invoice)
            invoice_list.append({**current_supplier, **flattenedInv})
    with open("b2b_sales.json", mode="w") as sampleData:
        json.dump(invoice_list, sampleData)

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
            b2b_sheet[f"{get_column_letter(heading_column)}{heading_row}"] = headings
            b2b_sheet[f"{get_column_letter(heading_column)}{heading_row}"].font = Font(
                bold=True
            )
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


write_b2b_invoices()
write_basic_data()
work_book.save("sample.xlsx")