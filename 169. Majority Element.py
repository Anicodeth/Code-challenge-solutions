class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      res = []
      count = Counter(nums)
      n = len(nums)

      for val in count:
        if count[val] > n//3:
          res.append(val)

      return res
