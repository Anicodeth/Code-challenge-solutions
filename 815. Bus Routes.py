class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

      if source == target:
        return 0

      routes = list(map(set, routes))

      graph = defaultdict(set)

      for i, stops in enumerate(routes):
        for j in range(i + 1, len(routes)):

          stops2 = routes[j]

          if any(stop in stops2 for stop in stops):
            graph[i].add(j)
            graph[j].add(i)

      visited, targetset = set(), set()

      for i,r in enumerate(routes):
        if source in r:
          visited.add(i)
        if target in r:
          targetset.add(i)

      que = deque([(node, 1) for node in visited])

      while que:
        node, depth = que.popleft()

        if node in targetset:
          return depth

        for child in graph[node]:
          if child not in visited:

            que.append((child, depth + 1))
            visited.add(node)

      return -1


