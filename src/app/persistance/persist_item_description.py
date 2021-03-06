from sqlalchemy import Table, Column, INTEGER, NUMERIC, TEXT
from src.app import engine, meta
from src.app.entities import ItemDescription


class PersistItemDescription:
    item_description_table = Table('item_descriptions', meta,
                                   Column('index', INTEGER, primary_key=True),
                                   Column('item_id', NUMERIC),
                                   Column('description', TEXT),
                                   Column('ecomm_description', TEXT, nullable=True),
                                   Column('category', TEXT),
                                   Column('item_type', NUMERIC),
                                   Column('upc', NUMERIC)
                                   )

    def __init__(self, item_description: ItemDescription):
        self.item_description = item_description

    def insert(self):
        sql = self.item_description_table.insert().values(description=self.item_description.description,
                                                          item_id=self.item_description.item_id,
                                                          ecomm_description=self.item_description.ecomm_description,
                                                          category=self.item_description.category,
                                                          item_type=self.item_description.item_type,
                                                          upc=self.item_description.upc)
        print('--------------------------------------------------------------------------------------------------')
        print(sql)
        with engine.connect() as conn:
            conn.execute(sql)
