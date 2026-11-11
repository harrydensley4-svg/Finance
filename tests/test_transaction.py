import pytest
from transaction import Transaction

class TestTransaction:
    def test_transaction_amount_invalid_type(self):
        with pytest.raises(TypeError):
            Transaction('100 dollars', 1, 'Withdraw', 'description')

    def test_transaction_negative_amount(self):
        with pytest.raises(ValueError):
            Transaction(-10, 1, 'Withdraw', 'description')

    def test_transaction_invalid_ID_type(self):
        with pytest.raises(TypeError):
            Transaction(100, '1', 'Withdraw', 'description')

    def test_negative_transaction_ID(self):
        with pytest.raises(ValueError):
            Transaction(100, -1, 'Withdraw', 'description')

    def test_transaction_type_error(self):
        with pytest.raises(TypeError):
            Transaction(100, 1, True, 'description')

    def test_transaction_type_empty(self):
        with pytest.raises(ValueError):
            Transaction(100, 1, '', 'description')

    def test_invalid_description_type(self):
        with pytest.raises(TypeError):
            Transaction(100, 1, 'withdraw', None)

    def test_empty_transaction_description(self):
        with pytest.raises(ValueError):
            Transaction(100, 1, 'withdraw', '')

    def test_processing_deposit_transaction(self, transaction1, savings_account):
        assert transaction1.process_transaction(savings_account) == 'Processed'

    def test_processing_withdraw_transaction(self, everyday_account, transaction2):
        assert transaction2.process_transaction(everyday_account) == 'Processed'

    def test_repeat_processing_transaction(self, transaction1, savings_account):
        transaction1.process_transaction(savings_account)
        assert transaction1.process_transaction(savings_account) == False

    def test_canceling_transaction(self, transaction1):
        assert transaction1.cancel_transaction() == True
        assert transaction1.status == 'Cancelled'

    def test_cancelling_processed_transaction(self, transaction1, savings_account):
        transaction1.process_transaction(savings_account)
        assert transaction1.cancel_transaction() == False

    def test_processing_invalid_transaction_type(self, savings_account):
        invalid_transaction = Transaction(10, 1, 'Invalid', 'Invalid Transaction')
        assert invalid_transaction.process_transaction(savings_account) == False

    def test_description_property(self, transaction1):
        assert transaction1.description == 'Depositing Money'
        transaction1.description = 'New Description'
        assert transaction1.description == 'New Description'

    def test_invalid_description_change(self, transaction1):
        assert transaction1.set_description(True) == False

    def test_transaction_ID_property(self, transaction1):
        assert transaction1.transaction_ID == 1

    def test_transaction_type_property(self, transaction1):
        assert transaction1.transaction_type == 'Deposit'

    def test_transaction_amount_property(self, transaction1):
        assert transaction1.amount == 800

    def test_transaction_string(self, transaction1):
        assert str(transaction1) == 'Transaction 1 of $800 to be Deposit with description Depositing Money is Pending'

    def test_transaction_repr(self, transaction1):
        assert repr(transaction1) == 'Transaction(Amount = $800, Transaction ID = 1, Transaction Type = Deposit, Description = Depositing Money, Status = Pending)'
