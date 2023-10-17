class Solution:
    def smallestRangeI(self, nums: List[int], k: int):
        score = max(nums) - min(nums)
        delta = score - 2 * k
        return max(delta, 0)
                
        
