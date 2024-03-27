class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        visited = {}

        n = len(graph)

        def dfs(node, color):
            if node in visited:
                return color == visited[node]

            visited[node] = color

            check = True
            for child in graph[node]:
                check &= dfs(child, ~color)

            return check


        
        res = True
        for i in range(n):
            if i not in visited:
                res &= dfs(i, 0)
                if res == False:
                    return False

        return True

        
