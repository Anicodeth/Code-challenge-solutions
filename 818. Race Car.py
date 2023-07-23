class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 0, 1)])
        visited = set()

        while queue:
            moves, pos, vel = queue.popleft()

            if pos == target:
                return moves

            if (moves, pos, vel) in visited:
                continue

            visited.add((moves, pos, vel))

            queue.append((moves + 1, pos + vel, 2 * vel))
            if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
                queue.append((moves + 1, pos, -vel // abs(vel)))

        return -1



