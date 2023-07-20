class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
      
      n = len(nums)

      dp = {}

      for right in range(n):
        for left in range(0, right):
          dp[(right, nums[right] - nums[left])] = dp.get(( left, nums[right] - nums[left]), 1) + 1
      return max(dp.values())
      
