class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rookRow, rookCol = -1, -1
        captures = 0
        
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rookRow, rookCol = i, j
                    break
        
        rowDirs = [-1, 0, 1, 0]
        colDirs = [0, 1, 0, -1]
        
        for d in range(4):
            newRow, newCol = rookRow + rowDirs[d], rookCol + colDirs[d]
            
            while 0 <= newRow < 8 and 0 <= newCol < 8:
                if board[newRow][newCol] == 'B':
                    break  
                if board[newRow][newCol] == 'p':
                    captures += 1
                    break  
                newRow += rowDirs[d]
                newCol += colDirs[d]
        
        return captures
