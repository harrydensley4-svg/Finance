# Account
# Attributes: account_ID, account_type, balance, status(?)
# Methods: deposit(), withdraw(), transfer(), close_account()

class Account:
    def __init__(self, account_ID, client_ID, account_type, balance, is_active=True):
        self.account_ID = account_ID
        self.client_ID = client_ID
        self.account_type = account_type
        self.balance = balance
        self.is_active = is_active

    def withdraw(self, withdraw_amount):
        if 0 < withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print(f'New Balance: ${self.balance}')
        else:
            print('Insufficient Funds')

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f'New Balance: ${self.balance}')

    def update_account_status(self):
        if self.is_active == True:
            self.is_active = False
            print('Not Active')
        else:
            self.is_active = True
            print('Active')

    def __str__(self):
        return f'The account {self.account_ID} is a {self.account_type} account with a balance of ${self.balance}'

    def __repr__(self):
        return f'Account(Account ID = {self.account_ID}, Client ID = {self.client_ID}, Account Type = {self.account_type}, Balance = ${self.balance}, Is Active = {self.is_active})'
