class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sumi = sum(nums)
        count = 0
        acc = 0

        for i in range(len(nums) - 1):
            acc += nums[i]
            if acc >= sumi - acc:
                count += 1

        return count
        
