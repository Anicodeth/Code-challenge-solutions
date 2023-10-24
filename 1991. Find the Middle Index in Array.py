class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        prefix_sum_forward = nums[:]
        prefix_sum_backward = nums[:]
        
        for i in range(1, n):
            prefix_sum_forward[i] += prefix_sum_forward[i - 1]
        
        for i in range(n - 2, -1, -1):
            prefix_sum_backward[i] += prefix_sum_backward[i + 1]
        
        if prefix_sum_backward[1] == 0:
            return 0
        
        for i in range(1, n - 1):
            if prefix_sum_forward[i - 1] == prefix_sum_backward[i + 1]:
                return i
        
        if prefix_sum_forward[-2] == 0:
            return n - 1
        
        return -1
