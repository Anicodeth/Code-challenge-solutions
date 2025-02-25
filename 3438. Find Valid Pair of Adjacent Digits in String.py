class Solution:
    def findValidPair(self, s: str) -> str:
        count = Counter(s)
        n = len(s)

        for i in range(n - 1):
            if s[i] != s[i + 1] and (int(s[i]) == count[s[i]]) and (int(s[i + 1]) == count[s[i + 1]]):
                return s[i] + s[i + 1]

        return ""
