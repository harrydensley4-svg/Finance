#client
#Attributes: clientID, clientName, clientEmail, clientPhone, clientAdddres (?), is_active
#Methods: update_phone, update_email, update_address, cancel_account()

class Client:
    def __init__(self, clientID, clientName, clientEmail, clientPhone, clientAddress, is_active):
        self.clientID = clientID
        self.clientName = clientName
        self.clientEmail = clientEmail
        self.clientPhone = clientPhone
        self.clientAddress = clientAddress
        self.is_active = is_active

    def client_info(self):
        print(f'{self.clientID}:{self.clientName}')
        print(f'Phone:{self.clientPhone}')
        print(f'Email:{self.clientEmail}')
        print(f'Address:{self.clientAddress}')
        print(f'Active:{self.is_active}')

    def update_phone(self, clientPhone):
        self.clientPhone = clientPhone

    def update_email(self, clientEmail):
        self.clientEmail = clientEmail

    def update_address(self, clientAddress):
        self.clientAddress = clientAddress

    def update_account_status(self, is_active):
        self.is_active = is_active

#Account
#Attributes: accountID, accountType, balance, status(?)
#Methods: deposit(), withdraw(), transfer(), close_account()

class Account:
    def __init__(self, accountID, clientID, accountType, balance, is_active):
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

    def transfer(self, transfer_accountID, transfer_amount):
        if transfer_amount <= self.balance:
            self.balance -= transfer_amount
            print(f'${transfer_amount} has been transferred to {transfer_accountID}')
        else:
            print('Insufficient Funds')

    def update_account_status(self, is_active):
        self.is_active = is_active

# DEMONSTRATION
client_1 = Client(1, 'John', 'john@gmail.com', '0403 550 670', '123 Adelaide Uni', True)
client_2 = Client(2, 'Bill', 'bill@gmail.com', '0403 450 776', '312 Adelaide Uni', True)
client_3 = Client(3, 'Harry', 'harry@gmail.com', '0401 660 716', '8 North Terrace', True)

print(client_1.clientName)
client_1.client_info()
client_3.client_info()

account_1 = Account(1, 1, 'Savings', 3450, True)
account_2 = Account(2, 2, 'Business', 103450, True)
account_3 = Account(3, 3, 'Everyday', 682.14, True)

print(account_1.accountType)
print(account_2.accountType)
print(account_3.accountID)
print(account_1.is_active)
account_1.deposit(340)
account_2.deposit(23000)
print(account_3.balance)
account_3.withdraw(700)
print(account_3.balance)

account_3.transfer(2, 300)