from account import Account

class EverydayAccount(Account):
    MAX_WITHDRAW = 1000
    def __init__(self, account_ID, client_ID, account_type, balance, is_active=True):
        super().__init__(account_ID, client_ID, account_type, balance, is_active)

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.MAX_WITHDRAW:
            return super().withdraw(withdraw_amount)
        return False