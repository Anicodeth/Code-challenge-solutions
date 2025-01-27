class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sumi = 0
        temp = x
        while x:
            rem = x % 10
            x //= 10
            sumi += rem

        if temp % sumi == 0:
            return sumi
        else: return -1
        
