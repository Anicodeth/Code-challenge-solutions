class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        
        return True
        
