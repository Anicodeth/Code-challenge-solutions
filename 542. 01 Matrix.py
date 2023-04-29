class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        for i in range(m):
          for j in range(n):
            if mat[i][j] == 0:
              q.append((i, j, 0))
            else:
              mat[i][j] = -1
        
        while q:
          i, j, dist = q.popleft()
          for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and mat[ni][nj] == -1:
              mat[ni][nj] = dist + 1
              q.append((ni, nj, dist + 1))
              
        return mat
