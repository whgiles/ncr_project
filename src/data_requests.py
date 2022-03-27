import pandas as pd
import requests


def send_account(account_number_hash: str, number_of_transactions: int, index=None):
    requests.post("http://127.0.0.1:5000/add/account",
                  json=
                  {"account_number_hash": account_number_hash,
                   "number_of_transactions": number_of_transactions}
                  )


def send_transaction(global_transaction_id: int, account_number_hash: str, store_num: int, ticket_num: int, date: str,
                     transaction_start_time: str, transaction_end_time: str, num_items: int, ticket_total_value: float,
                     index=None):
    requests.post("http://127.0.0.1:5000/add/transaction",
                  json=
                  {"global_transaction_id": global_transaction_id,
                   "account_number_hash": account_number_hash,
                   "store_num": store_num,
                   "ticket_num": ticket_num,
                   "date": str(date),
                   "transaction_start_time": str(transaction_start_time),
                   "transaction_end_time": str(transaction_end_time),
                   "num_items": num_items,
                   "ticket_total_value": ticket_total_value
                   }
                  )


def send_item_transaction(global_transaction_id: int, item_id: int, dept_num: int, qty_sold: int, item_price: float,
                          qty_is_weight: int, ticket_num: int, date: str, time_scanned: str, index=None):
    requests.post("http://127.0.0.1:5000/add/item_transaction",
                  json=
                  {"global_transaction": global_transaction_id,
                   "item_id": item_id,
                   "dept_num": dept_num,
                   "qty_sold": qty_sold,
                   "item_price": item_price,
                   "qty_is_weight": qty_is_weight,
                   "ticket_num": ticket_num,
                   "date": str(date),
                   "time_scanned": str(time_scanned)
                   })


def send_item_description(item_id: int, description: str, ecomm_description: str, category: str, item_type: int,
                          upc: int, index=None):
    requests.post("http://127.0.0.1:5000/add/item_description",
                  json=
                  {"item_id": item_id,
                   "description": description,
                   "ecomm_description": ecomm_description,
                   "category": category,
                   "item_type": item_type,
                   "upc": upc
                   })


# item_desc = pd.read_csv("../data/MSA_Practicum_Data_v1.0/items_descriptions.csv")
# item_desc = item_desc.fillna('')
# print(len(item_desc))
# for idx, row in item_desc.iterrows():
#     print(row)
#     send_item_description(row.item_id, row.description, row.ecomm_description, row.category, row.item_type, row.upc)


acc = pd.read_csv("../data/MSA_Practicum_Data_v1.0/accounts.csv")
print(acc.columns)