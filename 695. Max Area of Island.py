class Solution:
    def __init__(self):
      self.localmax = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
      def dfs(i,j):
        if i >= len(grid) or 0 > i or 0 > j or j >=len(grid[0]) or grid[i][j] == 0 or grid[i][j] == 2:
          return 
        grid[i][j] = 2
        self.localmax += 1
        if i+1 < len(grid) and grid[i+1][j] != 2:
          dfs(i+1, j)
        if j+1 < len(grid[0]) and grid[i][j+1] != 2:
          dfs(i, j + 1)
        if i-1 >= 0 and grid[i - 1][j] != 2:
          dfs(i - 1, j)
        if  j-1 >= 0 and grid[i][j - 1] != 2:
          dfs(i, j - 1)

      maxi = 0
      for i in range(len(grid)):
        for j in range(len(grid[0])):
          self.localmax = 0
          if  grid[i][j] == 1:
            dfs(i,j)
            if self.localmax > maxi:
              maxi = self.localmax

      return maxi
