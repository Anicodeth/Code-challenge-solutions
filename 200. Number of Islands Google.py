class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(i,j):
            que = deque([(i,j)])

            while que:
                i, j = que.pop()
                if i >= n or i < 0 or j < 0 or j >= m or grid[i][j] != "1" or (i,j) in visited:
                    continue
                visited.add((i, j))
                que.extend([(i + 1, j), (i - 1, j), (i , j + 1), (i , j - 1)])

        n = len(grid)
        m = len(grid[0])

        visited = set()
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visited:
                    bfs(i,j)
                    count += 1

        return count
        
