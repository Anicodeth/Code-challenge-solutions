class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
      piles = [-pile for pile in piles]
      heapq.heapify(piles)

      alice = 0
      bob = 0

      while piles:
        alice += -heapq.heappop(piles) if piles else 0
        bob += -heapq.heappop(piles) if piles else 0

      return alice > bob
