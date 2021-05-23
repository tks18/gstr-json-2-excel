import csv
from pathlib import Path


def get_paths():
    csv_write_path = Path(
        input("\nEnter the Dir to which the Format CSV Has to be Saved?  ").lower()
    )
    return csv_write_path


def generate_csv_template(write_path):
    with open(
        file=Path(f"{write_path}/ledger_data_format.csv"), mode="w", newline=""
    ) as csv_file:
        headers = [
            "Date",
            "Particulars",
            "Type",
            "GSTIN/UIN",
            "Taxability",
            "Invoice Value",
            "Taxable",
            "Integrated Tax",
            "Central Tax",
            "State Tax",
            "Total Tax",
            "Rate",
            "Month",
        ]
        writer = csv.DictWriter(csv_file, fieldnames=headers)

        writer.writeheader()
        writer.writerow(
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
            }
        )


paths = get_paths()
generate_csv_template(write_path=paths)