# Client
# Attributes: client_ID, client_name, client_email, client_phone, client_adddres (?), is_active
# Methods: update_phone, update_email, update_address, cancel_account()
from account import Account
from branch import Branch

class Client:
    def __init__(self, client_ID, client_name, client_email, client_phone, client_address, contact_method = 'Phone', is_active=True):
        if isinstance(client_ID, int) and client_ID > 0:
            self.__client_ID = client_ID
        else:
            self.__client_ID = 0
        if isinstance(client_name, str) and client_name.strip() != '':
            self.__client_name = client_name
        else:
            self.__client_name = 'Unknown'
        if isinstance(client_email, str) and client_email.strip() != '':
            self.__client_email = client_email
        else:
            self.__client_email = 'Unknown'
        if isinstance(client_phone, str) and client_phone.strip() != '':
            self.__client_phone = client_phone
        else:
            self.__client_phone = 'Unknown'
        if isinstance(client_address, str) and client_address.strip() != '':
            self.__client_address = client_address
        else:
            self.__client_address = 'Unknown'
        if isinstance(is_active, bool):
            self.__is_active = is_active
        else:
            self.__is_active = True
        if isinstance(contact_method, str) and contact_method.strip() != '':
            self.__conact_method = contact_method
        else:
            self.__conact_method = 'Phone'
        self.__accounts = []
        self.__preferred_branch = None

    def add_account(self, account):
        if isinstance(account, Account):
            if account in self.__accounts:
                print('Account is already assigned to this client')
            else:
                self.__accounts.append(account)

    def remove_account(self, account):
        if isinstance(account, Account):
            if account not in self.__accounts:
                print('This account does not exist')
            else:
                self.__accounts.remove(account)

    def set_preferred_branch(self, preferred_branch):
        if isinstance(preferred_branch, Branch):
            self.__preferred_branch = preferred_branch

    def get_preferred_branch(self):
        return self.__preferred_branch
    
    def get_accounts(self):
        return self.__accounts
            

    def client_info(self):
        print(f'{self.__client_ID}:{self.__client_name}')
        print(f'Phone:{self.__client_phone}')
        print(f'Email:{self.__client_email}')
        print(f'Address:{self.__client_address}')
        print(f'Active:{self.__is_active}')

    def get_phone(self):
        return self.__client_phone

    def set_phone(self, client_phone):
        if isinstance(client_phone, str):
            self.__client_phone = client_phone
            print(f'New Phone: {self.__client_phone}')

    def get_email(self):
        return self.__client_email

    def set_email(self, client_email):
        if isinstance(client_email, str):
            self.__client_email = client_email
            print(f'New Email: {self.__client_email}')

    def get_address(self):
        return self.__client_address

    def set_address(self, client_address):
        if isinstance(client_address, str):
            self.__client_address = client_address
            print(f'New Address: {self.__client_address}')

    def get_account_status(self):
        return self.__is_active

    def set_account_status(self):
        if self.__is_active == True:
            self.__is_active = False
            print('Not Active')
        else:
            self.__is_active = True
            print('Active')

    def get_contact_method(self):
        return self.__conact_method

    def set_preferred_contact(self, contact_method):
        if isinstance(contact_method, str):
            if self.__conact_method.lower() == 'phone':
                self.__conact_method = contact_method
                print('Preferred Contact Method: Phone')
            elif self.__conact_method.lower() == 'email':
                self.__conact_method = contact_method
                print('Preferred Contact Method: Email')
        else:
            print("Not a Valid Contact Method")

    def __str__(self):
        return f'{self.__client_name} has a phone number {self.__client_phone} and has a preferred contact method of {self.__conact_method}'

    def __repr__(self):
        return f'Client(Client ID = {self.__client_ID}, Client Name = {self.__client_name}, is_active = {self.__is_active}, Client Email = {self.__client_email}, Client Phone = {self.__client_phone}, Client Address = {self.__client_address}, Preferred Contact Method = {self.__conact_method})'
