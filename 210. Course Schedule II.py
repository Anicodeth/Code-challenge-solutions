class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            indegree[dest] = indegree.get(dest, 0) + 1

        zero_indegree = deque([k for k in range(numCourses) if k not in indegree])

        res = []

        while zero_indegree:
            vertex = zero_indegree.popleft()
            res.append(vertex)

            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        zero_indegree.append(neighbor)

        return res if len(res) == numCourses else []
