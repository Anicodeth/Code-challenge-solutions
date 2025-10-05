class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n = len(heights)
        m = len(heights[0])
        results = []
        def traverse(i, j, visited, state, last):
            nonlocal n, m
            if state == [True, True]:
                return

            if i < 0 or j < 0:
                state[0] = True
                return

            if i == n or j == m:
                state[1] = True
                return

            if (i, j) in visited or last < heights[i][j]:
                return

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited.add((i, j))
            for a, b in directions:
                traverse(i + a, j + b, visited, state, heights[i][j])
            visited.remove((i, j))
            return state


        for i in range(n):
            for j in range(m):
                visited = set()
                final = traverse(i, j, visited, [False, False], heights[i][j])
                if final == [True, True]:
                    results.append([i, j])

        return results


        
