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

def test_withdraw_success(token):
    token.createAccount("Acc 4")
    token.deposit("Acc 4", {
        'from': accounts[0],
        'value' : 50
        })
    
    token.withdraw("Acc 4",40, {
        'from' : accounts[0],
    })
    
    assert token.balanceOf("Acc 4").return_value == 10
    
def test_tranfer_with_same_owner_success(token):
    token.createAccount("Acc 5")
    token.createAccount("Acc 6")
    token.deposit("Acc 5", {
        'from': accounts[0],
        'value' : 50
        })
    
    token.tranfer("Acc 5", "Acc 6", 40,{
        'from' : accounts[0],
    })
    
    assert token.balanceOf("Acc 5").return_value == 10
    assert token.balanceOf("Acc 6").return_value == 40

def test_tranfer_with_different_owner_success(token):
    token.createAccount("Acc 7", {
        'from' : accounts[0]
    })
    token.createAccount("Acc 8", {
        'from' : accounts[1]
    })
    
    token.deposit("Acc 7", {
        'from': accounts[0],
        'value' : 50
        })
    
    token.tranfer("Acc 7", "Acc 8", 40,{
        'from' : accounts[0],
    })
    
    assert token.balanceOf("Acc 7").return_value == 10
    assert token.balanceOf("Acc 8").return_value == 40

