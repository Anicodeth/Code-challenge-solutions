class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n = len(board)
        m = len(board[0])
        
        def isValid(i, j):
            return 0 <= i < n and 0 <= j < m 
        
        def dfs(i, j, dirr):
            if not isValid(i, j) or board[i][j] == '.':
                return

            board[i][j] = '0'
            if dirr == 'r':
                dfs(i + 1, j, dirr)
            else:
                dfs(i, j + 1, dirr)

        count = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X':
                    if isValid(i + 1, j) and board[i + 1][j] == "X":
                        dfs(i, j, 'r')
                        count += 1
                    if isValid(i, j + 1) and board[i][j + 1] == "X":
                        dfs(i, j, 'd')
                        count += 1
                    if board[i][j] == 'X':
                        count += 1
                        board[i][j] = '0'
        return count
