class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def adj_mine_count(i,j):
            mine_count = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x != 0 or y != 0:
                        if i+y >= 0 and i + y < len(board) and  j + x >= 0 and j + x < len(board[0]) and board[i+y][j+x] == "M":
                            mine_count += 1
            return mine_count

        def dfs(i, j):
            if board[i][j] == "M":
                board[i][j] = "X"
                return 
            
            mine_count = adj_mine_count(i, j)
            if mine_count != 0:
                board[i][j] = str(mine_count)
            else:
                board[i][j] = "B"
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x != 0 or y != 0:
                            if i+y >= 0 and i + y < len(board) and  j + x >= 0 and j + x < len(board[0])  and board[i+y][j+x] == "E":
                                dfs(i+y, j+x)
        
        dfs(click[0], click[1])

        return board                
