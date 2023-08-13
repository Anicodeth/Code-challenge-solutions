
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        memo = {}

        def dp(index, op):
            if op == m:
                return 0
            if (index, op) in memo:
                return memo[(index, op)]

            left = multipliers[op] * nums[index] + dp(index + 1, op + 1)
            right = multipliers[op] * nums[len(nums) - (op - index) - 1] + dp(index, op + 1)

            memo[(index, op)] = max(left, right)
            return memo[(index, op)]

        return dp(0, 0)
