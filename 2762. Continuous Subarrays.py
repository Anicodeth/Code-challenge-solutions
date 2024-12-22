class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        total = 0
        minHeap = []
        maxHeap = []

        for r in range(n):
            while minHeap and abs(nums[r] - minHeap[0][0]) > 2:
                    l = max(l, minHeap[0][1])
                    heapq.heappop(minHeap)

            while maxHeap and abs(nums[r] - (-maxHeap[0][0])) > 2:
                    l = max(l, maxHeap[0][1])
                    heapq.heappop(maxHeap)

            heapq.heappush(minHeap, (nums[r], r + 1))
            heapq.heappush(maxHeap, (-nums[r], r + 1))

            total += (r - l + 1)

        return total
