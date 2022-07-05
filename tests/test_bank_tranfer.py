from brownie import accounts
from .test_base import contract

def test_tranfer_with_same_owner_success(contract):
    contract.createAccount("Acc 5")
    contract.createAccount("Acc 6")
    contract.deposit("Acc 5", {
        'from': accounts[0],
        'value' : 500
        })
    
    contract.tranfer("Acc 5", "Acc 6", 400,{
        'from' : accounts[0],
    })
    
    assert contract.balanceOf("Acc 5").return_value == 100
    assert contract.balanceOf("Acc 6").return_value == 400

def test_tranfer_with_different_owner_success(contract):
    contract.createAccount("Acc 7", {
        'from' : accounts[0]
    })
    contract.createAccount("Acc 8", {
        'from' : accounts[1]
    })
    
    contract.deposit("Acc 7", {
        'from': accounts[0],
        'value' : 500
        })
    
    contract.tranfer("Acc 7", "Acc 8", 400,{
        'from' : accounts[0],
    })
    
    assert contract.balanceOf("Acc 7").return_value == 100
    assert contract.balanceOf("Acc 8").return_value == 396

