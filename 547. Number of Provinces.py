class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
      n = len(isConnected)
      visited = [False] * n
      numProvinces = 0
      def dfs(city):
          visited[city] = True
          for neighbor in range(n):
              if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                  dfs(neighbor)
      for city in range(n):
          if not visited[city]:
              numProvinces += 1
              dfs(city)
      return numProvinces
