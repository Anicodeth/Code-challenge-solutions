class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        maxi = 0
        
        def dfs(i, j, curr):
            
          nonlocal maxi
          if i >= m or i < 0 or j >= n or j < 0 or (i, j) in visited or grid[i][j] == 0:
            return

          visited.add((i, j))
          curr += grid[i][j]
          if curr > maxi:
            maxi = curr

          dfs(i + 1, j, curr)
          dfs(i - 1, j, curr)
          dfs(i , j + 1, curr)
          dfs(i , j - 1, curr)
          visited.remove((i, j))

        for i in range(m):
          for j in range(n):
            if grid[i][j] != 0:
              visited = set()
              dfs(i,j,0)
        return maxi
