class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        visited = set()
        n = len(matrix)
        mini = inf
        directions = [(1,-1), (1,0), (1, 1)]

        def fall(i, j):
            ti, tj = i, j
            if i == n - 1 and j >= 0 and j < n:
                return matrix[i][j]
            if i == n or j < 0 or j >= n:
                return inf

            if (i,j) in memo:
                return memo[(i,j)]

            local = inf

            for d in directions:
                ni, nj = i + d[0], j + d[1]
                val = fall(ni, nj)

                if local > val:
                    local = val

            memo[(ti, tj)] = local + matrix[ti][tj]

            return memo[(ti, tj)]

        for j in range(n):
            mini = min(mini, fall(0, j))

        return mini
