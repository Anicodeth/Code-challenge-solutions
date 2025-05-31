class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        #I know it can be solved using BFS but that's too boring
        #Let's slighly complicate things and do Dijkstra :)

        graph = defaultdict(list)
        for i, j in enumerate(edges):
            if j != -1:
                graph[i].append(j)

        def djs(graph, tracker, start, visited):
            heap = [(0, start)]
            tracker[start] = 0

            while heap:
                dis, node = heapq.heappop(heap)

                if node in visited:
                    continue
                visited.add(node)

                for child in graph[node]:
                    if child not in visited:
                        new_dist = dis + 1
                        if child not in tracker or new_dist < tracker[child]:
                            tracker[child] = new_dist
                            heapq.heappush(heap, (new_dist, child))

        tracker1 = {}
        tracker2 = {}

        djs(graph, tracker1, node1, set())
        djs(graph, tracker2, node2, set())

        res = inf
        answer = -1

        for i in range(len(edges)):
            if i in tracker1 and i in tracker2:
                max_dist = max(tracker1[i], tracker2[i])
                if max_dist < res or (max_dist == res and i < answer):
                    res = max_dist
                    answer = i

        return answer
