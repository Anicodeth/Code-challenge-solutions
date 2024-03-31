class ATM:

    def __init__(self):
        self.storage = [[20, 0], [50, 0], [100, 0], [200, 0],[500, 0]]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, amount in enumerate(banknotesCount):
            self.storage[i][1] += amount

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        temp = [ [self.storage[i][0], self.storage[i][1]]  for i in range(5) ]
        for i in range(4, -1, -1):
            needed = amount // temp[i][0]
            amount -= min(needed, temp[i][1]) * temp[i][0] 
            capable = min(needed, temp[i][1]) 
            temp[i][1] -= capable
            res[i] = capable
            if amount == 0:
                self.storage = temp
                return res
        
        return [-1]

        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
