class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = {}

        for i in range(len(parent)):
            if parent[i] in graph:
                graph[parent[i]].append(i)
            else:
                graph[parent[i]] = [i]
                
        maxi = 1        
        def dfs(node):
            nonlocal maxi
            if node not in graph:
                return 1
            
            largest=0 
            second_largest=0 
            for j in graph[node]:
                curr = dfs(j)
                if s[j]!=s[node]:
                    if curr>largest:
                        second_largest = largest
                        largest = curr
                    elif curr>second_largest:
                        second_largest = curr
                        
            maxi = max(maxi,largest+second_largest+1) 
            return largest+1 
        
        dfs(0)
        return maxi
