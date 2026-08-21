from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

# DEMONSTRATION
client_1 = Client(1, 'John', 'john@gmail.com', '0403 550 670',
                  '123 Adelaide Uni', 'Phone', True)
client_2 = Client(2, 'Bill', 'bill@gmail.com',
                  '0403 450 776', '312 Adelaide Uni')
client_3 = Client(3, 'Harry', 'harry@gmail.com',
                  '0401 660 716', '8 North Terrace', 'Email')

account_1 = Account(1, 1, 'Savings', 3450, True)
account_2 = Account(2, 2, 'Business', 103450, True)
account_3 = Account(3, 3, 'Everyday', 682.14, True)

transaction_1 = Transaction(100, 1, 'Deposit', 'New deposit', account_1)
transaction_2 = Transaction(6780, 2, 'Deposit', 'New deposit', account_2)
transaction_3 = Transaction(48.78, 3, 'Withdraw', 'Withdrawal', account_3)

branch_1 = Branch(1, 'Adelaide Branch', 'Adelaide', '0403 505 670')
branch_2 = Branch(2, 'Melbourne Branch', 'Melbourne', '0401 000 123', True)
branch_3 = Branch(3, 'Sydney Branch', 'Sydney', '0401 456 891')

print(client_1)
client_1.set_phone('0401 550 610')
print(client_1)

print(repr(client_2))
client_2.set_address('Melbourne')
client_2.set_account_status()
print(repr(client_2))

print(repr(account_3))
account_3.set_account_status(False)
print(repr(account_3))

print(account_1)
account_1.deposit(600)
print(account_1)

print(transaction_2)
print(repr(transaction_3))
transaction_2.cancel_transaction()
transaction_3.process_transaction()
print(transaction_2)
print(repr(transaction_3))

print(branch_1)
branch_1.open_branch()
print(branch_1)
branch_1.open_branch()
print(branch_1)

print(repr(branch_2))
branch_2.close_branch()
branch_2.set_phone('0406 780 908')
print(repr(branch_2))

# Adding and Removing Accounts
client_1.add_account(account_1)
print(client_1.get_accounts())
client_1.add_account(account_2)
print(client_1.get_accounts())
client_1.add_account(account_2)
client_1.remove_account(account_2)
print(client_1.get_accounts())
client_1.remove_account(account_2)

# Setting Client's Preferred Branch
print(client_1.get_preferred_branch())
client_1.set_preferred_branch(branch_1)
print(client_1.get_preferred_branch())

client_4 = Client('ID', 6, 123, 'phone', 'address')
print(client_4)