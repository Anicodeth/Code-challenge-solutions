class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()

        pairs = [ (nums[i], nums[-i - 1]) for i in range(len(nums))]
        return max(a + b for a, b in pairs)
        
