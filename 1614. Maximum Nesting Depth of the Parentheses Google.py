class Solution:
    def maxDepth(self, s: str) -> int:
        nesting = 0
        maxi = 0

        for c in s:
            if c == '(':
                nesting += 1
            elif c == ')': 
                nesting -= 1
            maxi = max(maxi, nesting)

        return maxi

