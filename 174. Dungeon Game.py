
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        memo = {}

        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return max(1, 1 - dungeon[i][j])

            if i >= m or j >= n:
                return inf

            if (i, j) in memo:
                return memo[(i, j)]

            right = dp(i, j + 1)
            down = dp(i + 1, j)
            min_health = min(right, down) - dungeon[i][j]
            min_health = max(1, min_health)
            memo[(i, j)] = min_health

            return min_health

        return dp(0, 0)

        
