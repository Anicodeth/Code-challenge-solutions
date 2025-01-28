class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total, n = sum(nums), len(nums)
        running, count = 0, 0
    
        for i in range(n - 1):
            curr = abs(nums[i] - (total - nums[i]))
            if curr % 2 == 0: count += 1

        return count
