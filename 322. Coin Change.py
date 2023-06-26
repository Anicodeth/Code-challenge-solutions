class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recursiveCoinChange(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1

            if amount in memo:
                return memo[amount]

            minCoins = float('inf')
            for coin in coins:
                result = recursiveCoinChange(amount - coin)
                if result >= 0:
                    minCoins = min(minCoins, result + 1)

            memo[amount] = minCoins if minCoins != float('inf') else -1
            return memo[amount]

        return recursiveCoinChange(amount)

    

  
