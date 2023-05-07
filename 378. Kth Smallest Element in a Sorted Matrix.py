class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

      heap = []

      n = len(matrix)
      
      for i in range(n):
        for j in range(n):
          heapq.heappush(heap,matrix[i][j])

      for _ in range(k - 1):
        heapq.heappop(heap)

      return heapq.heappop(heap)
