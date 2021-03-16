import json
from flatten_json import flatten

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

work_book = Workbook()
work_book.active


def write_b2b_invoices():
    invoice_list = []
    b2b_headings_ref_map = {}
    b2b_sheet = work_book.create_sheet(title="B2B")
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
    with open("sales.json", mode="r") as salesData:
        jsonData = json.load(salesData)
        for sales in jsonData["b2b"]:
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


work_book["Sheet"].title = "Basic Data"
write_b2b_invoices()
work_book.save("sample.xlsx")