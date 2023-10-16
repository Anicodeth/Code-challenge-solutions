class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        def power(x, y):
            result = 1
            while y > 0:
                if y % 2 == 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                y //= 2
            return result
        
        count = 1
        if n % 2 == 1:
            count = (power(5, n // 2 + 1) * power(4, n // 2)) % MOD
        else:
            count = (power(5, n // 2) * power(4, n // 2)) % MOD

        return count
