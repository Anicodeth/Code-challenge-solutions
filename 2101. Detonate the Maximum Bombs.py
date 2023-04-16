from collections import defaultdict

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def is_connected(a,b):
            x1, y1, r1 = bombs[a]
            x2, y2, r2 = bombs[b]
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            if  dist <= r1:
              return True
            else:
              return False


        conn = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    if is_connected(i,j):
                        conn[i].append(j)

        def dfs(bomb):
          if bomb in visited:
            return

          visited.add(bomb)
          self.localmax += 1

          for detonate in conn[bomb]:
                dfs(detonate)
   


        self.maxi = 1
        for bomb in list(conn.keys()):
          self.localmax = 0
          visited = set()
          dfs(bomb)
          self.maxi = max(self.maxi, self.localmax)

        return self.maxi


        
