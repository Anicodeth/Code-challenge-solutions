class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        p1, p2, p3, count = 0, 1, 2, 0
        n = len(nums)

        for i in range(n - 2):
            if nums[p1 + i] + nums[p3 + i] == nums[p2 + i] / 2: count += 1

        return count
