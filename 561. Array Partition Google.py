class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sumi = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                sumi += nums[i]


        return sumi
        
