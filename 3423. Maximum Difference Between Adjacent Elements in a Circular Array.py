class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        maxi = -1
        n = len(nums)
        for i in range(n - 1, -2, -1):
            maxi = max(maxi, abs(nums[i] - nums[i - 1]))

        return maxi
        
