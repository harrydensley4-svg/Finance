class InvalidTransactionTypeError(Exception):
    def __init__(self, message="Not an excepted transaction type"):
        super().__init__(message)


class TransactionAlreadyProcessedError(Exception):
    def __init__(self, message='This transaction has already been processed'):
        super().__init__(message)


class Transaction:
    """
    A class to model transactions within an account by storing transaction information, 
    and processing/cancelling transactions

    Attributes:
    -----------
    amount (int/float): The amount of the transaction.
    transaction_ID (int): The unique ID of the transaction.
    transaction_type (str): The type of transaction (Deposit or Withdrawal).
    description (str): The transaction description.
    status (str): Current status of the transaction is initially set to "Pending".

    Methods:
    --------
    get_description()
        Returns the transaction description.
    get_status()
        Returns the transaction status.
    get_transaction_type()
        Returns the transaction type.
    get_transaction_ID()
        Returns the transaction identifier.
    get_amount()
        Returns the transaction amount.
    set_description()
        Sets the transaction description.
    process_transaction(account):
        If the transaction is pending, it can be processed depending on the transaction type 
        (Deposit or Withdraw)
    cancel_transaction():
        If the transaction has a Pending status, the transaction is cancelled.
        Otherwise, if the transaction has already been processed, the transaction can not be cancelled.
    """

    def __init__(self, amount, transaction_ID, transaction_type, description):
        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError('Amount must be an integer or float')
        if amount <= 0:
            raise ValueError('Amount must be greater than zero')

        if not isinstance(transaction_ID, int) or isinstance(transaction_ID, bool):
            raise TypeError('Transaction ID must be an integer')
        if transaction_ID <= 0:
            raise ValueError('Transaction ID must be greater than zero')

        if not isinstance(transaction_type, str):
            raise TypeError('Transaction type must be of type string')
        if transaction_type == '':
            raise ValueError('Transaction type can not be empty')

        if not isinstance(description, str):
            raise TypeError('Description must be of type string')
        if description == '':
            raise ValueError('Description must not be left blank')

        self.__amount = amount
        self.__transaction_ID = transaction_ID
        self.__transaction_type = transaction_type
        self.__description = description
        self.__status = 'Pending'

    def process_transaction(self, account):
        """
        Processes a pending transaction by either withdrawing or 
        depositing the specified amount into the associated account.
        Changes the status to processed if completed successfully.
        
        Parameters:
        -----------
        account : Account
            The account in which the transaction is associated to.

        Returns
        -------
        str
            Returns the updated transaction status.
            If the transaction is completed successfully, the
            status is updated to processed. 
            Otherwise, it returns false.

        """
        try:
            if self.__status != 'Pending':
                raise TransactionAlreadyProcessedError()
            if self.__transaction_type.lower() != 'withdraw' and self.__transaction_type.lower() != 'deposit':
                raise InvalidTransactionTypeError()
            else:
                if self.__transaction_type.lower() == 'withdraw':
                    account.withdraw(self.__amount)
                    self.__status = 'Processed'
                    return self.__status
                elif self.__transaction_type.lower() == 'deposit':
                    account.deposit(self.__amount)
                    self.__status = 'Processed'
                    return self.__status
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def cancel_transaction(self):
        """
        Provided the status is pending, it cancels a transaction.

        Returns
        -------
        bool
            If the transaction can be cancelled, then it returns true.
            Otherwise, it returns false. 
        """
        try:
            if self.__status != 'Pending':
                raise TransactionAlreadyProcessedError()
            else:
                self.__status = 'Cancelled'
                return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def get_description(self):
        """ Returns the description of the transaction."""
        return self.__description

    def get_status(self):
        """ Returns the status of the transaction."""
        return self.__status

    def get_transaction_type(self):
        """ Returns the transaction type."""
        return self.__transaction_type

    def get_transaction_ID(self):
        """ Returns the unique transaction ID."""
        return self.__transaction_ID

    def get_amount(self):
        """ Returns the transaction amount."""
        return self.__amount

    def set_description(self, description):
        """Sets the transaction description."""
        try:
            if not isinstance(description, str):
                raise TypeError('Description muts be of type string')
            else:
                self.__description = description
        except TypeError as e:
            print(f'{e.__class__.__name__}:{e}')
            return False

    description = property(get_description, set_description)
    status = property(get_status)
    transaction_type = property(get_transaction_type)
    transaction_ID = property(get_transaction_ID)
    amount = property(get_amount)

    def __str__(self):
        """Returns a readable string description."""
        return f'Transaction {self.__transaction_ID} of ${self.__amount} to be {self.__transaction_type} with description {self.__description} is {self.__status}'

    def __repr__(self):
        """Returns a developer friendly string representation of the transaction."""
        return f'Transaction(Amount = ${self.__amount}, Transaction ID = {self.__transaction_ID}, Transaction Type = {self.__transaction_type}, Description = {self.__description}, Status = {self.__status})'
