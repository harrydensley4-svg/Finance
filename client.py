# Client
# Attributes: client_ID, client_name, client_email, client_phone, client_adddres (?), is_active
# Methods: update_phone, update_email, update_address, cancel_account()

class Client:
    def __init__(self, client_ID, client_name, client_email, client_phone, client_address, contact_method = 'Phone', is_active=True):
        self.client_ID = client_ID
        self.client_name = client_name
        self.client_email = client_email
        self.client_phone = client_phone
        self.client_address = client_address
        self.is_active = is_active
        self.conact_method = contact_method

    def client_info(self):
        print(f'{self.client_ID}:{self.client_name}')
        print(f'Phone:{self.client_phone}')
        print(f'Email:{self.client_email}')
        print(f'Address:{self.client_address}')
        print(f'Active:{self.is_active}')

    def update_phone(self, client_phone):
        self.client_phone = client_phone
        print(f'New Phone: {self.client_phone}')

    def update_email(self, clientEmail):
        self.client_email = clientEmail
        print(f'New Email: {self.client_email}')

    def update_address(self, client_address):
        self.client_address = client_address
        print(f'New Address: {self.client_address}')

    def update_account_status(self):
        if self.is_active == True:
            self.is_active = False
            print('Not Active')
        else:
            self.is_active = True
            print('Active')

    def update_preferred_contact(self, contact_method):
        if self.conact_method.lower() == 'phone':
            self.conact_method = contact_method
            print('Preferred Contact Method: Phone')
        elif self.conact_method.lower() == 'email':
            self.conact_method = contact_method
            print('Preferred Contact Method: Email')
        else:
            print("Not a Valid Contact Method")

    def __str__(self):
        return f'{self.client_name} has a phone number {self.client_phone} and has a preferred contact method of {self.conact_method}'

    def __repr__(self):
        return f'Client(Client ID = {self.client_ID}, Client Name = {self.client_name}, is_active = {self.is_active}, Client Email = {self.client_email}, Client Phone = {self.client_phone}, Client Address = {self.client_address}, Preferred Contact Method = {self.conact_method})'
