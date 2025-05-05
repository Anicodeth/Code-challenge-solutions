class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        f1, f2, f3 = 1, 1, 2  # dp[0], dp[1], dp[2]

        if n == 1:
            return 1
        elif n == 2:
            return 2

        for _ in range(n - 2):
            front = (2 * f3 + f1) % MOD
            f1, f2, f3 = f2, f3, front

        return f3
