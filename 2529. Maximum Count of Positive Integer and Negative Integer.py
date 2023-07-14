class Solution:
    def maximumCount(self, nums: List[int]) -> int:

      neg = 0
      pos = 0
      
      for num in nums:
        if num > 0:
          pos += 1
        elif num < 0:
          neg += 1

      return max(neg, pos)

