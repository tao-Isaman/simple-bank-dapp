from brownie import accounts, Bank


def main():
    account = accounts[0]
    contract = Bank.deploy({"from": account})
    
    contract.createAccount("Acc 1")
    contract.createAccount("Acc 2")
    
    print(contract.countAccount().return_value)