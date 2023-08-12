class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
      n = len(nums)

      left = [0] * n
      right = [0] * n

      for i in range(n-1):
        left[i + 1] = left[i] + nums[i]

      for i in range(n- 1, 0, -1):
        right[i - 1] = right[i] + nums[i]

      res = []

      for i in range(n):
        res.append(abs(left[i] - right[i]))


      return res
