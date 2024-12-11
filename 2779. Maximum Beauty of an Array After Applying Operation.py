class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        maxi = 0
        l = 0
        nums.sort()
        
        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1

            maxi = max(maxi, r - l + 1)

        return maxi
