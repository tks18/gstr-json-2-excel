import json
from flatten_json import flatten

from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font

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