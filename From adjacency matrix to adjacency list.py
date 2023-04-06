mat = []
n = int(input())
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)


for row in mat:
    res = []
    for entity in range(len(row)):
        if row[entity] == 1:
            res.append(entity+1)


    print(len(res),"",end = '')
    for c in res:
        print(str(c),"", end='')
    print()
