class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        temp = nums[:]
        nums.sort()
        start = end = 0
        n = len(nums)

        for i in range(n):
          if temp[i] != nums[i]:
            start = i
            break
        for i in range(n - 1, -1, -1):
          if temp[i] != nums[i]:
            end = i
            break

        return end - start + 1 if end - start != 0 else 0
