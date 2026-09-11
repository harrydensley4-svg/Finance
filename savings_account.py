from account import Account

class SavingsAccount(Account):
    MIN_BALANCE = 0
    def __init__(self, account_ID, client_ID, account_type, balance, interest_rate, is_active=True):
        super().__init__(account_ID, client_ID, account_type, balance, is_active)
        self.__interest_rate = interest_rate

    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount >= self.MIN_BALANCE:
            return super().withdraw(withdraw_amount)
        return False

    def get_interest_rate(self):
        return self.__interest_rate

    interest_rate = property(get_interest_rate)