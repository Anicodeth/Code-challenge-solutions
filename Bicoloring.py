from collections import defaultdict

def dfs(node, color):
        if visited[node-1] != color and visited[node-1] != 0 :
          global bi 
          bi = False
          return
        if visited[node-1] != 0:
          return
        visited[node-1] = color
        for i in graph[node]:
          dfs(i, 1  if color == 2 else 2)
    
while True:
    edges = []
    bi = True
    graph = defaultdict(list)
    n = int(input())

    visited = [0] * n

    if n == 0:
        break

    e = int(input())
    for _ in range(e):
        edges.append(list(map(int, input().split())))

    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    dfs(1,1)

    if  bi:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")


    


