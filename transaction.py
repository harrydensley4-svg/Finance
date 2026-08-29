from account import Account

class Transaction:
    """
    A class to model transactions within an account by storing transaction information, 
    and processing/cancelling transactions

    Attributes:
        amount: int/float
        transaction_ID: int
        transaction_type: str
        description: str
        account: Account
        status: str
            Current status of the transaction is initially set to "Pending"
    """

    def __init__(self, amount, transaction_ID, transaction_type, description, account):
        if isinstance(amount, (int, float)) and not isinstance(amount, bool) and amount > 0:
            self.__amount = amount
        else:
            self.__amount = 0
        if isinstance(transaction_ID, int) and transaction_ID > 0:
            self.__transaction_ID = transaction_ID
        else:
            self.__transaction_ID = 0
        if isinstance(transaction_type, str) and transaction_type != '':
            self.__transaction_type = transaction_type
        else:
            self.__transaction_type = 'Unknown'
        if isinstance(description, str) and description != '':
            self.__description = description
        else:
            self.__description = 'No Description'
        if isinstance(account, Account):
            self.__account = account
        else:
            self.__account = 'Unknown'
        self.__status = 'Pending'

    def process_transaction(self):
    # Processes a pending transaction by either withdrawing or depositing the specified amount into the associated account.
    # Changes the status to processed if completed successfully.
        if self.__status == 'Pending':
            if self.__transaction_type.lower() == 'withdraw':
                self.__account.withdraw(self.__amount)
                self.__status = 'Processed'
                print('Withdrawal Processed')
            elif self.__transaction_type.lower() == 'deposit':
                self.__account.deposit(self.__amount)
                self.__status = 'Processed'
                print('Deposit Processed')
            else:
                print('Invalid Transaction Type')

    def cancel_transaction(self):
    # Provided the status is pending, it cancels a transaction.
        if self.__status == 'Pending':
            self.__status = 'Cancelled'
            print('Transaction has been Cancelled')
        else:
            print('Transaction has already been Processed')

    def get_description(self):
    # Returns the description of the transaction.
        return self.__description

    def get_status(self):
    # Returns the status of the transaction.
        return self.__status

    def get_transaction_type(self):
    # Returns the transaction type.
        return self.__transaction_type

    def get_transaction_ID(self):
    # Returns the unique transaction ID.
        return self.__transaction_ID

    def get_amount(self):
    # Returns the transaction amount.
        return f'${self.__amount}'

    def set_description(self, description):
        if isinstance(description, str):    
            self.__description = description
            print(f'The description has been updated to: {self.__description}')

    def __str__(self):
        return f'Transaction {self.__transaction_ID} of ${self.__amount} to be {self.__transaction_type} with description {self.__description} is {self.__status}'

    def __repr__(self):
        return f'Transaction(Amount = ${self.__amount}, Transaction ID = {self.__transaction_ID}, Transaction Type = {self.__transaction_type}, Description = {self.__description}, Account = {self.__account}, Status = {self.__status})'
