class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def convert(time):
            hr, min = time.split(":")
            total = int(min) + (int(hr) * 60)
            return total

        times = []
        totalMinutes = 1440

        for time in timePoints:
            times.append(convert(time))

        times.sort()
        smallest = inf
        n = len(times)
        for i in range(n - 1):
            smallest = min(smallest, times[i + 1] - times[i])
        
        gap = (totalMinutes - times[-1]) + times[0]

        return min(gap, smallest)

