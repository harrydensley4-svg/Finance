from account import Account

class MaxWithdrawError(Exception):
    def __init__(self, message = 'Exceeds the maximum withdrawal amount'):
        super().__init__(message)

class NegativeWithdrawalError(Exception):
    def __init__(self, message = "Withdrawal amount can not be negative"):
        super().__init__(message)

class EverydayAccount(Account):
    """
    Represents the properties commonly associated with an everyday account.
    It inherits from the Account class.

    Attributes:
    -----------
    MAX_WITHDRAW (int): The fixed max withdrawal amount

    Methods:
    --------
    withdraw(withdraw_amount):
        Overrides the withdraw method inherited from Account. 
        Ensures that the withdrawal amount is less than MAX_WITHDRAW.
    
    """
    MAX_WITHDRAW = 1000
    def __init__(self, account_ID, account_type, balance, is_active=True):
        super().__init__(account_ID, account_type, balance, is_active)

    def withdraw(self, withdraw_amount):
        """
        If sufficient funds are available, it withdraws money from the account.
        The withdrawal amount must be less than MAX_WITHDRAW.

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

            if withdraw_amount > self.MAX_WITHDRAW:
                raise MaxWithdrawError()

            self._Account__balance -= withdraw_amount
            return self.balance

        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False
