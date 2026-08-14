class Transaction:
    def __init__(self, amount, transaction_ID, transaction_type, description, account, status="Pending"):
        self.amount = amount
        self.transaction_ID = transaction_ID
        self.transaction_type = transaction_type
        self.description = description
        self.status = status
        self.account = account

    def process_transaction(self):
        if self.status == "Pending":
            if self.transaction_type.lower() == 'withdraw':
                self.account.withdraw(self.amount)
                self.status = "Processed"
                print('Withdrawal Processed')
            elif self.transaction_type.lower() == 'deposit':
                self.account.deposit(self.amount)
                self.status = "Processed"
                print('Deposit Processed')
            else:
                print("Invalid Transaction Type")

    def cancel_transaction(self):
        if self.status == 'Pending':
            self.status = "Cancelled"
            print("Transaction has been Cancelled")
        else:
            print('Transaction has already been Processed')

    def update_description(self, description):
        self.description = description
        print(f'The description has been updated to: {self.description}')

    def __str__(self):
        return f'Transaction {self.transaction_ID} of ${self.amount} to be {self.transaction_type} with description {self.description} is {self.status}'

    def __repr__(self):
        return f'Transaction(Amount = ${self.amount}, Transaction ID = {self.transaction_ID}, Transaction Type = {self.transaction_type}, Description = {self.description}, Account = {self.account}, Status = {self.status})'
