class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums) - 1
        memo = {}
        def dp(index):
            if index > n:
                return 0
            elif index == n:
                return nums[index]
            elif index in memo:
                return memo[index]

            memo[index] = max(nums[index] + dp(index + 2), dp(index + 1))
            return memo[index]

        return dp(0)
