class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
            if not grid:
                return 0

            rows, cols = len(grid), len(grid[0])
            fresh_oranges = 0
            rotten_oranges = deque()


            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1:
                        fresh_oranges += 1
                    elif grid[i][j] == 2:
                        rotten_oranges.append((i, j, 0))  

            if fresh_oranges == 0:
                return 0  

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            minutes = 0

            while rotten_oranges:
                i, j, minutes = rotten_oranges.popleft()

                for dr, dc in directions:
                    ni, nj = i + dr, j + dc

                    if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                        grid[ni][nj] = 2  
                        fresh_oranges -= 1
                        rotten_oranges.append((ni, nj, minutes + 1))

            return minutes if fresh_oranges == 0 else -1
