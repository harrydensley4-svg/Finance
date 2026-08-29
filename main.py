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

# TESTING CLIENT METHODS
print(client_1)
client_1.__client_phone = '0405 660 716' # Attempts to modify the private attribute directly, this does not work due to name mangling.
print(client_1.get_phone())
client_1.set_phone('0430 660 891') # Correctly update the clients number with the setter.
print(client_1.get_phone())
print(client_1.get_account_status())
client_1.set_email('newemail@gmail.com')
print(client_1.get_email())
print(client_1.get_accounts())
client_1.add_account(account_1)
client_1.add_account(account_2)
print(client_1.get_accounts())
print(client_1)
client_1.add_account(account_1)
client_1.remove_account(account_1)
client_1.client_info()
print(client_1)

print(repr(client_2))
client_2.remove_account(account_2)
client_2.set_preferred_branch(branch_2)
print(client_2.get_preferred_branch())
print(repr(client_2))
print(client_2.get_address())
client_2.set_address('New Address 123')
client_2.set_phone('Banana') # Despite being a string, this should be rejected as it is not a valid phone number.
client_2.set_account_status()
print(client_2.get_accounts())
print(repr(client_2))

print(client_3)
client_3.set_preferred_branch('Adelaide') # Passes "Adelaide" instead of a valid Branch type, thus it should be rejected.
print(client_3.get_preferred_branch())
print(client_3.get_address())
print(client_3.get_email())
print(client_3.get_contact_method())
client_3.set_preferred_contact('Carrier Pigeon') # This should be rejected as it is not one of the valid contact methods.
print(client_3.get_contact_method())
client_3.set_preferred_contact('Phone')
print(client_3.get_contact_method())
print(repr(client_3))

# Example of an object created with invalid constructor attributes.
client_4 = Client('Four', 'Bob', 'bob@gmail.com', 'Phone Number', 3, 'Message in a bottle')
print(repr(client_4))

# TESTING ACCOUNT METHODS
print(account_1)
print(account_1.get_balance())
account_1.deposit(-13) # Test validation by attempting to deposit a negative value which is rejected.
account_1.deposit(True) # Test validation by attempting to deposit a bool which is also rejected.
print(account_1.get_balance())
print(account_1.get_account_type())
account_1.set_account_status(False)
print(repr(account_1))

print(account_2.get_balance())
account_2.withdraw('One Hundred Dollars') # This will be rejected as it is not an int or a float.
print(account_2.get_account_type())
print(account_2.get_balance())
account_1.set_account_status(True)
print(repr(account_2))

print(account_3.get_account_type())
print(account_3.get_balance())
account_3.withdraw(13.4)
print(account_3.get_balance())
account_3.withdraw(-3)
print(account_3)

# Example of an object created with invalid constructor attributes.
account_4 = Account(False, True, 'Savings', 'Two hundred and fifty dollars')
print(repr(account_4))

# TESTING TRANSACTION METHODS.
print(transaction_1.get_description())
transaction_1.process_transaction()
print(transaction_1)
transaction_1.cancel_transaction()
print(transaction_1.get_transaction_ID())
print(transaction_1.get_transaction_type())
print(transaction_1.get_status())
print(repr(transaction_1))

print(repr(transaction_2))
transaction_2.cancel_transaction()
transaction_2.process_transaction()
transaction_2.set_description("I am depositing this money")
print(transaction_2.get_amount())
print(transaction_2.get_status())
print(repr(transaction_2))

print(transaction_3.get_description())
transaction_3.set_description('I am withdrawing this money')
print(transaction_3.get_amount())
print(transaction_3.get_transaction_ID())
print(transaction_3.get_transaction_type())
print(transaction_3)

# Example of an object created with invalid constructor attributes.
transaction_4 = Transaction(True, 'Ten', 'Withdraw', 'Incorrect Example', "Account 1")
print(repr(transaction_4))

# TESTING BRANCH METHODS.
print(branch_1.get_is_open())
branch_1.close_branch()
branch_1.open_branch()
print(branch_1.get_name())
print(branch_1.get_number())
print(repr(branch_1))

print(branch_2)
branch_2.open_branch()
print(branch_2.get_is_open())
print(branch_2.get_name())
print(branch_2.get_location())
branch_2.close_branch()
print(branch_2)

branch_3.set_phone("Phone Number") # Once again, this is not a valid phone number type, despite being a string.
print(branch_3.get_phone())
branch_3.set_phone("0403 123 456") # Setting a valid phone number. 
print(branch_3.get_phone())
print(branch_3.get_location())
print(repr(branch_3))

# Example of an object created with invalid constructor attributes.
branch_4 = Branch("One", "Perth Branch", 'Perth', 45067080, True)
print(branch_4)