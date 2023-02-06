class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        no_of_rows=len(grid)
        no_of_cols=len(grid[0])
        localmax=[]

        for i in range(no_of_rows - 2):
            rowmax=[]
            for j in range(no_of_cols -2):
                rowmax.append(max(max(grid[i][j:j+3]),max(grid[i+1][j:j+3]),max(grid[i+2][j:j+3])))
            localmax.append(rowmax)

        return localmax
                
