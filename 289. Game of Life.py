class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        def is_valid(i,j):
            return i >= 0 and i < m and j >= 0 and j < n

        matrix = [[board[i][j] for j in range(n)] for i in range(m)]
        ne = [(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1, 0),(-1, 0)]
        for i in range(m):
            for j in range(n):
                live = dead = 0
                for a,b in ne:
                    if is_valid(i + a, j + b):
                        if board[i + a][j + b]:
                            live += 1
                        else:
                            dead += 1
                if board[i][j] and (live == 2 or live == 3):
                    continue
                elif board[i][j] and (live < 2 or live > 3):
                    matrix[i][j] = 0
                elif not board[i][j] and live == 3:
                    matrix[i][j] = 1

        for i in range(m):
            for j in range(n):
                board[i][j] = matrix[i][j]


