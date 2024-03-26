class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        @cache
        def dp(index, remain):
            if remain < 0:
                return 0
            elif remain == 0:
                return 1
            local = 0
            for i in range(index, n):
                local += dp(i, remain - coins[i])

            return local
        return dp(0, amount)


            
