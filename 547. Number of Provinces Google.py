class UnionFind:
    def __init__(self):
        self.roots = {}

    def find(self, x):
        if x in self.roots:
            return self.roots[x]
        else:
            self.roots[x] = x
            return self.roots[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for node in self.roots:
                if self.roots[node] == rootY:
                    self.roots[node] = rootX


    def isConnected(self, x, y):
        return self.roots[x] == self.roots[y]

    def countComp(self):
        return len(set(self.roots.values()))



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #Build Graph
        n = len(isConnected)

        disjointSet = UnionFind()

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    disjointSet.union(i + 1, j + 1)

        return disjointSet.countComp()

