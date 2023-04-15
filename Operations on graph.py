from collections import defaultdict
n = int(input())
op = int(input())

graph = defaultdict(list)

for _ in range(op):
    operation = list(map(int, input().split()))
    type = operation[0]
    if type == 1:
        graph[operation[1]].append(operation[2])
        graph[operation[2]].append(operation[1])
    else:
        for i in graph[operation[1]]:
            print(i, end = " ")
        print()
