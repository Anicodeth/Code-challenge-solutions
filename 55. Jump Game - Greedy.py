class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        last = n - 1

        for i in range(n - 2, -1, -1):
            if nums[i] >= last - i:
                last = i
        
        return 0 == last

        
