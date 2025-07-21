class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        flagged = set()

        for i in range(1, n - 1):
            if s[i - 1] == s[i] == s[i + 1]:
                flagged.add(i - 1)

        return "".join([ c for i, c in enumerate(s) if i not in flagged])
