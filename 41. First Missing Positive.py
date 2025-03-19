class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and nums[i] - 1 != i and nums[nums[i] - 1] - 1 != nums[i] - 1:
                temp = nums[i]
                nums[i], nums[temp- 1] = nums[temp - 1], nums[i]

        for i in range(n):
            if nums[i] - 1 != i:
                return i + 1

        return n + 1
