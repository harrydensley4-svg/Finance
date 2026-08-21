class Transaction:
    def __init__(self, amount, transaction_ID, transaction_type, description, account, status="Pending"):
        self.__amount = amount
        self.__transaction_ID = transaction_ID
        self.__transaction_type = transaction_type
        self.__description = description
        self.__status = status
        self.__account = account

    def process_transaction(self):
        if self.__status == "Pending":
            if self.__transaction_type.lower() == 'withdraw':
                self.__account.withdraw(self.__amount)
                self.__status = "Processed"
                print('Withdrawal Processed')
            elif self.__transaction_type.lower() == 'deposit':
                self.__account.deposit(self.__amount)
                self.__status = "Processed"
                print('Deposit Processed')
            else:
                print("Invalid Transaction Type")

    def cancel_transaction(self):
        if self.__status == 'Pending':
            self.__status = "Cancelled"
            print("Transaction has been Cancelled")
        else:
            print('Transaction has already been Processed')

    def get_description(self):
        return self.__description

    def get_status(self):
        return self.__status

    def get_transaction_type(self):
        return self.__transaction_type

    def get_transaction_ID(self):
        return self.__transaction_ID

    def get_amount(self):
        return self.__amount

    def set_description(self, description):
        if isinstance(description, str):    
            self.__description = description
            print(f'The description has been updated to: {self.__description}')

    def __str__(self):
        return f'Transaction {self.__transaction_ID} of ${self.__amount} to be {self.__transaction_type} with description {self.__description} is {self.__status}'

    def __repr__(self):
        return f'Transaction(Amount = ${self.__amount}, Transaction ID = {self.__transaction_ID}, Transaction Type = {self.__transaction_type}, Description = {self.__description}, Account = {self.__account}, Status = {self.__status})'
