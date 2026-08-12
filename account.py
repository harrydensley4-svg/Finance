#Account
#Attributes: accountID, accountType, balance, status(?)
#Methods: deposit(), withdraw(), transfer(), close_account()

class Account:
    def __init__(self, accountID, clientID, accountType, balance, is_active=True):
        self.accountID = accountID
        self.clientID = clientID
        self.accountType = accountType
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