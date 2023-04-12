from collections import defaultdict

n = int(input())
mat = []
graph = defaultdict(list)

for _ in range(n):
    mat.append(list(map(int, input().split())))

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] == 1:
            graph[i+1].append(j+1)

bonds = set()
visited = set()
def dfs(city):
    if city in visited:
        return

    visited.add(city)
    for ne in graph[city]:
        if (ne,city) not in bonds:
            bonds.add((ne,city))
            bonds.add((city,ne))
        


for i in range(1, n+1):
    if i in graph:
        dfs(i)
    


print(len(bonds)//2)
