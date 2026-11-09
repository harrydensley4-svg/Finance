from account import Account, NegativeWithdrawalError, WithdrawGreaterThanBalanceError

class LessThanMinBalanceError(Exception):
    def __init__(self, message = "Less than minimum balance for a savings account"):
        super().__init__(message)

class SavingsAccount(Account):
    MIN_BALANCE = 0
    def __init__(self, account_ID, client_ID, account_type, balance, interest_rate, is_active=True):
        if balance <= self.MIN_BALANCE:
            raise LessThanMinBalanceError()
        super().__init__(account_ID, client_ID, account_type, balance, is_active)
        self.__interest_rate = interest_rate
    
    def withdraw(self, withdraw_amount):
    # If sufficient funds are available, it withdraws money from the account.
    # Parameters: withdraw_amount (int/float)
        try:
            if self.balance - withdraw_amount >= self.MIN_BALANCE:
                raise LessThanMinBalanceError()
            else:
                return super().withdraw(withdraw_amount)
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False


    def get_interest_rate(self):
        return self.__interest_rate

    interest_rate = property(get_interest_rate)