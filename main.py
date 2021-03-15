import json
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = Workbook()
wb.active
ws = wb.create_sheet(title="headings")

b2b = [
    "idt",
    "ctin",
    "inum",
    "val",
    "txvalue",
    "rt",
    "iamt",
    "camt",
    "samt",
    "csamt",
]

b2bFormmatedDate = [
    "Date",
    "GSTIN",
    "Invoice No.",
    "Invoice Value",
    "Taxable Value",
    "Rate",
    "IGST",
    "CGST",
    "SGST",
    "Cess",
]

# for heading in b2b:
#     for head in heading:
#         # print(head)
#         ref = f"{get_column_letter(i)}1"
#         ws[ref] = heading[head]
#         i += 1

with open("sales.json", mode="r") as salesData:
    jsonData = json.load(salesData)
    i = 1
    j = 2
    b2bSales = jsonData["b2b"]
    for sales in b2bSales:
        ref = f"{get_column_letter(i)}{j}"
        ws[ref] = sales
        i += 1
        j += 1

    wb.save(filename="sample.xlsx")