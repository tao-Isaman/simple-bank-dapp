import pytest

from brownie import accounts, Bank

@pytest.fixture
def contract():
    account = accounts[0]
    contract = Bank.deploy({"from": account})
    return contract