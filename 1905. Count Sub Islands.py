class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

      def dfs(i,j,grid,land):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
          return
        land.add((i,j))
        grid[i][j] = 2

        dfs(i - 1, j, grid,land)
        dfs(i , j - 1, grid,land)
        dfs(i + 1, j, grid,land)
        dfs(i , j + 1, grid,land)

      land = set()
      for i in range(len(grid1)):
        for j in range(len(grid1[0])):
          if grid1[i][j] != 2 and grid1[i][j] == 1:
            dfs(i,j,grid1,land)
      
      count = 0

      for i in range(len(grid1)):
        for j in range(len(grid1[0])):
          if grid2[i][j] != 2 and grid2[i][j] == 1:
            land1 = set()
            dfs(i,j,grid2,land1)
            if land1.issubset(land):
              count += 1


      return count



      
      


      
