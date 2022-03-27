from src.app.entities import *
import requests

requests.post("http://127.0.0.1:5000/add/account",
              json=
              {"account_number_hash": "111111111111",
               "number_of_transactions": None}
              )

requests.post("http://127.0.0.1:5000/add/transaction",
              json=
              {"global_transaction_id": 1,
               "account_number_hash": "123456hgg",
               "store_num": 1,
               "ticket_num": 1,
               "date": "1998-07-15",
               "transaction_start_time": None,
               "transaction_end_time": "12:57:57",
               "num_items": 2,
               "ticket_total_value": 4.50
               }
              )

requests.post("http://127.0.0.1:5000/add/item_transaction",
              json=
              {"global_transaction": 1,
               "item_id": 1,
               "dept_num": 2,
               "qty_sold": 2,
               "item_price": 4.50,
               "qty_is_weight": 0,
               "ticket_num": 234,
               "date": "1998-07-15",
               "time_scanned": "12:57:57"
               })

requests.post("http://127.0.0.1:5000/add/item_description",
              json=
              {"item_id": 1,
               "description": "this is a description",
               "ecomm_description": None,
               "category": "category",
               "item_type": 5,
               "upc": 4
               })
