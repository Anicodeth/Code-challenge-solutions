class Disjoint:
    def __init__(self,n):
        self.rank = [0]*(n+1)
        self.parent = [i for i in range(n+1)]
    
    def findUpar(self,node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUpar(self.parent[node])
        return self.parent[node]

    def byRank(self,u,v):
        ulp_u = self.findUpar(u)
        ulp_v = self.findUpar(v)
        if ulp_u == ulp_v:
            return False
        if self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_u] = ulp_v
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        disjoint = Disjoint(n)
        for x,y in edges:
            if disjoint.byRank(x,y)==False:
                lst = [x,y]
        return lst
