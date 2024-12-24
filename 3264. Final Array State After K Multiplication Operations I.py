class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        nums = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(nums)
        
        for _ in range(k):
            value, i = heapq.heappop(nums)
            value *= multiplier
            heapq.heappush(nums, (value, i))

        nums.sort(key = lambda x : x[1])
        nums = [ num for num, _ in nums]
        
        return nums
