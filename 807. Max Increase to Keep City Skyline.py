class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        n = len(grid)

        rowMax = {}
        colMax = {}

        for i in range(n):
            for j in range(n):
                rowMax[i] = max(grid[i][j], rowMax.get(i, 0))
                colMax[j] = max(grid[i][j], colMax.get(j, 0))

        res = 0
        for i in range(n):
            for j in range(n):
                res += abs(grid[i][j] - min(rowMax[i], colMax[j]))

        return res
