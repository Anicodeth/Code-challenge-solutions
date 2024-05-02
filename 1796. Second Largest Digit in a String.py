class Solution:
    def secondHighest(self, s: str) -> int:
        values = set()
        heap = []
        for c in s:
            if c.isdigit() and int(c) not in values:
                values.add(int(c))
                heapq.heappush(heap, -int(c))

        if heap: heapq.heappop(heap) 
        return -heapq.heappop(heap) if heap else -1
        
