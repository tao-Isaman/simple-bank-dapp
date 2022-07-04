import pytest

from brownie import accounts, Bank

@pytest.fixture
def token():
    account = accounts[0]
    contract = Bank.deploy({"from": account})
    return contract

def test_create_account_success(token):
    token.createAccount("Acc 1")
    token.createAccount("Acc 2")
    
    assert token.countAccount().return_value == 2
    
def test_deposit_success(token):
    token.createAccount("Acc 3")
    token.deposit("Acc 3", {
        'from': accounts[0],
        'value' : 10
        })
    
    assert token.balanceOf("Acc 3").return_value == 10