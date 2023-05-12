from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
 #Code here
        seen = set()
        def dfs(node, parent):
            seen.add(node)
            
            for child in adj[node]:
                if child not in seen:
                    if dfs(child, node):
                        return True
                        
                elif child != parent:
                    return True
                    
            return False
		  
        for node in range(len(adj)):
            if node not in seen:
                if dfs(node, -1):
                    return 1
                    
        return 0
