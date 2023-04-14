class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

      n = len(nums)
      max_or = 0
      count = 0
      for i in range(1, 2**n):
          subset_or = 0
          for j in range(n):
              if i & (1 << j):
                  subset_or |= nums[j]
          if subset_or > max_or:
              max_or = subset_or
              count = 1
          elif subset_or == max_or:
              count += 1
      return count
