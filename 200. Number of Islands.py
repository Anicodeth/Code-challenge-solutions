class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      count = 0

      def dfs(i,j):

        if i >= len(grid) or 0 > i or 0 > j or j >=len(grid[0]) or grid[i][j] == "0" or grid[i][j] == "2":
          return 
        
        grid[i][j] = "2"

        if i+1 < len(grid) and grid[i+1][j] != "2":
          dfs(i+1, j)
        if j+1 < len(grid[0]) and grid[i][j+1] != "2":
          dfs(i, j + 1)
        if i-1 >= 0 and grid[i - 1][j] != "2":
          dfs(i - 1, j)
        if  j-1 >= 0 and grid[i][j - 1] != "2":
          dfs(i, j - 1)


      for i in range(len(grid)):
        for j in range(len(grid[0])):
          
          if  grid[i][j] == "1":
            dfs(i,j)
            count += 1



      return count

          
