class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      l = 0
      r = len(nums) - 1

      first = -1
      second = -1

      while l <= r:
        m = (l + r) // 2

        if nums[m] > target:
          r = m - 1
        elif nums[m] < target:
          l = m + 1
        else:
          first = m 
          r = m - 1
          
      l = 0
      r = len(nums) - 1

      while l <= r:
        m = (l + r) // 2

        if nums[m] > target:
          r = m - 1
        elif nums[m] < target:
          l = m + 1
        else:
          second = m 
          l = m + 1

      return [first, second]
        


      
