class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:

        counter = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 
            
            grid[i][j] = 2
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        m, n = len(grid), len(grid[0])

        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    counter += 1
                    

        return counter

        
