class TermsConditions():
    id = None
    term = ""
    is_active = True
    created_at = None
    updated_at = None
    user_id = None
    def __init__(self, id, term, is_active, created_at, updated_at, user_id):
        self.id = id
        self.term = term
        self.is_active = is_active
        self.created_at = created_at
        self.updated_at = updated_at
        self.user_id = user_id
        
    def create_term(self):
        pass
    def update_term(self):
        pass
    def delete_term(self):
        self.is_active = False
        pass
    def get_term(self):
        pass

