from account import Account


class LessThanMinBalanceError(Exception):
    def __init__(self, message="Less than minimum balance for a savings account"):
        super().__init__(message)


class NegativeWithdrawalError(Exception):
    def __init__(self, message="Withdrawal amount can not be negative"):
        super().__init__(message)


class SavingsAccount(Account):
    """
    Represents the properties commonly associated with a savings account such as an interest rate, 
    and a minimum balance. It inherits from the Account class. 

    Attributes:
    -----------
    MIN_BALANCE (int = 0): The fixed minimum balance required for the savings account.
    interest_rate (int): The interest rate acting on the account.

    Methods:
    --------
    withdraw(withdraw_amount):
        Overrides the abstract method from the Account class. 
        Implements a withdrawal functionality that ensures the balance never drops below the minimum balance. 
    get_interest_rate()
        Returns the interest rate.

    """
    MIN_BALANCE = 0

    def __init__(self, account_ID, account_type, balance, interest_rate, is_active=True):
        if balance < self.MIN_BALANCE:
            raise LessThanMinBalanceError()
        super().__init__(account_ID, account_type, balance, is_active)
        self.__interest_rate = interest_rate

    def withdraw(self, withdraw_amount):
        """
        If sufficient funds are available, it withdraws money from the account.

        Parameters: 
        -----------
        withdraw_amount : int | float
            The amount of money to be withdrawn from the account.

        Returns
        --------
        float
            If the money can be withdrawn it subtracts the withdrawal amount 
            from the balance and returns it as a float.
            Otherwise, it returns false.

        """
        try:
            if not isinstance(withdraw_amount, (int, float)) or isinstance(withdraw_amount, bool):
                raise TypeError('Should Be a Float or an Integer')

            if withdraw_amount < 0:
                raise NegativeWithdrawalError()

            if self.balance - withdraw_amount <= self.MIN_BALANCE:
                raise LessThanMinBalanceError()

            self._Account__balance -= withdraw_amount
            return self.balance

        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def get_interest_rate(self):
        """Returns the interest rate."""
        return self.__interest_rate

    interest_rate = property(get_interest_rate)
