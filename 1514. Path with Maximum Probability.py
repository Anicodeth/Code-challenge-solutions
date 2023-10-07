class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        visited = set()
        for edge, p in zip(edges, succProb):
            graph[edge[0]].append((edge[1], p))
            graph[edge[1]].append((edge[0], p))
        values = {i: 0 for i in range(n)}
        values[start_node] = 1
        
        heap = [(-1, start_node)]

        #Djkistra
        while heap:
            probablity, node = heapq.heappop(heap)
            visited.add(node)
            for child, multiplier in graph[node]:
                if child not in visited:
                    newProb = max(values[child], -probablity * multiplier)
                    values[child] = newProb
                    heapq.heappush(heap, (-newProb, child))
        
        return values[end_node]

        
