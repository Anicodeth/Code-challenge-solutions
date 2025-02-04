class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        running = 0
        prev = -1
        maxi = -1

        for num in nums:
            if num > prev:
                running += num
                maxi = max(maxi, running)
            else: running = num
            prev = num

        return maxi 
                
