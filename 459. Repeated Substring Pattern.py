class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        div = n // 2

        for i in range(1, div + 1):
            if n % i == 0:  
                mul = n // i
                if s[:i] * mul == s:
                    return True

        return False
