from account import Account

class MaxWithdrawError(Exception):
    def __init__(self, message = 'Exceeds the maximum withdrawal amount'):
        super().__init__(message)

class EverydayAccount(Account):
    MAX_WITHDRAW = 1000
    def __init__(self, account_ID, client_ID, account_type, balance, is_active=True):
        super().__init__(account_ID, client_ID, account_type, balance, is_active)

    def withdraw(self, withdraw_amount):
        try:
            if withdraw_amount >= self.MAX_WITHDRAW:
                raise MaxWithdrawError()
            else:
                return super().withdraw(withdraw_amount)
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')