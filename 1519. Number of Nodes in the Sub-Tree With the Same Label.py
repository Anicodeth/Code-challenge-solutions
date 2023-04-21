class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        freq_tables = [defaultdict(int) for _ in range(n)]
        
        def dfs(node, parent):
            freq_tables[node][labels[node]] = 1
            for child in adj_list[node]:
                if child != parent:
                    child_freq_table = dfs(child, node)
                    for k, v in child_freq_table.items():
                        freq_tables[node][k] += v
            return freq_tables[node]
        
        dfs(0, None)
        
        result = [freq_tables[i][labels[i]] for i in range(n)]
        
        return result


