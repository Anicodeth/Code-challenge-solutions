class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        memo = {}

        def dp(rem):
            if rem < 0:
                 return inf
            elif rem == 0:
                return 1
            elif rem in memo:
                return memo[rem]

            mini = inf

            for coin in coins:
                mini = min(mini, dp(rem - coin) + 1)
            memo[rem] = mini
            return mini

        res = inf

        for coin in coins:
            res = min(dp(amount - coin), res)

        return res if res != inf else -1

            



        
