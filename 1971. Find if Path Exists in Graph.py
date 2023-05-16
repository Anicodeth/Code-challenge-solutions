class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
      if source == destination:
        return True
      aj = defaultdict(list)
      visited = set()
      for pair in edges:
        aj[pair[0]].append(pair[1])
        aj[pair[1]].append(pair[0])

      def dfs(v):
        if v == destination:
          return True
        visited.add(v)
        for ne in aj[v]:
          if ne not in visited:
            if dfs(ne):
              return True

      if dfs(source):
        return True
      return False


      
