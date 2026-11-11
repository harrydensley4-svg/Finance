class TestEverydayAccount:
    def test_withdraw_exceeds_max_withdraw(self, everyday_account):
        assert everyday_account.withdraw(1100) == False

    def test_successful_everyday_withdrawal(self, everyday_account):
        assert everyday_account.withdraw(100) == 9900

    def test_withdraw_negative_amount(self, everyday_account):
        assert everyday_account.withdraw(-10) == False

    def test_incorrect_withdraw_amount_type(self, everyday_account):
        assert everyday_account.withdraw('10 Dollars') == False