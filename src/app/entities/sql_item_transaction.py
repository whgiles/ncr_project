

class ItemTransaction:

    def __init__(self,
                 global_transaction_id: int,
                 item_id: int,
                 dept_num: int,
                 qty_sold: int,
                 item_price: float,
                 qty_is_weight: int,
                 ticket_num: int,
                 date: str,
                 time_scanned: str,
                 index=None):
        self.global_transaction_id = global_transaction_id
        self.item_id = item_id
        self.dept_num = dept_num
        self.qty_sold = qty_sold
        self.item_price = item_price
        self.qty_is_weight = qty_is_weight
        self.ticket_num = ticket_num
        self.date = date
        self.time_scanned = time_scanned
        self.index = index
