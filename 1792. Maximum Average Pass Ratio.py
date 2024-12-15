class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        ratio = [[ -(((p + 1) / (t + 1)) - (p / t)) ,p, t] for p, t in classes ]
        heapq.heapify(ratio)

        for _ in range(extraStudents):
            largestChange, p, t = heapq.heappop(ratio)
            heapq.heappush(ratio, [-(((p + 2) / (t + 2)) - (p + 1) / (t + 1)), p + 1, t + 1])

        sumi = 0
        for r, p, t in ratio:
            sumi += (p / t)

        return sumi / len(ratio)
        
