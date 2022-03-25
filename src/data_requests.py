from src.app.entities import *
import requests

# requests.post(" http://127.0.0.1:5000/add/account",
#               json=
#               {"account_number_hash": "123456hgg",
#                "number_of_transactions": None}
#               )

requests.post(" http://127.0.0.1:5000/add/transaction",
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
