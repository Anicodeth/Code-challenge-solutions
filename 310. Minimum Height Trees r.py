class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

      if n == 1:
          return [0]  
      
      adj = defaultdict(set)
      for u, v in edges:
          adj[u].add(v)
          adj[v].add(u)
      
      leaves = deque([i for i in range(n) if len(adj[i]) == 1])

      while n > 2:
          num_leaves = len(leaves)
          n -= num_leaves
          
          for _ in range(num_leaves):
              leaf = leaves.popleft()
              for neighbor in adj[leaf]:
                  adj[neighbor].remove(leaf)
                  if len(adj[neighbor]) == 1:
                      leaves.append(neighbor)
      
      return list(leaves)
