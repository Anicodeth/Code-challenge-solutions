class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        rows = [ 0 for _ in range(m)]
        cols = [ 0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    rows[i] += 1
                    cols[j] += 1

        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and rows[i] == n - 1 and cols[j] == m - 1:
                    count += 1

        return count
                    
