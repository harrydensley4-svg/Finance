from client import Client
from account import Account
from transaction import Transaction
from branch import Branch

# DEMONSTRATION
client_1 = Client(1, 'John', 'john@gmail.com', '0403 550 670', '123 Adelaide Uni', True)
client_2 = Client(2, 'Bill', 'bill@gmail.com', '0403 450 776', '312 Adelaide Uni', False)
client_3 = Client(3, 'Harry', 'harry@gmail.com', '0401 660 716', '8 North Terrace', True)

account_1 = Account(1, 1, 'Savings', 3450, True)
account_2 = Account(2, 2, 'Business', 103450, True)
account_3 = Account(3, 3, 'Everyday', 682.14, True)

transaction_1 = Transaction(100, 1, 'Deposit', 'New deposit', account_1)
transaction_2 = Transaction(6780, 2, 'Deposit', 'New deposit', account_2)
transaction_3 = Transaction(48.78, 3, 'Withdraw', 'Withdrawal', account_3)

branch_1 = Branch(1, 'Adelaide Branch', 'Adelaide', '0403 505 670')
branch_2 = Branch(1, 'Melbourne Branch', 'Melbourne', '0401 000 123', True)
branch_3 = Branch(1, 'Sydney Branch', 'Sydney', '0401 456 891')

print(client_1.clientPhone)
client_1.update_phone('0401 550 610')
client_2.update_address('Melbourne')
client_3.update_account_status()

transaction_2.cancel_transaction()
transaction_3.process_transaction()

branch_1.open_branch()
branch_1.open_branch()