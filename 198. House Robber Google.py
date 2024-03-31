class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dp(index):
            if index >= n:
                return 0

            return max(nums[index] + dp(index + 2), dp(index + 1))

        return dp(0)
