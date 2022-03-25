class ItemDescription:

    def __init__(self, item_id: int,
                 description: str,
                 ecomm_description: str,
                 category: str,
                 item_type: int,
                 upc: int,
                 index=None):
        self.item_id = item_id
        self.description = description
        self.ecomm_description = ecomm_description
        self.category = category
        self.item_type = item_type
        self.upc = upc
        self.index = index
