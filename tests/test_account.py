class TestAccount:
    def test_deposit_process_transaction(self, savings_account):
        savings_account.process_transaction(800, 1, 'Deposit', 'Deposit')
        assert savings_account.balance == 900

    def test_find_transactions(self, account):
        assert account.transaction_collection == None