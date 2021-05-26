import csv
from pathlib import Path
from app.reco.gstr_9c.constants.sample_invoices import SAMPLE_DATA


def generate_csv_template(write_path):
    for file in SAMPLE_DATA:
        with open(
            file=Path(f"{write_path}/{file['file_name']}"),
            mode="w",
            newline="",
        ) as csv_file:
            headers = file["invoices"][0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=headers)

            writer.writeheader()
            for items in file["invoices"]:
                writer.writerow(items)
