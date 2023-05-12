class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
      graph = defaultdict(list)

      for edge in adjacentPairs:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

      self.res = []

      def dfs(node):
        if node in visited:
          return

        visited.add(node)
        self.res.append(node)
        for child in graph[node]:
          dfs(child)

      visited = set()
      for node in graph:
        if len(graph[node]) == 1:
          dfs(node)
          break

      return self.res
