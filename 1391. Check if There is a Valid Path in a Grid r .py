class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        p, rank = [[(i, j) for j in range(m)] for i in range(n)], [[1 for _ in range(m)] for _ in range(n)]

        def get(i, j):
            while p[i][j] != (i, j):
                i, j = p[i][j]
            return i, j

        def connect(i1, j1, i2, j2):
            i1, j1 = get(i1, j1)
            i2, j2 = get(i2, j2)
            if rank[i1][j1] >= rank[i2][j2]:
                p[i2][j2] = p[i1][j1]
                rank[i1][j1] += 1
            else:
                p[i1][j1] = p[i2][j2]
                rank[i2][j2] += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] in [1, 4, 6] and j+1 < m and grid[i][j+1] in [1, 3, 5]:
                    connect(i, j, i, j+1)
                if grid[i][j] in [2, 3, 4] and i+1 < n and grid[i+1][j] in [2, 5, 6]:
                    connect(i, j, i+1, j)

        return get(0, 0) == get(n-1, m-1)
