class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

      def bfs(node):
        que = deque([node])
        visited = set([node])

        while que:
          node = que.popleft()

          for child in rooms[node]:
            if child not in visited:
              visited.add(child)
              que.append(child)

        return len(visited) == len(rooms)
      if bfs(0):
        return True

      return False


        
