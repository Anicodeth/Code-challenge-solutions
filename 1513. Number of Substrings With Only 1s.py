class Solution:
    def numSub(self, s: str) -> int:

        count = 0
        current = 0

        for c in s:
            if c == '1':
                current += 1
            else:
                current = 0
            count += current

        return (count) % ((10**9) + 7)
