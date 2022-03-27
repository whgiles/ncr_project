
class Transaction:

    def __init__(self,
                 global_transaction_id: int,
                 account_number_hash: str,
                 store_num: int,
                 ticket_num: int,
                 date: str,
                 transaction_start_time: str,
                 transaction_end_time: str,
                 num_items: int,
                 ticket_total_value: float,
                 index=None):
        self.global_transaction_id = global_transaction_id
        self.account_number_hash = account_number_hash
        self.store_num = store_num
        self.ticket_num = ticket_num
        self.date = date
        self.transaction_start_time = transaction_start_time
        self.transaction_end_time = transaction_end_time
        self.num_items = num_items
        self.ticket_total_value = ticket_total_value
        self.index = index
