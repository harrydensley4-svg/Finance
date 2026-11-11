from transaction import Transaction
from abc import ABC, abstractmethod


class Account(ABC):
    """
    A class to represent a client's account by storing/providing account information, 
    managing the account balance through withdrawals and deposits, and managing account status.

    Attributes:
    ------------
    account_ID (int): The unique account identifier.
    client_ID (int): The unique client identifer.
    account_type (str): The account type (savings or everyday).
    balance (int/float): The account balance.
    is_active (bool): whether the account is active or not.

    Methods:
    ----------
    get_account_id()
        Returns the account identifier.
    get_balance()
        Returns the account balance.
    get_account_type()
        Returns the account type.
    get_transactions()
        Returns the list of transactions associated with the account.
    set_account_status()
        Sets the account status.
    get_account_status()
        Returns the account status.
    get_client_id()
        Returns the client identifier.
    process_transaction(amount, transaction_ID, transaction_type, description):
        Creates and processes a Transaction instance. This is then appended to the transaction collection
        returns the transaction
    find_records(trans_ID):
        Returns the specific transaction that corresponds to the transaction ID. Returns None if the
        transaction does not exist.
    number_of_transactions():
        Returns the length of the accounts transaction collection list.
    withdraw(withdraw_amount):
        An abstract method that defines withdrawing money from an account. Subclasses
        must provide their own implementation
    deposit(deposit_amount):
        After validating the deposit amount, the deposit amount is added to the accounts balance.

    """

    def __init__(self, account_ID, account_type, balance, is_active=True):
        if not isinstance(account_ID, int) or isinstance(account_ID, bool):
            raise TypeError('Account ID should be a positive integer')
        if account_ID < 0:
            raise ValueError('Account ID should be a positive integer')

        if not isinstance(account_type, str):
            raise TypeError('Account Type should be of type string')
        if account_type == '':
            raise ValueError('Account type should not be left empty')

        if not isinstance(balance, (int, float)) or isinstance(balance, bool):
            raise TypeError('Balance should be a integer or float')

        if not isinstance(is_active, bool):
            raise TypeError('Is active should be a boolean')

        self.__account_ID = account_ID
        self.__client_ID = None
        self.__account_type = account_type
        self.__balance = balance
        self.__is_active = is_active
        self.__transaction_collection = []

    def process_transaction(self, amount, transaction_ID, transaction_type, description):
        """
        Creates and processes a Transaction instance.
        This is then appended to the transaction collection.

        Parameters:
        -----------
        amount: int | float
            The transaction amount.
        transaction_ID : int
            The unique transaction identifier.
        transaction_type : str
            The type of transaction (deposit or withdrawal).
        description : str
            A brief description of the transaction.

        Returns
        -------
        Transaction
            Returns the transaction instance.
            This is also appened to the accounts list of transactions. 
        """
        if self.__is_active:
            transaction = Transaction(
                amount, transaction_ID, transaction_type, description)
            transaction.process_transaction(self)
            self.__transaction_collection.append(transaction)
            return transaction

    def find_records(self, trans_ID):
        """
        For a specific transaction identifier, find that transaction.

        Parameters:
        -----------
        trans_ID : int
            The unique transaction identifier.

        Returns
        -------
        Transaction
            If the transaction can be found within the accounts collection, 
            then the transaction instance is returned. 
            Otherwise it returns none.
        """
        for transaction in self.__transaction_collection:
            if transaction.transaction_ID == trans_ID:
                return transaction
        return None

    def number_of_transactions(self):
        """The length of the transaction collection list."""
        return len(self.__transaction_collection)

    def get_account_id(self):
        """Returns the account identifier."""
        return self.__account_ID

    def get_balance(self):
        """Returns the account balance."""
        return self.__balance

    def get_account_type(self):
        """Returns the account type"""
        return self.__account_type

    def get_transactions(self):
        """Returns the list of transactions."""
        return self.__transaction_collection

    @abstractmethod
    def withdraw(self, withdraw_amount):
        """An abstract method that defines withdrawing money."""
        pass

    def deposit(self, deposit_amount):
        """
        Deposits money into the account if the ammount is greater than zero.

        Parameters:
        ----------- 
        deposit_amount (int/float)
            The amount to be deposited.

        Returns
        --------
        bool
            If the deposit amount is a positive integer or float, 
            then the balance is increased by the deposit amount.
            This returns true. Otherwise, false is returned.
        """
        try:
            if not isinstance(deposit_amount, (int, float)) or isinstance(deposit_amount, bool):
                raise TypeError('Deposit amount should be an integer or float')
            if deposit_amount < 0:
                raise ValueError('Deposit amount must be positive')
            self.__balance += deposit_amount
            return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def set_account_status(self, is_active):
        """Sets the active status of the account."""
        try:
            if not isinstance(is_active, bool):
                raise TypeError('Account status should be a boolean')
            self.__is_active = is_active
        except TypeError as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def get_account_status(self):
        """Returns the account status."""
        return self.__is_active

    def get_client_id(self):
        """Returns the client identifier."""
        return self.__client_ID

    def set_client_id(self, client_id):
        """Sets the client identifier."""
        self.__client_ID = client_id

    account_id = property(get_account_id)
    client_id = property(get_client_id, set_client_id)
    account_type = property(get_account_type)
    account_status = property(get_account_status, set_account_status)
    balance = property(get_balance)
    transaction_collection = property(get_transactions)

    def __str__(self):
        """Returns a readable string description."""
        return f'Account ID: {self.__account_ID}, is a {self.__account_type} account with a balance of ${self.__balance}'

    def __repr__(self):
        return f'Account(Account ID = {self.__account_ID}, Client ID = {self.__client_ID}, Account Type = {self.__account_type}, Balance = ${self.__balance}, Is Active = {self.__is_active})'
