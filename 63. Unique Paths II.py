class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

      memo = {}

      n = len(obstacleGrid)
      m = len(obstacleGrid[0])

      def dp(i, j):

        if i < 0 or j < 0 or i >= n or j >= m or obstacleGrid[i][j] == 1:
          return 0
        elif i == n - 1 and j == m - 1:
          return 1
        elif (i,j) in memo:
          return memo[(i,j)]

        right = dp(i, j + 1)
        down = dp(i + 1, j)

        memo[(i, j)] = right + down

        return memo[(i,j)]

      return dp(0,0)
