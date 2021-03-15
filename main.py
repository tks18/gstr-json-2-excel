import json
import json_flatten

from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = Workbook()
wb.active
ws = wb.create_sheet(title="headings")


new_array = []
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
            flattenedInv = json_flatten.flatten(invoice)
            new_array.append({**current_supplier, **flattenedInv})
    with open("sales_flatten.json", mode="w") as sampleData:
        json.dump(new_array, sampleData)

headings_map = {}

i = 1
j = 1
for headings in set().union(*(d.keys() for d in new_array)):
    headings_map.update({headings: f"{get_column_letter(i)}"})
    ws[f"{get_column_letter(i)}{j}"] = headings
    i += 1

i = 1
j = 2
for invoice in new_array:
    for (item, value) in invoice.items():
        for (head_map, head_value) in headings_map.items():
            if head_map == item:
                ws[f"{head_value}{j}"] = value
        i += 1
    i = 1
    j += 1

wb.save("sample.xlsx")