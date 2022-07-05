from brownie import accounts
from .test_base import contract

def test_withdraw_success(contract):
    contract.createAccount("Acc 4")
    contract.deposit("Acc 4", {
        'from': accounts[0],
        'value' : 50
        })
    
    contract.withdraw("Acc 4",40, {
        'from' : accounts[0],
    })
    
    assert contract.balanceOf("Acc 4").return_value == 10
    
