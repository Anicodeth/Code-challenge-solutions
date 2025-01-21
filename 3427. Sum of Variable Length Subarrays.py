class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        running = 0
        for i, num in enumerate(nums):
            start = max(0, i - num)
            running += (prefix[i + 1] - prefix[start])

        return running 
        
