class InvoiceRow():
    id = None
    item_name = ""
    quantity = 0
    unit_price = 0.0
    total_price = None
    invoice_id = None
    created_at = None
    updated_at = None
    deleted_at = None

    def __init__(self, id=None, item_name="", quantity=0, unit_price=0.0, total_price=0.0,
                 invoice_id=None, created_at=None, updated_at=None, deleted_at=None):
        self.id = id
        self.item_name = item_name
        self.quantity = quantity
        self.unit_price = unit_price
        self.total_price = self.amount()
        self.invoice_id = invoice_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
    def create_invoice_row(self):
        # Logic to create a new invoice row in the database
        pass
    def get_invoice_row(self, id):
        # Logic to retrieve an invoice row from the database by id
        pass
    def update_invoice_row(self):
        # Logic to update an existing invoice row in the database
        pass
    def delete_invoice_row(self, id):
        # Logic to delete an invoice row from the database by id
        pass
    def amount(self):
        return self.quantity * self.unit_price

