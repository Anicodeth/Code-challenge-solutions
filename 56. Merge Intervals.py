class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      
      intervals.sort(key = lambda x: (x[0]))

      i = 0

      while (i < len(intervals) - 1):
        x, y = intervals[i]
        x1 , y1 = intervals[i + 1]

        if x1 >= x and x1 <= y:
          start = x
          end = max(y, y1)
          intervals[i] = [start, end]
          del intervals[i + 1]
        else:
          i += 1

      return intervals
