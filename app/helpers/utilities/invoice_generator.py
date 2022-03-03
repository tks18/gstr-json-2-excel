import json
from flatten_json import flatten
from app.helpers.threader import threader


def gen_invoices_function(sales_data, sales_type, invoice_term, gen_json, file_name):
    invoice_list = []
    if not sales_type == "b2cs":
        for sales in sales_data[sales_type]:
            current_supplier = sales.copy()
            current_supplier.pop(invoice_term)
            for invoice in sales[invoice_term]:
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

        if gen_json:
            with open(file_name, mode="w") as b2b_sales_data:
                json.dump(invoice_list, b2b_sales_data)

    else:
        for invoice in sales_data[sales_type]:
            flattened_invoice = flatten(invoice)
            invoice_list.append(flattened_invoice)

    return invoice_list


def generate_invoices_list(sales_data, sales_type, invoice_term, gen_json, file_name):
    gen_invoices_thread = threader(
        function=gen_invoices_function,
        sales_data=sales_data,
        sales_type=sales_type,
        invoice_term=invoice_term,
        gen_json=gen_json,
        file_name=file_name,
    )
    gen_invoices_thread.start()
    invoice_list = gen_invoices_thread.join()
    if gen_invoices_thread.error is not None:
        raise gen_invoices_thread.error
    return invoice_list
