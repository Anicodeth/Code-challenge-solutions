class Solution:
    def knightDialer(self, n: int) -> int:
        keyboard = [
            ['1', '2', '3'],
            ['4', '5', '6'],
            ['7', '8', '9'],
            ['*', '0', '#'],
        ]
        visited = set([(3, 0), (3, 2)])
        memo = {}

        d = [
            (1, 2),
            (2, 1),
            (2, -1),
            (1, -2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),  
        ]

        def is_valid(i, j):
            return 0 <= i <= 3 and 0 <= j <= 2

        def dfs(i, j, curr):
            typed = len(curr)
            if (i, j) in visited:
                return 0
            elif typed == n:
                return 1
            elif (i, j, typed) in memo:
                return memo[(i, j, typed)]
            
            sumi = 0
            for x, y in d:
                ni, nj = i + x, j + y
                if is_valid(ni, nj):
                    sumi += dfs(ni, nj, curr + keyboard[ni][nj])
            memo[(i, j, typed)] = sumi
            return sumi
        res = 0
        for i in range(4):
            for j in range(3):
                res += dfs(i, j, keyboard[i][j])

        return res % ((10**9) + 7)
