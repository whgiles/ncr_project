from sqlalchemy import Table, Column, INTEGER, NUMERIC, TEXT
from src.app import engine, meta
from src.app.entities import Account


class PersistAccount:
    account_table = Table('accounts', meta,
                          Column('index', INTEGER, primary_key=True),
                          Column('account_number_hash', TEXT),
                          Column('number_of_transactions', NUMERIC)
                          )

    def __init__(self, account: Account):
        self.account = account
        with engine.connect() as conn:
            sql = self.account_table.insert().values(account_number_hash=self.account.account_number_hash,
                                                     number_of_transactions=self.account.number_of_transactions)
            conn.execute(sql)

    def insert(self):
        sql = self.account_table.insert().values(account_number_hash=self.account.account_number_hash,
                                                 number_of_transactions=self.account.number_of_transactions)
        with engine.connect() as conn:
            conn.execute(sql)
