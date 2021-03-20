import json
from flatten_json import flatten

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

work_book = Workbook()
work_book.active


def write_b2b_invoices():
    invoice_list = []
    with open("april 2018.json", mode="r") as json_data:
        data = json.load(json_data)
        if "b2b" in data:
            for sales in data["b2b"]:
                current_supplier = sales.copy()
                current_supplier.pop("inv")
                for invoice in sales["inv"]:
                    current_invoice = invoice.copy()
                    if len(invoice["itms"]) > 1:
                        current_invoice.pop("itms")
                        for current_inv_item in invoice["itms"]:
                            new_invoice = current_invoice.copy()
                            new_invoice["itms"] = [current_inv_item]
                            flattened_inv = flatten(new_invoice)
                            invoice_list.append({**current_supplier, **flattened_inv})
                    else:
                        flattened_inv = flatten(invoice)
                        invoice_list.append({**current_supplier, **flattened_inv})

    with open("sample.json", mode="w") as summa:
        json.dump(invoice_list, fp=summa)

    b2b_sheet = work_book.create_sheet("B2B")
    b2b_headings_ref_map = {}
    heading_column = 1
    heading_row = 1
    for headings in set().union(*(d.keys() for d in invoice_list)):
        b2b_headings_ref_map.update({headings: f"{get_column_letter(heading_column)}"})
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


work_book.save("Sample.xlsx")