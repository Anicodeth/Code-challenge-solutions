class Solution:
    def addDigits(self, num: int) -> int:
        num = str(num)
        while len(num) != 1:
            
            sumi = 0
            for c in num:
                sumi += int(c)

            num = str(sumi)

        return int(num)
        
