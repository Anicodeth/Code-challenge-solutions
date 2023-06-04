
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      memo = {}
      def dp(i, j):
        if (i, j) in memo:
          return memo[(i,j)]
        if j < 0 or j >= m or i >= n:
          return 0 

        if j == m - 1 and i == n - 1:
          return 1

        memo[(i, j)] = dp(i + 1, j) + dp(i, j + 1)
        return memo[(i, j)]


      return dp(0,0)
