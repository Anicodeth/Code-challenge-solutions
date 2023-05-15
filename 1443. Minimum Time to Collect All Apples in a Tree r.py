class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:                          
        visited, graph = set(), defaultdict(list)

        for a,b in edges: 
            graph[a].append((b))
            graph[b].append((a))
           
        def dfs(node):
            visited.add(node)    
  
            ans = sum(dfs(n) for n in graph[node] if n not in visited) 
 
            if not ans and not hasApple[node]: return 0

            return ans+2           

        return max (0,dfs(0)-2)
