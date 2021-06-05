from app.common.utilities.path_helpers import get_json_sales_data


from app.common.utilities.invoice_generator import generate_invoices_list
from app.common.utilities.invoice_writer_helper import write_invoices_to_excel


def invoices_writer(
    work_book,
    sheet_name,
    file_name,
    sales_data_list_name,
    invoice_item_name,
    gen_json,
    gen_excel,
    heading_map,
    path_to_json,
):

    invoice_list = []
    heading_list = [heading for heading in heading_map]

    sales_data = get_json_sales_data(path_to_json)
    if sales_data_list_name in sales_data:

        invoice_list = generate_invoices_list(
            sales_data=sales_data,
            sales_type=sales_data_list_name,
            invoice_term=invoice_item_name,
            gen_json=gen_json,
            file_name=file_name,
        )

        if gen_excel:
            b2b_sheet = work_book.create_sheet(sheet_name)
            write_invoices_to_excel(
                work_sheet=b2b_sheet,
                invoice_list=invoice_list,
                heading_map=heading_map,
                heading_list=heading_list,
            )