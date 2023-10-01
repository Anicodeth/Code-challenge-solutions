class Solution:
    def countHomogenous(self, s: str) -> int:
        last = s[0]
        current = 0
        count = 0

        for c in s:
            if last == c:
                current += 1
            else:
                last = c
                current = 1
            count += current

        return  (count) % ((10**9) + 7)              
