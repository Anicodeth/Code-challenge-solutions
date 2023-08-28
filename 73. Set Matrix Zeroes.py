class Solution:    
    def setZeroes(self, matrix: List[List[int]]) -> None:
      n = len(matrix)
      m = len(matrix[0])
      def isValid(i , j ):
        return not (i < 0 or j < 0 or i >= n or j >=m )

        
      def dfs(i, j, ops):
        if ops == 'A':
          dfs(i, j, 'U')
          dfs(i, j, 'D')
          dfs(i, j, 'L')
          dfs(i, j, 'R')

        if ops == 'U' and isValid(i - 1, j): 
          dfs(i - 1, j, 'U')
          if matrix[i - 1][j] != 0:
            matrix[i- 1][j] = inf
        elif ops == 'D' and isValid(i + 1, j):
          dfs(i + 1, j, 'D')
          if matrix[i + 1][j] != 0:
            matrix[i + 1][j] = inf
        elif ops == 'L' and isValid(i , j - 1):
          dfs(i , j - 1, 'L')
          if matrix[i][j - 1] != 0:
            matrix[i][j -1] = inf
        elif ops == 'R' and isValid(i , j + 1):
          dfs(i , j + 1, 'R')
          if matrix[i][j + 1] != 0:
            matrix[i][j + 1] = inf

      for i in range(n):
        for j in range(m):
          if matrix[i][j] == 0:
            dfs(i, j, 'A')

      for i in range(n):
        for j in range(m):
          if matrix[i][j] == inf:
            matrix[i][j] = 0

      return matrix
