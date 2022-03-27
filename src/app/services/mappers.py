from src.app.entities import *
from src.app import app


def dict_to_account(data: dict):
    acc = Account(
        data['account_number_hash'],
        data['number_of_transactions']
    )

    return acc


def dic_to_transaction(data: dict):
    tran = Transaction(
        data['global_transaction_id'],
        data['account_number_hash'],
        data['store_num'],
        data['ticket_num'],
        data['date'],
        data['transaction_start_time'],
        data['transaction_end_time'],
        data['num_items'],
        data['ticket_total_value']
    )
    return tran


def dic_to_item_transaction(data: dict):
    item = ItemTransaction(
        data['global_transaction_id'],
        data['item_id'],
        data['dept_num'],
        data['qty_sold'],
        data['item_price'],
        data['qty_is_weight'],
        data['ticket_num'],
        data['date'],
        data['time_scanned']
    )
    return item


def dic_to_item_description(data: dict):
    item = ItemDescription(
        data['item_id'],
        data['description'],
        data['ecomm_description'],
        data['category'],
        data['item_type'],
        data['upc']
    )
    return item
