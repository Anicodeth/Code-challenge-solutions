class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        minLocal = nums[0]
        maxLocal = nums[0]

        maxGlobal = maxLocal

        for i, num in enumerate(nums):
            if i == 0: continue
            one = minLocal * num
            two = maxLocal * num

            minLocal = min(num, one, two)
            maxLocal = max(num, one, two)

            maxGlobal = max(maxGlobal, maxLocal)

            print(minLocal, maxLocal, num)

        return maxGlobal
        
