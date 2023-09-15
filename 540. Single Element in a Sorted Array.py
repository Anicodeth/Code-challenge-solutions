class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if  (i + 1 >= n or (nums[i] != nums[i + 1])) and ( i - 1 < 0 or (nums[i] != nums[i - 1])):
                return nums[i]
        
