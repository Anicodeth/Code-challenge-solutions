class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ranges = []

        n = len(nums)

        for i in range(n):
            mini = nums[i]
            maxi = nums[i]
            for j in range(i + 1, n):
                
                if mini > nums[j]:
                    mini = nums[j]
                elif maxi < nums[j]:
                    maxi = nums[j]
                r = maxi - mini
                ranges.append(r)

        return sum(ranges)
        
