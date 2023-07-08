class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
      n = len(nums)
      dpMax = n * [0]
      dpMin = n * [0]

      dpMax[0] = dpMin[0] = nums[0]

      total = sum(nums)

      for i in range(1,n):
        dpMax[i] = max(nums[i], nums[i] + dpMax[i-1])
        
      for i in range(1,n):
        dpMin[i] = min(nums[i], nums[i] + dpMin[i-1])

      mini = min(dpMin)
      maxi = max(dpMax)

      if total == mini:
        return maxi
      else:
        return max(maxi, total - mini)

      
