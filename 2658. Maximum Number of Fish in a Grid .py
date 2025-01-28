class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:

        n, m = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j, visited):
            nonlocal n,m
            if i >= n or i < 0 or j >=m or j < 0 or (i, j) in visited or grid[i][j] == 0:
                return 0

            visited.add((i, j))

            up = dfs(i + 1, j, visited)
            down = dfs(i - 1, j, visited)
            right = dfs(i, j + 1, visited)
            left = dfs(i, j - 1, visited)

            combined = up + down + right + left + grid[i][j]
            return combined

        maxi = -1

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 or (i, j) not in visited: 
                    maxi = max(dfs(i, j, visited), maxi)

        return maxi
