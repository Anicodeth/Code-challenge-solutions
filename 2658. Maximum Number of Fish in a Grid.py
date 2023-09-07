class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:  

      m = len(grid)
      n = len(grid[0])
      maxi = 0
      def dfs(i, j):
        nonlocal final
        if i >= m or i < 0 or j >= n or j < 0 or (i, j) in visited or grid[i][j] == 0:
          return 

        visited.add((i, j))
        final += grid[i][j]
        
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i , j + 1)
        dfs(i , j - 1)


      for i in range(m):
        for j in range(n):
          if  grid[i][j] > 0:  
            visited = set()
            final = 0
            dfs(i, j)
            if final > maxi:
              maxi = final

      return maxi
