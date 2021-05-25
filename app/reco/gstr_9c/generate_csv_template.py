import csv
from pathlib import Path


def generate_csv_template(write_path):
    sample_data = [
        {
            "Date": "01-04-2018",
            "Particulars": "Supplier name",
            "Type": "Taxable",
            "GSTIN/UIN": "09BIOPA1154J1Z9",
            "Taxability": "TRUE",
            "Invoice Value": 79868.30,
            "Taxable": 67685.00,
            "Integrated Tax": 0,
            "Central Tax": 6091.65,
            "State Tax": 6091.65,
            "Total Tax": 12183.30,
            "Rate": 0.18,
            "Month": "Apr-18",
        },
        {
            "Date": "04-04-2018",
            "Particulars": "Supplier name",
            "Type": "Reversals",
            "GSTIN/UIN": "09BIOPA1154J1Z9",
            "Taxability": "TRUE",
            "Invoice Value": 79868.30,
            "Taxable": 67685.00,
            "Integrated Tax": 0,
            "Central Tax": 6091.65,
            "State Tax": 6091.65,
            "Total Tax": 12183.30,
            "Rate": 0.18,
            "Month": "Apr-18",
        },
        {
            "Date": "01-05-2018",
            "Particulars": "Supplier name",
            "Type": "Exempted",
            "GSTIN/UIN": "09BIOPA1154J1Z9",
            "Taxability": "FALSE",
            "Invoice Value": 67685.00,
            "Taxable": 67685.00,
            "Integrated Tax": 0,
            "Central Tax": 0,
            "State Tax": 0,
            "Total Tax": 0,
            "Rate": 0,
            "Month": "May-18",
        },
        {
            "Date": "01-05-2018",
            "Particulars": "Supplier name",
            "Type": "Reversals - Exempted",
            "GSTIN/UIN": "09BIOPA1154J1Z9",
            "Taxability": "FALSE",
            "Invoice Value": 67685.00,
            "Taxable": 67685.00,
            "Integrated Tax": 0,
            "Central Tax": 0,
            "State Tax": 0,
            "Total Tax": 0,
            "Rate": 0,
            "Month": "May-18",
        },
        {
            "Date": "04-04-2018",
            "Particulars": "Supplier name",
            "Type": "RCM - Inwards",
            "GSTIN/UIN": "09BIOPA1154J1Z9",
            "Taxability": "TRUE",
            "Invoice Value": 79868.30,
            "Taxable": 67685.00,
            "Integrated Tax": 0,
            "Central Tax": 6091.65,
            "State Tax": 6091.65,
            "Total Tax": 12183.30,
            "Rate": 0.05,
            "Month": "Apr-18",
        },
    ]
    with open(
        file=Path(f"{write_path}/ledger_data_format.csv"), mode="w", newline=""
    ) as csv_file:
        headers = sample_data[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=headers)

        writer.writeheader()
        for items in sample_data:
            writer.writerow(items)
