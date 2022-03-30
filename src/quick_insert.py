import pandas as pd
from app import engine


def quick_item_desc():
    item_des = pd.read_csv('../data/MSA_Practicum_Data_v1.0/items_descriptions.csv')
    item_des.to_sql('item_descriptions', engine, if_exists='append')


def quick_acc():
    acc = pd.read_csv('../data/MSA_Practicum_Data_v1.0/accounts.csv', dtype=str)
    acc = acc.drop(columns=['global_transaction_id', 'ticket_num'])
    acc['number_of_transactions'] = 0
    acc = acc.rename({'account_num_hash': 'account_number_hash'}, axis='columns')
    acc = acc.drop_duplicates('account_number_hash', keep='first')

    acc.to_sql('accounts', engine, if_exists='append')


def quick_trans():
    acc = pd.read_csv('../data/MSA_Practicum_Data_v1.0/accounts.csv', dtype=str)
    acc = acc.rename({'account_num_hash': 'account_number_hash'}, axis='columns')
    acc = acc.drop(columns=['ticket_num'])
    acc = acc.drop_duplicates('global_transaction_id', keep='first')

    trans = pd.read_csv('../data/MSA_Practicum_Data_v1.0/transactions.csv', dtype=str)

    master = trans.merge(acc, on='global_transaction_id', how='left')
    master = master.fillna('')
    master = master[
        ['global_transaction_id', 'account_number_hash', 'store_num', 'ticket_num', 'date', 'transaction_start_time',
         'transaction_end_time', 'num_items', 'ticket_total_value']]

    master.to_sql('transactions', engine, if_exists='append')


def quick_item_trans():
    item_trans = pd.read_csv("../data/MSA_Practicum_Data_v1.0/items_transactions.csv", dtype=str)
    item_trans = item_trans[
        ['global_transaction_id', 'item_id', 'dept_num', 'qty_sold', 'item_price', 'qty_is_weight', 'ticket_num',
         'date', 'time_scanned']]
    item_trans.to_sql('item_transactions', engine, if_exists='append')


if __name__ == '__main__':
    quick_acc()
    print('accounts persisted')
    quick_item_desc()
    print('item descriptions persisted')
    quick_trans()
    print('transactions persisted')
    quick_item_trans()
    print('item transactions persisted')

    # the above mass import breaks the primary key, so I reset it below
    with engine.connect() as conn:
        conn.execute("SELECT setval(pg_get_serial_sequence('accounts', 'index'), (SELECT MAX(index) FROM accounts)+1);")
        conn.execute("SELECT setval(pg_get_serial_sequence('item_transactions', 'index'), (SELECT MAX(index) FROM item_transactions)+1);")
        conn.execute("SELECT setval(pg_get_serial_sequence('transactions', 'index'), (SELECT MAX(index) FROM transactions)+1);")
        conn.execute("SELECT setval(pg_get_serial_sequence('item_descriptions', 'index'), (SELECT MAX(index) FROM item_descriptions)+1);")
