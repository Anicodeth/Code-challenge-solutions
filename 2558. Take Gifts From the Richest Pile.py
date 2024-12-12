class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [ -gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            largest = heapq.heappop(gifts)
            updated = floor(sqrt(-largest))
            heapq.heappush(gifts, -updated)

        return -sum(gifts)
