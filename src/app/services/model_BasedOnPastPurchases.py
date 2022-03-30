from src.app.persistance import PersistAccount, PersistTransaction, PersistItemTransaction, PersistItemDescription
from src.app.entities import Transaction, ItemTransaction
import pandas as pd
import numpy as np
# from sklearn.linear_model import LinearRegression


class BasedOnPastPurchases:
    empty_transaction = Transaction(0, "0", 0, 0, "0", "0", "0", 0, 0)
    empty_item_transaction = ItemTransaction(0, 0, 0, 0, 0, 0, 0, "0", "0")

    def __init__(self, account_number_hash: str, todays_date: str):
        self.account_number_hash = account_number_hash
        self.todays_date = todays_date
        self.trans = self._get_transactions()
        self.item_trans = self._get_item_transactions()
        self.final_df = pd.DataFrame(
            columns=['last_date_of_purchase', 'average_cycle', 'num_of_transactions', 'item_id'])

    def _get_transactions(self):
        trans = PersistTransaction(self.empty_transaction).select_all()
        # print(trans.head())
        return trans

    def _get_item_transactions(self):
        item_trans = PersistItemTransaction(self.empty_item_transaction).select_all()
        # print(item_trans.head())
        return item_trans

    @staticmethod
    def _merge_data(item_trans: pd.DataFrame, trans: pd.DataFrame):
        trans = trans[['account_number_hash', 'global_transaction_id']]
        df = item_trans.merge(trans, on='global_transaction_id')
        print('merge data: 200 - -------------------------------------------')
        return df

    def _set_up(self):

        df = self._merge_data(self.item_trans, self.trans)

        df = df[df.account_number_hash == self.account_number_hash]

        for item in pd.unique(df.item_id):
            df1 = df[df.item_id == item]
            df2 = df1.groupby('global_transaction_id', as_index=False).sum()
            df1 = df1.drop_duplicates('global_transaction_id').drop(columns=['qty_sold'])
            df1 = df1.merge(df2[['global_transaction_id', 'qty_sold']], on='global_transaction_id')
            df1.item_id = df1.item_id.astype(np.int64).astype(str)

            df_length = len(df1)
            if 2 <= df_length < 20:
                df1 = df1.sort_values(by='date')
                df1['lag_date'] = df1['date'].shift(1)
                df1['diff_date'] = abs(df1['date'] - df1['lag_date']).dt.days

                if df_length > 20:
                    pass
                    # X = df1['qty_sold']
                    # y = df1['diff_date']
                    # reg = LinearRegression(X, y)

                else:

                    a = {'last_date_of_purchase': max(df1.date),
                         'average_cycle': df1.diff_date.mean(),
                         'num_of_transactions': df_length,
                         'item_id': df1.item_id.iloc[1]}
                    self.final_df = self.final_df.append(a, ignore_index=True)

    def run(self):
        self._set_up()
        self.final_df['today'] = pd.to_datetime(self.todays_date)
        print(self.final_df)

        self.final_df['diff_date'] = abs(self.final_df['last_date_of_purchase'] - self.final_df['today']).dt.days
        self.final_df = self.final_df[self.final_df.diff_date > self.final_df.average_cycle]

        return list(self.final_df.item_id)
