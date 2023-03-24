class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      dup = set()

      for i in nums:
        if i in dup:
          return i
        else:
          dup.add(i)
