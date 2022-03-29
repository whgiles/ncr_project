import json


class Account:

    def __init__(self, account_number_hash: str, number_of_transactions: int, index=None):
        self.index = index
        self.account_number_hash = account_number_hash
        self.number_of_transactions = number_of_transactions
