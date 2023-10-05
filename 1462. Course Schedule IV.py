class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        def dfs(pre, chi):
            if pre == chi:
                return True

            visited.add(chi)
            for child in graph[chi]:
                if child not in visited and dfs(pre, child):
                    return True

            return False

        answer = []

        for u, v in queries:
            visited = set()
            if dfs(u, v):
                answer.append(True)
            else:
                answer.append(False)

        return answer
