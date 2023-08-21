class Solution:
    def maximumGap(self, nums: List[int]) -> int:

      nums.sort()
      n = len(nums)
      maxi = -inf
      for i in range( n - 1):
        local = nums[i + 1] - nums[i]
        if local > maxi:
          maxi = local

      return maxi  if maxi != -inf else 0
