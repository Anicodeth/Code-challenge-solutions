class Solution:
    def convert(self, s: str, numRows: int) -> str:
      if numRows  == 1: return s
      down = (1, 0)
      zigup = (-1, 1)
      direction = down

      mat = [[0] * len(s) for _ in range(numRows)]
      pos = [0,0]
      for i in range(len(s)):
        mat[pos[0]][pos[1]] = s[i]
        if pos[0] == numRows - 1:
          direction = zigup
        elif pos[0] == 0:
          direction = down
        a, b = direction

        pos[0] += a
        pos[1] += b

      res = []
      for i in range(numRows):
        for j in range(len(s)):
          if mat[i][j] != 0:
            res.append(mat[i][j])

      return "".join(res)

        
