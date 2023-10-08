from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, end, cost in flights:
            graph[start].append((end, cost))
        
        min_cost = inf
        queue = [(0, 0, src)]  
        visited = set()
        
        while queue:
            total_cost, stops, current_city = heappop(queue)
            
            if current_city == dst:
                min_cost = min(min_cost, total_cost)
            
            if stops > k or (current_city, stops) in visited:
                continue
            
            visited.add((current_city, stops))
            
            for neighbor, edge_cost in graph[current_city]:
                heappush(queue, (total_cost + edge_cost, stops + 1, neighbor))
        
        return min_cost if min_cost != inf else -1
