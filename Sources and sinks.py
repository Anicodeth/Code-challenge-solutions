mat = []
n = int(input())

for _ in range(n):
    mat.append(list(map(int, input().split())))

sinks = list(range(1, n + 1))
sources = list(range(1, n + 1))


for i, row in enumerate(mat):
    for e in range(len(row)):
        if row[e] == 1:
            if i+1 in sinks:
                sinks.remove(i+1)

            if e+1 in sources:
                sources.remove(e+1)

print(len(sources),"",end = '')
for c in sources:
    print(str(c),"", end='')
print()


print(len(sinks),"",end = '')
for c in sinks:
    print(str(c),"", end='')
print()

