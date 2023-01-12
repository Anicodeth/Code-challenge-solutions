
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
            cols, rows = [0] * len(board), [0] * len(board[0])
            
            diagonal, anti_diagonal = 0, 0
            turn, x_win, o_win = 0, False, False

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 'X':
                        turn += 1
                        rows[i] += 1
                        cols[j] += 1
                        if i == j:
                            diagonal += 1
                        if i + j == len(board) - 1:
                            anti_diagonal += 1
                    elif board[i][j] == 'O':
                        turn -= 1
                        rows[i] -= 1
                        cols[j] -= 1
                        if i == j:
                            diagonal -= 1
                        if i + j == len(board) - 1:
                            anti_diagonal -= 1

            for idx in range(len(cols)):
                if cols[idx] == 3 or rows[idx] == 3 or diagonal == 3 or anti_diagonal == 3:
                    x_win = True
                    break
                elif cols[idx] == -3 or rows[idx] == -3 or diagonal == -3 or anti_diagonal == -3:
                    o_win = True
                    break

            if (turn != 1 and x_win) or (turn != 0 and o_win):
                return False

            return turn == 1 or turn == 0
