class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
            board = [[ '.' for _ in range(n) ] for _ in range(n)]
            res = []

            def build(board):
                ans = []
                for row in board:
                    ans.append("".join(row))
                return ans
        
            def backtrack(board, row, cols, diagonals,antis):
                nonlocal res
                if row == n:
                    res.append(build(board))
                    return

                for i in range(n):
                    if (i in cols) or (row - i in diagonals) or (i + row in antis):
                        continue

                    board[row][i] = 'Q'
                    cols.add(i)
                    diagonals.add(row - i)
                    antis.add(row + i)

                    backtrack(board, row + 1, cols, diagonals, antis)

                    board[row][i] = '.'
                    cols.remove(i)
                    diagonals.remove(row - i)
                    antis.remove(row + i)

                return

            backtrack(board, 0, set(), set(), set())

            return res
