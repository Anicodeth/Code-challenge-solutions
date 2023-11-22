class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        count = 0
        while num:
            val = num % 10

            if temp % val == 0:
                count += 1

            num //= 10

        return count
        
