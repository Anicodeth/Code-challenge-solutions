class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        if y > x:
            return y - x

        visited = set()

        que = deque([(x, 0)])
        visited.add(x)

        while que:
            node, steps = que.popleft()
            visited.add(node)
            possible = []
            if node == y:
                return steps

            if node % 11 == 0:
                possible.append(node // 11)
            if node % 5 == 0:
                possible.append(node // 5)

            possible.append(node - 1)
            possible.append(node + 1)

            for state in possible:
                if state not in visited:
                    que.append((state, steps + 1))
