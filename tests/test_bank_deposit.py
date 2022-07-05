from brownie import accounts
from .test_base import contract

def test_create_account_success(contract):
    contract.createAccount("Acc 1")
    contract.createAccount("Acc 2")
    
    assert contract.countAccount().return_value == 2
    
def test_deposit_success(contract):
    contract.createAccount("Acc 3")
    contract.deposit("Acc 3", {
        'from': accounts[0],
        'value' : 10
        })
    
    assert contract.balanceOf("Acc 3").return_value == 10

