class Solution:    
    def shortestBridge(self, grid: List[List[int]]) -> int:
       
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def is_valid(i, j):
            return  0 <= i < m and 0 <= j < n
        def dfs(i, j, queue, visited,grid):
            if i >= m or i < 0 or j >= n or j < 0 or grid[i][j] != 1 or (i, j) in visited:
                return 

            visited.add((i, j))
            queue.append((i, j, 0)) 
             
            dfs(i + 1, j, queue, visited,grid)
            dfs(i - 1, j, queue, visited,grid)
            dfs(i, j + 1, queue, visited,grid)
            dfs(i, j - 1, queue, visited,grid)


        # find one island using DFS
        queue = deque()
        done = False
        for i in range(m):
            if done: break
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j,queue, visited,grid)
                    done = True
                    break

        # BFS to find the shortest bridge
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j, moves = queue.popleft()
            
            for a, b in directions:
                if is_valid(i + a, j + b) and (i + a, j + b) not in visited:       
                    if grid[i + a][j + b] == 1:
                            return moves

                    visited.add((i + a , j + b))
                    queue.append((i + a, j + b, moves + 1))

