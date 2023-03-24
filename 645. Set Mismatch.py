class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      unique = set()
      res = []

      for i in nums:
        if i not in unique:
          unique.add(i)
        else:
          res.append(i)

      for i in range(1,len(nums)+1):
        if i not in unique:
          res.append(i)

      return res          



        
