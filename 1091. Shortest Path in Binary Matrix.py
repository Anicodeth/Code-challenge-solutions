class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        
        q = deque()
        q.append((0, 0, 1))
        visited = set()
        visited.add((0, 0))
        
        while q:
            i, j, dist = q.popleft()
            
            if i == n-1 and j == n-1:
                return dist
            
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)]:
                if 0 <= x < n and 0 <= y < n and grid[x][y] == 0 and (x, y) not in visited:
                    visited.add((x, y))
                    q.append((x, y, dist+1))
                    
        return -1

        
