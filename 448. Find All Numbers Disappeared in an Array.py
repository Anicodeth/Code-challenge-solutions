class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
      unique = set()

      notfound = []

      for i in nums:
        if i not in unique:
          unique.add(i)

      for i in range(1, len(nums)+1):
        if i not in unique:
          notfound.append(i)

      return notfound
