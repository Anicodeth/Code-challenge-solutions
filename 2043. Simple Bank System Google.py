class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance
        self.n = len(balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if  account1 > self.n or account2 > self.n:
            return False

        balance = self.accounts[account1 - 1]

        if balance < money :
            return False
        else:
            self.accounts[account1 - 1] -= money
            self.accounts[account2 - 1] += money
            return True


    def deposit(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        else:
            self.accounts[account - 1] += money
            return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n:
            return False

        balance = self.accounts[account - 1]
        
        if balance < money:
            return False
        else:
            self.accounts[account - 1] -= money
            return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
