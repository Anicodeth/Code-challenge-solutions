class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 2)
        dp[2] = 1
        dp[3] = 2
        
        for i in range(4, n + 1):
            for j in range(1, i // 2 + 1):
                dp[i] = max(dp[i], max(i - j, dp[i - j]) * j)
        
        return dp[n]
