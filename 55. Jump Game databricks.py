class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = n - 1

        for i in range(n - 1, -1, -1):
            if nums[i] + i >= reach:
                reach = i

        return not reach
