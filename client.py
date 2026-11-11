from account import Account
from branch import Branch


class AccountNotFoundError(Exception):
    def __init__(self, message="This account is not found"):
        super().__init__(message)


class AccountAlreadyExistsError(Exception):
    def __init__(self, message='This account already exists'):
        super().__init__(message)


class Client:
    """
    A class to represent a bank client by managing their personal information, 
    account relationships, contact preferences and account status.

    Attributes:
    -----------
    client_ID (int): Unique identifier for the client.
    client_name (str): The name of the client.
    client_email (str): The email of the client.
    client_phone (str): The phone number of the client.
    client_address (str): The address of the client.
    contact_method (str): The clients preferred contact method.
    is_active (bool): Whether the client is active or not.

    Methods:
    --------
    add_account(account: Account)
        Add an account to the client. This updates the accounts client id.
    remove_account(account_id)
        Removes the account from the client. 
    set_preferred_branch(branch: Branch)
        set the clients preferred branch.
    get_preferred_branch()
        Returns the clients preferred branch.
    get_all_accounts()
        Returns the clients list of accounts.
    get_phone()
        Returns the clients phone number.
    set_phone(phone: str)
        Sets the clients phone number.
    get_email()
        Returns the clients email.
    set_email(email: str)
        Sets the clienst email.
    get_address()
        Returns the clients address.
    set_address(address: str)
        Sets the clients address.
    get_account_status()
        Returns the clients account status.
    set_account_status()
        Sets the clients account status.
    find_account(account_id: int)
        Given some account_id, returns a specific account.
    set_preffered_contact(contact_method: str)
        Set the clients preferred contact method (email or phone).
    get_client_id()
        Returns the clients unique ID.
    get_client_name()
        Returns the clients name.
    """

    def __init__(self, client_ID, client_name, client_email, client_phone, client_address, contact_method='Phone', is_active=True):
        if not isinstance(client_ID, int) or isinstance(client_ID, bool):
            raise TypeError('Client ID should be an integer')
        if client_ID <= 0:
            raise ValueError('Client ID should be a positive integer')

        if not isinstance(client_name, str):
            raise TypeError('Client name should be a string')
        if client_name.strip() == '':
            raise ValueError('Client name should not be empty')

        if not isinstance(client_email, str):
            raise TypeError('Client email should be a string')
        if client_email.strip() == '':
            raise ValueError('Client email should not be empty')

        if not isinstance(client_phone, str):
            raise TypeError('Client phone should be a string')
        if client_phone.strip() == '':
            raise ValueError('Client phone should not be empty')

        if not isinstance(client_address, str):
            raise TypeError('Client address should be a string')
        if client_address.strip() == '':
            raise ValueError('Client address should not be empty')

        if not isinstance(contact_method, str):
            raise TypeError('Contact method should be a string')
        if contact_method.strip() == '':
            raise ValueError('Contact method should not be empty')

        if not isinstance(is_active, bool):
            raise TypeError('Is active should be a boolean')

        self.__client_ID = client_ID
        self.__client_name = client_name
        self.__client_email = client_email
        self.__client_phone = client_phone
        self.__client_address = client_address
        self.__contact_method = contact_method
        self.__is_active = is_active
        self.__accounts = {}
        self.__preferred_branch = None

    def add_account(self, account):
        """
        Adds an Account object to the clients list of accounts.

        Parameters: 
        -----------
        account (Account)
            The account to be added to the client

        Returns
        -------
        bool
            If the account can be appended to the list of clients accounts, it returns true.
            Otherwise it returns false.
        """
        try:
            if not isinstance(account, Account):
                raise TypeError('Should be an account Type')
            if account.account_id in self.__accounts:
                raise AccountAlreadyExistsError()
            self.__accounts[account.account_id] = account
            account.client_id = self.__client_ID
            return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def remove_account(self, account_id):
        """Given some account_id, remove the account from the clients list of accounts."""
        return self.__accounts.pop(account_id, None)

    def set_preferred_branch(self, preferred_branch):
        """
        Sets the clients preferred bank branch.

        Parameters: 
        -----------
        preferred_branch (Branch)
            The preferred branch for the client

        Returns
        -------
        bool
            If successfully completed, it return true.
            Otherwise it returns false.
        """
        try:
            if not isinstance(preferred_branch, Branch):
                raise TypeError('Should be of typr Branch')
            self.__preferred_branch = preferred_branch
            return True
        except TypeError as e:
            print(f'{e.__class__.__name__}:{e}')
            return False

    def get_preferred_branch(self):
        """ Returns the clients preferred bank branch."""
        return self.__preferred_branch

    def get_all_accounts(self):
        """ Returns the list of accounts associated with the client."""
        return self.__accounts

    def get_phone(self):
        """ Returns the clients phone number."""
        return self.__client_phone

    def set_phone(self, client_phone):
        """
        Updates the clients phone number.

        Parameters: 
        -----------
        client_phone (str)
            The updated clients phone number
        """
        if isinstance(client_phone, str):
            # Removes any spaces in the string.
            client_phone = client_phone.replace(" ", "")
            # Checks that what remains is a digit.
            if client_phone.isdigit():
                self.__client_phone = client_phone

    def get_email(self):
        """ Returns the clients email address."""
        return self.__client_email

    def set_email(self, client_email):
        """
        Updates the clients email address.

        Parameters: 
        -----------
        client_email (str)
            The updated client email.
        """
        if isinstance(client_email, str):
            self.__client_email = client_email

    def get_address(self):
        """ Returns the clients address."""
        return self.__client_address

    def set_address(self, client_address):
        """
        Updates the clients address.

        Parameters: 
        -----------
        client_address (str)
            The updated client address.
        """
        if isinstance(client_address, str):
            self.__client_address = client_address

    def get_account_status(self):
        """ Returns the clients account status."""
        return self.__is_active

    def set_account_status(self, is_active):
        """Sets the clients account status."""
        if isinstance(is_active, bool):
            self.__is_active = is_active

    def find_account(self, account_id):
        """
        Given some account_id, find the account within 
        the clients list of accounts.

        Parameters:
        -----------
        account_id : int
            The unique identifier of the account to be found

        Returns
        -------
        Account
            Returns the account object.
            Otherwise, returns false.
        """
        try:
            if account_id not in self.__accounts:
                raise AccountNotFoundError()
            else:
                return self.__accounts.get(account_id, None)
        except AccountNotFoundError as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def get_contact_method(self):
        """Returns the clients preferred contact method."""
        return self.__contact_method

    def set_preferred_contact(self, contact_method):
        """
        Updates the clients preferred contact method provided it is either 'phone' or 'email'.

        Paramaters: 
        -----------
        contact_method (str)
            The clients new preffered contact method.

        Returns
        -------
        If contact_method is either 'phone' or 'email', 
        the client preffered contact method is updated.
        Otherwise it defaults to 'Phone'
        """
        if isinstance(contact_method, str):
            if contact_method.lower() == 'phone':
                self.__contact_method = contact_method
            elif contact_method.lower() == 'email':
                self.__contact_method = contact_method
            else:
                self.__contact_method = 'Phone'
        else:
            self.__contact_method = 'Phone'

    def get_client_id(self):
        """Returns the clients identifier."""
        return self.__client_ID

    def get_client_name(self):
        """Returns the clients name."""
        return self.__client_name

    client_id = property(get_client_id)
    client_name = property(get_client_name)
    client_email = property(get_email, set_email)
    client_phone = property(get_phone, set_phone)
    client_address = property(get_address, set_address)
    contact_method = property(get_contact_method, set_preferred_contact)
    is_active = property(get_account_status, set_account_status)
    accounts = property(get_all_accounts)
    preferred_branch = property(get_preferred_branch, set_preferred_branch)

    def __str__(self):
        """Returns a readable string description."""
        account_list = ''
        for account in self.__accounts.values():
            account_list += '\n' + '- ' + str(account)
        if len(self.__accounts) == 0:
            return f'{self.__client_name} has a phone number {self.__client_phone} and has a preferred contact method of {self.__contact_method}. No current Accounts.'
        else:
            return f'{self.__client_name} has a phone number {self.__client_phone} and has a preferred contact method of {self.__contact_method}. Accounts: ' + account_list

    def __repr__(self):
        """Returns a developer friendly string representation of the client."""
        return f'Client(Client ID = {self.__client_ID}, Client Name = {self.__client_name}, is_active = {self.__is_active}, Client Email = {self.__client_email}, Client Phone = {self.__client_phone}, Client Address = {self.__client_address}, Preferred Contact Method = {self.__contact_method}, Accounts: {self.__accounts})'
