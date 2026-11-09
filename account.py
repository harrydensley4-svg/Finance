from transaction import Transaction
from abc import ABC, abstractmethod

class NegativeWithdrawalError(Exception):
    def __init__(self, message = "Withdrawal amount can not be negative"):
        super().__init__(message)

class WithdrawGreaterThanBalanceError(Exception):
    def __init__(self, message = "Can not withdraw more than account balance"):
        super().__init__(message)

class Account(ABC):
    """
    A class to represent a client's account by storing/providing account information, 
    managing the account balance through withdrawals and deposits, and managing account status.

    Attributes:
        account_ID: int
        client_ID: int
        account_type: str
        balance: int/float
        is_active: bool
    """

    def __init__(self, account_ID, client_ID, account_type, balance, is_active=True):
        if isinstance(account_ID, int) and not isinstance(account_ID, bool) and account_ID > 0:
            self.__account_ID = account_ID
        else:
            self.__account_ID = 0
        if isinstance(client_ID, int) and not isinstance(client_ID, bool) and client_ID > 0:
            self.__client_ID = client_ID
        else:
            self.__client_ID = 0
        if isinstance(account_type, str) and account_type != '':
            self.__account_type = account_type
        else:
            self.__account_type = 'Unknown'
        if isinstance(balance, int | float):
            self.__balance = balance
        else:
            self.__balance = 0
        if isinstance(is_active, bool):
            self.__is_active = is_active
        else:
            self.__is_active = True

        self.__transaction_collection = []

    def process_transaction(self, amount, transaction_ID, transaction_type, description):
        transaction = Transaction(amount, transaction_ID, transaction_type, description)
        transaction.process_transaction(self)
        self.__transaction_collection.append(transaction)
        return transaction

    def find_records(self, trans_ID):
        for transaction in self.__transaction_collection:
            if transaction.transaction_ID == trans_ID:
                return transaction
        return None

    def number_of_transactions(self):
        return len(self.__transaction_collection)

    def get_account_id(self):
        return self.__account_ID

    def set_account_id(self, account_ID):
        self.__account_ID = account_ID

    def get_balance(self):
    # Returns the account balance.
        return self.__balance

    def get_account_type(self):
    # Returns the account type
        return self.__account_type

    def get_transactions(self):
        return self.__transaction_collection

    def withdraw(self, withdraw_amount):
    # If sufficient funds are available, it withdraws money from the account.
    # Parameters: withdraw_amount (int/float)
        try:
            if not isinstance(withdraw_amount, (int, float)) or isinstance(withdraw_amount, bool):
                raise TypeError('Should Be a Float or an Integer')
            if 0 > withdraw_amount:
                raise NegativeWithdrawalError()
            if withdraw_amount >= self.__balance:
                raise WithdrawGreaterThanBalanceError()
            else:
                self.__balance -= withdraw_amount
                print(f'New Balance: ${self.__balance}')
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def deposit(self, deposit_amount):
    # Deposits money into the account if the ammount is greater than zero
    # Parameters: deposit_amount (int/float)
        if isinstance(deposit_amount, (int, float)) and not isinstance(deposit_amount, bool):
            if deposit_amount > 0:
                self.__balance += deposit_amount
                print(f'New Balance: ${self.__balance}')

    def set_account_status(self, is_active):
    # Sets the active status of the account
    # Parameters: is_active (bool)
        if isinstance(is_active, bool):
            self.__is_active = is_active

    def get_account_status(self):
        return self.__is_active

    account_id = property(get_account_id, set_account_id)
    account_type = property(get_account_type)
    account_status = property(get_account_status, set_account_status)
    balance = property(get_balance)
    transaction_collection = property(get_transactions)

    def __str__(self):
        return f'Account ID: {self.__account_ID}, is a {self.__account_type} account with a balance of ${self.__balance}'

    def __repr__(self):
        return f'Account(Account ID = {self.__account_ID}, Client ID = {self.__client_ID}, Account Type = {self.__account_type}, Balance = ${self.__balance}, Is Active = {self.__is_active})'
