from sqlalchemy import Table, Column, INTEGER, TEXT, NUMERIC, DATE, TIME
from src.app import engine, meta
from src.app.entities import Transaction


class PersistTransaction:
    transaction_table = Table('transactions', meta,
                              Column('index', INTEGER, primary_key=True),
                              Column('global_transaction_id', NUMERIC),
                              Column('account_number_hash', TEXT),
                              Column('store_num', NUMERIC),
                              Column('ticket_num', NUMERIC),
                              Column('date', DATE),
                              Column('transaction_start_time', TIME),
                              Column('transaction_end_time', TIME),
                              Column('num_items', NUMERIC),
                              Column('ticket_total_value', NUMERIC)
                              )

    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    def insert(self):
        sql = self.transaction_table.insert().values(
            global_transaction_id=self.transaction.global_transaction_id,
            account_number_hash=self.transaction.account_number_hash,
            store_num=self.transaction.store_num,
            ticket_num=self.transaction.ticket_num,
            date=self.transaction.date,
            transaction_start_time=self.transaction.transaction_start_time,
            transaction_end_time=self.transaction.transaction_end_time,
            num_items=self.transaction.num_items,
            ticket_total_value=self.transaction.ticket_total_value
        )

        with engine.connect() as conn:
            conn.execute(sql)
