class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        
        heap = [(-nums[0], 0)]
        n = len(nums)
        res = nums[0]
        for i in range(1, n):
            while i - (heap[0][1]) > k:
                heapq.heappop(heap)
            track = max(-heap[0][0], 0)
            curr = (track) + nums[i]
            res = max(curr, res)
            heapq.heappush(heap, (-max(nums[i], curr), i))

        return res
        
