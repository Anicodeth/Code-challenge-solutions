class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        @cache
        def dp(index):
            if index >= n:
                return 0

            return min(cost[index] + dp(index + 1), cost[index] + dp(index + 2))

        return min(dp(0), dp(1))

        
