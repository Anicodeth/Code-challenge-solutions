class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        countSet = 0
        width = 0
        for i in range(32):
            temp = num2 & (1 << i)
            if temp: 
                countSet += 1
                width = i + 1

        res = 0
        for i in range(31, -1, -1):
            if not countSet: break
            temp = num1 & (1 << i)
            if temp: 
                res |= (1 << i)
                countSet -= 1
        
        i = 0
        while countSet:
            temp = res & (1 << i)
            if not temp: 
                res |= (1 << i)
                countSet -= 1
            i += 1

        return res



        
