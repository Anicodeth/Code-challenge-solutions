class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

      graph = [[] for _ in range(n)]

      for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

      print(graph)

      maxi = 0

      for i in range(len(graph) - 1):
        for j in range(i + 1, len(graph)):
          local = len(graph[i]) + len(graph[j])
          if i in graph[j]:
            local-=1

          maxi = max(local, maxi)

      return maxi
          
