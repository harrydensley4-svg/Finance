from savings_account import SavingsAccount, LessThanMinBalanceError
import pytest

class TestSavingsAccount:
    def test_savings_withdraw_fail(self, savings_account):
        assert savings_account.withdraw(-10) == False

    def test_successful_savings_withdrawal(self, savings_account):
        assert savings_account.withdraw(1) == 99

    def test_get_interest_rate_property(self, savings_account):
        assert savings_account.interest_rate == 5

    def test_less_than_min_balance(self, savings_account):
        assert savings_account.withdraw(120) == False

    def test_constructor_less_than_min_balance(self):
        with pytest.raises(LessThanMinBalanceError):
            SavingsAccount(1, 'Savings', -10, 5)

    def test_incorrect_withdraw_amount_type(self, savings_account):
        assert savings_account.withdraw('10 Dollars') == False