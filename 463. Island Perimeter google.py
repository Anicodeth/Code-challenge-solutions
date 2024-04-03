class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 1
            elif (i, j) in visited:
                return 0

            visited.add((i, j))
            local = 0
            for dx, dy in directions:
                local += dfs(i + dx, j + dy)

            return local


        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return dfs(i, j)
        
        
