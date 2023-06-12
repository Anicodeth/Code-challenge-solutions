class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

      def bfs():

        que = deque([(entrance[0], entrance[1] , 0)])
        visited = set([(entrance[0], entrance[1])])

        while que:

          i, j, m= que.popleft()

          nextStates = [(i + 1, j, m + 1), (i - 1, j, m + 1), (i, j - 1, m + 1), (i, j + 1, m + 1)]

          for i,j,m in nextStates:
            
            if  (i,j) in visited or i >= len(maze) or i < 0 or j >= len(maze[0]) or j < 0 or maze[i][j] == "+":
              continue

            if  (maze[i][j] == '.') and ( i + 1 >= len(maze) or i - 1 < 0 or j + 1 >= len(maze[0]) or j - 1 < 0):
                return m
              
            visited.add((i,j))
            que.append((i,j,m))
        return inf
      
      value = bfs()
      return value if value != inf else -1
      



