from brownie import accounts
from .test_base import contract


def test_get_owner(contract):
    assert contract.getOwner().return_value == accounts[0]

def test_change_owner(contract):
    contract.setOwner(accounts[1])
    assert contract.getOwner().return_value == accounts[1]