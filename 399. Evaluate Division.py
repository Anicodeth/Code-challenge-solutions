class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
            graph = defaultdict(list)

            for i, eq in enumerate(equations):
                graph[eq[0]].append((eq[1], values[i]))
                graph[eq[1]].append((eq[0], 1 / values[i]))

            def dfs(start, end, curr, visited):
                if start == end:
                    return curr

                visited.add(start)
                result = -1.0

                for neighbor, value in graph[start]:
                    if neighbor not in visited:
                        result = dfs(neighbor, end, curr * value, visited)
                        if result != -1.0:
                            break

                visited.remove(start)
                return result

            res = []

            for a, b in queries:
                if a not in graph or b not in graph:
                    res.append(-1.0)
                else:
                    visited = set()
                    ans = dfs(a, b, 1.0, visited)
                    res.append(ans if ans != -1.0 else -1.0)

            return res
