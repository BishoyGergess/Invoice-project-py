class User():
    id = None
    first_name = ""
    last_name = ""
    email = ""
    phone_number = ""
    is_active = False
    user_email_verified = False
    created_at = None
    updated_at = None

    
    def __init__(self, id, first_name, last_name, email, phone_number, is_active, user_email_verified, created_at, updated_at):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.is_active = is_active
        self.user_email_verified = user_email_verified
        self.created_at = created_at
        self.updated_at = updated_at

    def create_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        self.is_active = False
        pass
    def get_user(self):
        pass

    def activate_user(self):
        self.is_active = True
        pass

    def deactivate_user(self):
        self.is_active = False
        pass
    
    def user_email_verified(self):
        self.user_email_verified = True
        pass

new_user = User(1, "John", "Doe", "john.doe@example.com", "123-456-7890", True, "2023-01-01", "2023-01-01")