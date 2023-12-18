class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
          maxi = [ -num for num in nums ]

          heapq.heapify(nums)
          heapq.heapify(maxi)
          
          a = -heapq.heappop(maxi)
          b = -heapq.heappop(maxi)
          c = heapq.heappop(nums)
          d = heapq.heappop(nums)

          return  (a * b) - (c * d)
