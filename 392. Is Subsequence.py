class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        reach = len(s)
        for c in t:
            if p == reach:
                return True
            if c == s[p]:
                p += 1

        return p == reach
