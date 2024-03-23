class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegree = { i:0 for i in range(1, n + 1)}

        for a, b in relations:
            graph[a].append(b)
            indegree[b] += 1

        que = deque()

        for node, degrees in indegree.items():
            if degrees == 0:
                que.append(node)

        semesters = 0

        visited = []

        while que:
            courses = len(que)
            for _ in range(courses):
                node = que.popleft()
                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        que.append(child)

                visited.append(node)

            semesters += 1

        if len(visited) == n:
            return semesters
        else:
            return -1
        
