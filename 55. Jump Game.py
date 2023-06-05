class Solution:
    def canJump(self, nums: List[int]) -> bool:
      dp = [False for _ in range(len(nums) - 1)]
      dp += [True]

      for i in range(len(nums) - 2, -1, -1):
        for j in range(i, min(len(nums), i + nums[i] + 1)):
          if dp[j]:
            dp[i] = dp[j]
            break

      return dp[0]
