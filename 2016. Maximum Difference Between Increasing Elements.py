class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        globalMax = -1
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                value1 = nums[i]
                value2 = nums[j]

                if value1 < value2:
                    globalMax = max(globalMax, value2 - value1)

        return globalMax
        
