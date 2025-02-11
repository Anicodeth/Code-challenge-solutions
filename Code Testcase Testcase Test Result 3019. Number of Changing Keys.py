class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        n = len(s)

        for i in range(1, n):
            if abs(ord(s[i]) - ord(s[i-1])) not in {32, 0}:
                count += 1

        return count
