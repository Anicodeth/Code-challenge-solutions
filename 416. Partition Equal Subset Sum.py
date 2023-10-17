class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False

        half_sum = total_sum // 2
        dp = [False] * (half_sum + 1)
        dp[0] = True

        for num in nums:
            for j in range(half_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[half_sum]
