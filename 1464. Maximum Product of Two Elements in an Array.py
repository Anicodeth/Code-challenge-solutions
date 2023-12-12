class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [ -num for num in nums ]
        heapq.heapify(nums)
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)

        return (-first - 1) * (-second - 1)
        
