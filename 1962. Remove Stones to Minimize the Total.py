class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
      
      for i in range(len(piles)):
        piles[i] = -piles[i]

      heapq.heapify(piles)

      for _ in range(k):
        stones = heapq.heappop(piles)

        stones //= 2
        heapq.heappush(piles, stones)

      return -sum(piles)
        
