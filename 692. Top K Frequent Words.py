class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      freq = Counter(words)

      heap = []

      for word, f in freq.items():
        heapq.heappush(heap, (-f, word))

      res = []

      for _ in range(k):
        res.append(heapq.heappop(heap)[1])

      return res
