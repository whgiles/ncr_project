from src.app.entities import Account, ItemDescription, Transaction, ItemTransaction
from src.app.persistance import PersistAccount, PersistTransaction, PersistItemTransaction, PersistItemDescription
from src.app import app, logger
from flask import request
from src.app.services import dic_to_item_transaction, dic_to_transaction, dic_to_item_description, dict_to_account, \
    BasedOnPastPurchases


@app.route('/', methods=['GET'])
def home():
    return "<p>Hi NCR!</p>"


@app.route('/add/account', methods=['POST'])
def add_account():
    data = request.get_json()
    acc = dict_to_account(data)
    PersistAccount(acc).insert()
    return "<p>Account Added</p>"


@app.route('/add/transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    tran = dic_to_transaction(data)
    PersistTransaction(tran).insert()
    return "<p>Transaction Added</p>"


@app.route('/add/item_description', methods=['POST'])
def add_item_description():
    data = request.get_json()
    item = dic_to_item_description(data)
    PersistItemDescription(item).insert()
    return "<p>ItemDescription Added</p>"


@app.route('/add/item_transaction', methods=['POST'])
def add_item_transaction():
    data = request.get_json()
    item = dic_to_item_transaction(data)
    PersistItemTransaction(item).insert()
    return "<p>ItemTransaction Added</p>"


@app.route('/<account_number_hash>/<curr_date>')
def get_suggestions(account_number_hash=None, curr_date=None):
    # suggestions = BasedOnPastPurchases('11259155490741164724', '2020-07-15').run()
    print(account_number_hash, curr_date, type(account_number_hash), type(curr_date))
    suggestions = BasedOnPastPurchases(account_number_hash, curr_date).run()
    return f'<p>{suggestions}</p>'
