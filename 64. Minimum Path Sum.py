class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]):
                return float('inf')

            if (i, j) in memo:
                return memo[(i, j)]

            if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
                memo[(i, j)] = grid[i][j]
            else:
                right_sum = dfs(i, j + 1)
                down_sum = dfs(i + 1, j)
                memo[(i, j)] = grid[i][j] + min(right_sum, down_sum)

            return memo[(i, j)]

        memo = {}
        return dfs(0, 0)
