class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        n = len(nums)
        
        for i in range(n - 1, 1 ,-1):
            side1 = nums[i]
            side2 = nums[i - 1]
            side3 = nums[i - 2]

            if side2 + side3 > side1:
                return side1 + side2 + side3

        return 0
