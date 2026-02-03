class Invoice():
    id = None
    invoice_number = None
    invoice_date = None
    invoice_due_date = None
    subtotal = None
    discount = None
    sales_tax = None
    total = None
    user_id = None
    contact_id = None
    
    def __init__(self, id, invoice_number, invoice_date, invoice_due_date,
                 subtotal, discount, sales_tax, total, user_id, contact_id):
        self.id = id
        self.invoice_number = invoice_number
        self.invoice_date = invoice_date
        self.invoice_due_date = invoice_due_date
        self.subtotal = subtotal
        self.discount = discount
        self.sales_tax = sales_tax
        self.total = total
        self.user_id = user_id
        self.contact_id = contact_id
        
    def create_invoice(self):
        pass
    
    def invoice_number_generator(self):
        if self.invoice_number is None or self.invoice_number == "":
            """import random
            self.invoice_number = random.randint(1000, 9999)"""
            pass
        else:
            return self.invoice_number
        
    def get_invoice(self):
        pass
    
    def update_invoice(self):
        pass
    
    def delete_invoice(self):
        pass
    
    def invoice_total(self):
        if self.discount != 0:
            return self.subtotal - self.discount + self.sales_tax
        else:
            return self.subtotal + self.sales_tax
