from brownie import accounts
from .test_base import contract

def test_multiple_tranfer_with_same_owner_success(contract):
    contract.createAccount("Acc 5")
    contract.createAccount("Acc 6", {
        'from': accounts[0],
    })
    contract.createAccount("Acc 7", {
        'from': accounts[0],
    })
    contract.deposit("Acc 5", {
        'from': accounts[0],
        'value' : 500
        })
    
    accountList = ['Acc 6', 'Acc 7']
    
    contract.multipleTranfer('Acc 5', accountList, 100)
    
    assert contract.balanceOf("Acc 5").return_value == 300
    assert contract.balanceOf("Acc 6").return_value == 100
    assert contract.balanceOf("Acc 7").return_value == 100
    

def test_multiple_tranfer_with_differents_owner_success(contract):
    contract.createAccount("Acc 5", {
        'from': accounts[0],
    })
    contract.createAccount("Acc 6", {
        'from': accounts[0],
    })
    contract.createAccount("Acc 7", {
        'from': accounts[1],
    })
    contract.deposit("Acc 5", {
        'from': accounts[0],
        'value' : 500
        })
    
    accountList = ['Acc 6', 'Acc 7']
    
    contract.multipleTranfer('Acc 5', accountList, 100)
    
    assert contract.balanceOf("Acc 5").return_value == 300
    assert contract.balanceOf("Acc 6").return_value == 100
    assert contract.balanceOf("Acc 7").return_value == 99