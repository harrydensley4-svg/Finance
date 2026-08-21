# Account
# Attributes: account_ID, account_type, balance, status(?)
# Methods: deposit(), withdraw(), transfer(), close_account()

class Account:
    def __init__(self, account_ID, client_ID, account_type, balance, is_active=True):
        self.__account_ID = account_ID
        self.__client_ID = client_ID
        self.__account_type = account_type
        self.__balance = balance
        self.__is_active = is_active

    def get_balance(self):
        return self.__balance

    def get_account_type(self):
        return self.__account_type

    def withdraw(self, withdraw_amount):
        if 0 < withdraw_amount <= self.__balance:
            self.__balance -= withdraw_amount
            print(f'New Balance: ${self.__balance}')
        else:
            print('Insufficient Funds')

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance += deposit_amount
            print(f'New Balance: ${self.__balance}')

    def set_account_status(self, is_active):
        if isinstance(is_active, bool):
            self.__is_active = is_active

    def __str__(self):
        return f'The account {self.__account_ID} is a {self.__account_type} account with a balance of ${self.__balance}'

    def __repr__(self):
        return f'Account(Account ID = {self.__account_ID}, Client ID = {self.__client_ID}, Account Type = {self.__account_type}, Balance = ${self.__balance}, Is Active = {self.__is_active})'
