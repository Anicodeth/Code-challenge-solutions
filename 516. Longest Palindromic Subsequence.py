class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = {}
        def dp(l, r):
            if  r == l:
                return 1
            elif r < l:
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            if s[r] == s[l]:
                memo[(l, r)] = dp(l + 1, r - 1) + 2
            else:
                memo[(l, r)] = max(dp(l, r - 1), dp(l + 1, r))

            return memo[(l, r)]

        n = len(s)
        return dp(0, n - 1)


