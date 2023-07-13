class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      n = len(board)
      m = len(board[0])
      res = False
      
      
      def backtrack(cord, search, visited):
        nonlocal res
        i, j = cord

        
        if search == len(word):
          res = True
          return

        if i < 0 or i >= n or j < 0 or j >=m or (i,j) in visited or board[i][j] != word[search]:
          return

        visited.add((i,j))

        backtrack((i + 1, j), search + 1, visited)
        backtrack((i , j + 1), search + 1, visited)
        backtrack((i - 1, j), search + 1, visited)
        backtrack((i , j - 1), search + 1, visited)

        visited.remove((i, j))




      for i in range(n):
        for j in range(m):
          visited = set()
          if board[i][j] == word[0]:
            backtrack((i, j), 0, visited)

      return res


      
