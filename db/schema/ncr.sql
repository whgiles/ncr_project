CREATE TABLE accounts (
    index SERIAL PRIMARY KEY,
    account_number_hash varchar(100) UNIQUE NOT NULL,
    number_of_transactions NUMERIC
);
CREATE TABLE transactions (
    index SERIAL PRIMARY KEY,
    global_transaction_id NUMERIC UNIQUE NOT NULL,
    account_number_hash varchar(100) NULL,
    store_num NUMERIC,
    ticket_num NUMERIC,
    date DATE NOT NULL,
    transaction_start_time TIME,
    transaction_end_time TIME,
    num_items NUMERIC NOT NULL,
    ticket_total_value NUMERIC NOT NULL
);
CREATE TABLE item_descriptions (
    index SERIAL PRIMARY KEY,
    item_id NUMERIC UNIQUE NOT NULL,
    description TEXT,
    ecomm_description TEXT,
    category varchar(100),
    item_type NUMERIC,
    upc NUMERIC
);
CREATE TABLE item_transactions (
    index SERIAL PRIMARY KEY,
    global_transaction_id NUMERIC REFERENCES transactions (global_transaction_id),
    item_id NUMERIC REFERENCES item_descriptions (item_id),
    dept_num NUMERIC,
    qty_sold NUMERIC,
    item_price NUMERIC,
    qty_is_weight NUMERIC,
    ticket_num NUMERIC,
    date DATE,
    time_scanned TIME
);
