from sqlalchemy import Table, Column, INTEGER, NUMERIC, DATE, TIME
from src.app import engine, meta
from src.app.entities import ItemTransaction
import pandas as pd


class PersistItemTransaction:
    item_transaction_table = Table('item_transactions', meta,
                                   Column('index', INTEGER, primary_key=True),
                                   Column('global_transaction_id', NUMERIC),
                                   Column('item_id', NUMERIC, nullable=False),
                                   Column('dept_num', NUMERIC),
                                   Column('qty_sold', NUMERIC),
                                   Column('item_price', NUMERIC),
                                   Column('qty_is_weight', NUMERIC),
                                   Column('ticket_num', NUMERIC),
                                   Column('date', DATE),
                                   Column('time_scanned', TIME)
                                   )

    def __init__(self, item_transaction: ItemTransaction):
        self.item_transaction = item_transaction

    def insert(self):
        sql = self.item_transaction_table.insert().values(
            item_id=self.item_transaction.item_id,
            dept_num=self.item_transaction.dept_num,
            global_transaction_id=self.item_transaction.global_transaction_id,
            qty_sold=self.item_transaction.qty_sold,
            item_price=self.item_transaction.item_price,
            qty_is_weight=self.item_transaction.qty_is_weight,
            ticket_num=self.item_transaction.ticket_num,
            date=self.item_transaction.date,
            time_scanned=self.item_transaction.time_scanned
        )

        with engine.connect() as conn:
            conn.execute(sql)

    @staticmethod
    def select_all():
        # sql = f"SELECT * FROM {self.item_transaction_table}'"
        with engine.connect() as conn:
            df = pd.read_sql_table('item_transactions', conn)
        return df
