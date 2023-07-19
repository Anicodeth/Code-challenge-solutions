class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
      intervals.sort(key = lambda x : x[1])

      k = -inf
      res = 0 

      for x, y in intervals:
        if x >= k:
          k = y
        else:
          res += 1

      return res 
