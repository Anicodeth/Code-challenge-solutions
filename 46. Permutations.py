class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

      permute = []

      self.length = len(nums)

      def backtrack(start):
        if start == self.length:
          permute.append(nums[:])

        for i in range(start, self.length):
          nums[i], nums[start] = nums[start], nums[i]
          backtrack(start + 1)
          nums[i], nums[start] = nums[start], nums[i]

      backtrack(0)
      return permute
        
