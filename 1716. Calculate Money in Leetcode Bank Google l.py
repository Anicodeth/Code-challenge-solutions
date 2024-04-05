class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday = 1

        while n > 0:

            for i in range(min(n, 7)):
                total += monday + i

            monday += 1
            n -= 7

        return total
        
