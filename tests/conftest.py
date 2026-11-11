from account import Account
from branch import Branch
from client import Client
from everyday_account import EverydayAccount
from savings_account import SavingsAccount
from transaction import Transaction
import pytest

@pytest.fixture
def branch():
    return Branch(1, 'Adelaide', 'Adelaide', '0401660716')

@pytest.fixture
def client():
    return Client(1, 'Harry', 'harry@gmail.com', '0401660716', 'address')

@pytest.fixture
def everyday_account():
    return EverydayAccount(2, 'Everyday', 10000)

@pytest.fixture
def savings_account():
    return SavingsAccount(1, 'Savings', 100, 5)

@pytest.fixture
def transaction1():
    return Transaction(800, 1, 'Deposit', 'Depositing Money')

@pytest.fixture
def transaction2():
    return Transaction(800, 2, 'Withdraw', 'Withdrawing Money')