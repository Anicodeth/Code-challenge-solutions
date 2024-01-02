import heapq
stations =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 9

distances = []

for i in range(len(stations) - 1):
    distances.append(-(stations[i + 1] - stations[i]))


heapq.heapify(distances)

for _ in range(k):
    maxi = heapq.heappop(distances)
    heapq.heappush(distances, maxi / 2)

print(-heapq.heappop(distances))
