
from collections import Counter

fin = int(input())
for i in range(fin):
    inp = list(map(int,input().split()))
    n , c = inp[0], inp[1]
    orbits = list(map(int,input().split()))
    data = Counter(orbits)
    cost = 0

    for planet in info:
        if data[planet] >= c:
            cos += c
        else:
            cos += info[planet]

    print(cos)
