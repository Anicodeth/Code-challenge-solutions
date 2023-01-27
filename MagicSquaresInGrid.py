class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        no_of_rows=len(grid)
        no_of_cols=len(grid[0])
        count=0

        if no_of_cols < 3 or no_of_rows < 3:
            return 0

        for row in range(no_of_rows-2):
            for entry in range(no_of_cols-2):
                if(sorted(set(grid[row][entry:entry+3]+grid[row+1][entry:entry+3]+grid[row+2][entry:entry+3]))!=[1,2,3,4,5,6,7,8,9]):
                    continue
                row0=sum(grid[row][entry:entry+3])
                row1=sum(grid[row+1][entry:entry+3])
                row2=sum(grid[row+2][entry:entry+3])

                col0=sum([grid[row][entry],grid[row+1][entry],grid[row+2][entry]])
                col1=sum([grid[row][entry+1],grid[row+1][entry+1],grid[row+2][entry+1]])
                col2=sum([grid[row][entry+2],grid[row+1][entry+2],grid[row+2][entry+2]])

                diagonal=sum([grid[row][entry],grid[row+1][entry+1],grid[row+2][entry+2]])
                anti_diagonal=sum([grid[row][entry+2],grid[row+1][entry+1],grid[row+2][entry]])

                if(row0==row1==row2==col0==col1==col2==diagonal==anti_diagonal):
                    count+=1

        return count
