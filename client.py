from account import Account
from branch import Branch

class Client:
    """
    A class to represent a bank client by managing their personal information, 
    account relationships, contact preferences and account status.
    
    Attributes:
        client_ID: int
            Unique Identifier for the Client
        client_name: str
        client_email: str
        client_phone: str
        client_address: str
        contact_method: str
        is_active: bool
    """
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
        self.set_preferred_contact(contact_method)
        self.__accounts = []
        self.__preferred_branch = None

    def add_account(self, account):
    # Adds an Account object to the clients list of accounts.
    # Parameters: account (Account)
        if not isinstance(account, Account):
            print('This is not an account')
            return
        
        if account in self.__accounts:
            print('Account is already assigned to this client')
            return
        
        self.__accounts.append(account)

    def remove_account(self, account):
    # Removes an Account object from the clients list of accounts.
    # Parameters: account (Account)
        if isinstance(account, Account):
            if account not in self.__accounts:
                print('This account does not exist')
            else:
                self.__accounts.remove(account)

    def set_preferred_branch(self, preferred_branch):
    # Sets the clients preferred bank branch.
    # Parameters: preferred_branch (Branch)
        if not isinstance(preferred_branch, Branch):
            print('This is not a branch')
            return
        self.__preferred_branch = preferred_branch

    def get_preferred_branch(self):
    # Returns the clients preferred bank branch.
        return self.__preferred_branch
    
    def get_accounts(self):
    # Returns the list of accounts associated with the client. 
        return self.__accounts 

    def client_info(self):
        print(f'{self.__client_ID}: {self.__client_name}')
        print(f'Phone: {self.__client_phone}')
        print(f'Email: {self.__client_email}')
        print(f'Address: {self.__client_address}')
        print(f'Active: {self.__is_active}')

    def get_phone(self):
    # Returns the clients phone number.
        return self.__client_phone

    def set_phone(self, client_phone):
    # Updates the clients phone number.
    # Parameters: client_phone (str)
        if isinstance(client_phone, str):
            # Removes any spaces in the string.
            client_phone = client_phone.replace(" ", "")
            # Checks that what remains is a digit.
            if client_phone.isdigit():
                self.__client_phone = client_phone
            print(f'New Phone: {self.__client_phone}')

    def get_email(self):
    # Returns the clients email address.
        return self.__client_email

    def set_email(self, client_email):
    # Updates the clients email address.
    # Parameters: client_email (str)
        if isinstance(client_email, str):
            self.__client_email = client_email
            print(f'New Email: {self.__client_email}')

    def get_address(self):
    # Returns the clients address.
        return self.__client_address

    def set_address(self, client_address):
    # Updates the clients address.
    # Parameters: client_address (str)
        if isinstance(client_address, str):
            self.__client_address = client_address
            print(f'New Address: {self.__client_address}')

    def get_account_status(self):
    # Returns the clients account status.
        return self.__is_active

    def set_account_status(self):
    # Sets the clients account status between active and inactive.
        if self.__is_active == True:
            self.__is_active = False
            print('Not Active')
        else:
            self.__is_active = True
            print('Active')

    def get_contact_method(self):
    # Returns the clients preferred contact method.
        return self.__contact_method

    def set_preferred_contact(self, contact_method):
    # Updates the clients preferred contact method provided it is either 'phone' or 'email'. 
    # Paramaters: contact_method (str)
        if isinstance(contact_method, str):
            if contact_method.lower() == 'phone':
                self.__contact_method = contact_method
                print('Preferred Contact Method: Phone')
            elif contact_method.lower() == 'email':
                self.__contact_method = contact_method
                print('Preferred Contact Method: Email')
            else:
                self.__contact_method = 'Phone'
        else:
            self.__contact_method = 'Phone'

    def __str__(self):
        account_list = ''
        for account in self.__accounts:
            account_list += '- ' + str(account) + '\n'
        if len(self.__accounts) == 0:
            return f'{self.__client_name} has a phone number {self.__client_phone} and has a preferred contact method of {self.__contact_method}. No current Accounts.'
        else:
            return f'{self.__client_name} has a phone number {self.__client_phone} and has a preferred contact method of {self.__contact_method}. Accounts: ' + '\n' + account_list

    def __repr__(self):
        return f'Client(Client ID = {self.__client_ID}, Client Name = {self.__client_name}, is_active = {self.__is_active}, Client Email = {self.__client_email}, Client Phone = {self.__client_phone}, Client Address = {self.__client_address}, Preferred Contact Method = {self.__contact_method}, Accounts: {self.__accounts})'
