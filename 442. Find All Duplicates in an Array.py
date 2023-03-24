class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
      unique = set()
      dups = []

      for i in nums:
        if i not in unique:
          unique.add(i)
        else:
          dups.append(i)

      return dups

