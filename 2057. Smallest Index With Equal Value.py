class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
      mini = inf

      for i, num in enumerate(nums):
        if i % 10 ==  num:
          mini = i
          break
      
      return mini if mini != inf else -1
