import pytest
from account import Account
from savings_account import SavingsAccount

class TestAccount:
    def test_account_is_abstract(self):
        # An abstract class should not be able to be instantiated
        with pytest.raises(TypeError):
            Account(1, 'Savings', 100)

    # Test account functionalty was tested through inheritance with the savings_account instance being used.
    def test_account_ID_type(self):
        with pytest.raises(TypeError):
            SavingsAccount('1', 'Savings', 100, 5)

    def test_account_ID_positive(self):
        with pytest.raises(ValueError):
            SavingsAccount(-1 , 'Savings', 100, 5)

    def test_account_type(self):
        with pytest.raises(TypeError):
            SavingsAccount(1, True, 100, 5)

    def test_empty_account_type(self):
        with pytest.raises(ValueError):
            SavingsAccount(1 , '', 100, 5)

    def test_balance_type(self):
        with pytest.raises(TypeError):
            SavingsAccount(1, 'Savings', '$100', 5)

    def test_is_active_type(self):
        with pytest.raises(TypeError):
            SavingsAccount(1, 'Savings', 100, 5, 'Active')

    def test_account_deposit(self, savings_account):
        assert savings_account.deposit(100) == True
        assert savings_account.balance == 200

    def test_account_deposit_negative_amount(self, savings_account):
        assert savings_account.deposit(-10) == False
        assert savings_account.balance == 100

    def test_account_deposit_invalid_type(self, savings_account):
        assert savings_account.deposit('$10') == False
        assert savings_account.balance == 100

    def test_process_transaction(self, savings_account):
        savings_account.process_transaction(100, 1, 'Deposit', 'description')
        assert savings_account.balance == 200
        assert savings_account.number_of_transactions() == 1

    def test_find_records(self, savings_account):
        savings_account.process_transaction(100, 1, 'Deposit', 'description')
        assert str(savings_account.find_records(1)) == 'Transaction 1 of $100 to be Deposit with description description is Processed'

    def test_find_nonexistent_records(self, savings_account):
        assert savings_account.find_records(1) == None

    def test_account_id_property(self, savings_account):
        assert savings_account.account_id == 1

    def test_transaction_collection_property(self, savings_account):
        assert savings_account.transaction_collection == []

    def test_set_account_status_invalid_type(self, savings_account):
        assert savings_account.set_account_status('Active') == False

    def test_set_account_status(self, savings_account):
        savings_account.set_account_status(False)
        assert savings_account.account_status == False

    def test_account_repr(self, savings_account):
        assert repr(savings_account) == f'Account(Account ID = {savings_account.account_id}, Client ID = {savings_account.client_id}, Account Type = {savings_account.account_type}, Balance = ${savings_account.balance}, Is Active = {savings_account.account_status})'
