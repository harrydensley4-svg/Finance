class Transaction:
    def __init__(self, amount, transactionID, transactionType, description, account, status="Pending"):
        self.amount = amount
        self.transactionID = transactionID
        self.transactionType = transactionType
        self.description = description
        self.status = status
        self.account = account

    def process_transaction(self):
        if self.status == "Pending":
            if self.transactionType.lower() == 'withdraw':
                self.account.withdraw(self.amount)
                self.status = "Processed"
                print('Withdrawal Processed')
            elif self.transactionType.lower() == 'deposit':
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

