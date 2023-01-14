class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        ans = 0

        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):

                sm = ( grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                                      + grid[i  ][j] +
                       grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1] )

                if sm > ans: ans = sm

        return ans
