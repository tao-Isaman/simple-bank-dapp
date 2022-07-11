from brownie import accounts
from .test_base import contract


def test_get_list_account(contract):
    contract.createAccount("Acc 1")
    contract.createAccount("Acc 2")
    
    
    assert contract.getAccountList().return_value[0][1] == 'Acc 1'
    assert contract.getAccountList().return_value[1][1] == 'Acc 2'

