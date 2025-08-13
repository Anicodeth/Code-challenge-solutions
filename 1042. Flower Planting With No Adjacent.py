class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for x, y in paths:
            adj[x-1].append(y-1)
            adj[y-1].append(x-1)

        res = [0] * n

        for i in range(n):
            used = {res[nei] for nei in adj[i] if res[nei] != 0}
            
            for flower in range(1, 5):
                if flower not in used:
                    res[i] = flower
                    break

        return res
