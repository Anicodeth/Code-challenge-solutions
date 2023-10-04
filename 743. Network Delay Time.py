class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1, n + 1)}

        for u, v, w in times:
            graph[u].append((v, w))
            
        def dijkstra(graph, start):
            distances = {node: inf for node in graph}
            distances[start] = 0
            
            visited = set()
            priority_queue = [(0, start)]
            
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                
                if current_node in visited:
                    continue
                visited.add(current_node)
                
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
            
            return distances

        shortest_distances = dijkstra(graph, k)

        if any(dist == inf for dist in shortest_distances.values()):
            return -1
        
        return max(shortest_distances.values())
