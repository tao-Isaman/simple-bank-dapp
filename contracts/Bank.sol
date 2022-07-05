pragma solidity >=0.6.0;


contract Bank {

    mapping (address => uint ) private _balances;

    struct bankAccount {
        address owner;
        string accountName;
        uint balances;
    }

    bankAccount[] public accountList;

    function createAccount(string calldata accountName) public {
        bool checkDup = isDupAccountName(accountName);
        require(!checkDup, "is Duplicatate account name");
        bankAccount memory newAccount = bankAccount(msg.sender,accountName,0);
        accountList.push(newAccount);
    }

    function countAccount() public returns(uint) {
      return accountList.length;
    }

    function isDupAccountName(string calldata accountName) public returns(bool) {
        for (uint256 i = 0 ; i < accountList.length ; i++){
            if(keccak256(abi.encode(accountName)) == keccak256(abi.encode(accountList[i].accountName))){
                return true ;
            }
        }
        return false;
    }

    function deposit(string calldata accountName) payable public {
        (bool found, uint index) = getIndexByAccountName(accountName);
        require(found, "no Account Found");
        
        _balances[msg.sender] += msg.value;
        accountList[index].balances += msg.value;
    }

    function balanceOf(string calldata accountName) public returns(uint) {
        (bool found, uint index) = getIndexByAccountName(accountName);
        require(found, "no Acc ount Found");
        return accountList[index].balances;
    }

    function getIndexByAccountName(string calldata accountName) public returns(bool,uint) {
        for (uint256 i = 0 ; i < accountList.length ; i++){
            if(keccak256(abi.encode(accountName)) == keccak256(abi.encode(accountList[i].accountName))){
                return (true, i);
            }
        }
        return (false, 0);
    }

    function withdraw(string calldata accountName, uint amount) public {
        (bool found, uint index) = getIndexByAccountName(accountName);
        require(found, "no Acc ount Found");
        require(accountList[index].balances >= amount);

        _balances[msg.sender] -= amount;
        accountList[index].balances -= amount;
    }

    // function deposit(){}

}