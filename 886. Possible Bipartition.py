class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

      graph = defaultdict(list)
      visited = [0] * n

      self.bi = True

      for dis in dislikes:
        graph[dis[0]].append(dis[1])
        graph[dis[1]].append(dis[0])

      def dfs(node, color):
        if visited[node-1] != color and visited[node-1] != 0 :
          self.bi = False
          return
        if visited[node-1] != 0:
          return
        visited[node-1] = color
        for i in graph[node]:
          dfs(i, 1  if color == 2 else 2)
      for i in range(1 , n+1):
        if visited[i - 1] != 0:
          continue
        dfs(i,1)

      return self.bi




        
