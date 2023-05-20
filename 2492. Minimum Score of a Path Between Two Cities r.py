
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
          parent = list(range(n))
          
          def find(p): 
              if p != parent[p]: parent[p] = find(parent[p])
              return parent[p]
          
          tab = defaultdict(lambda: inf)
          for u, v, dist in roads: 
              ms = find(u-1)
              mh = find(v-1)
              parent[ms] = mh
              tab[ms] = tab[mh] = min(tab[ms], tab[mh], dist)
          
          return tab[find(0)] if find(0) == find(n-1) else -1
