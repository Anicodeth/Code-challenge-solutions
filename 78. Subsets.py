class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      subsets = []
      def back_track(curr, i):
        subsets.append(curr)

        for i in range(i,len(nums)):
          back_track(curr + [nums[i]], i + 1)
      back_track([], 0)
      return subsets





