class Solution:
    def candy(self, ratings: List[int]) -> int:
      n = len(ratings)
      if n == 1: return  1 

      left, right = [1] * n, [1] * n

      for i in range(1, n):
        if ratings[i - 1] < ratings[i]:
          left[i] = left[i - 1] + 1

      for i in range(n - 2, -1, -1):
        if ratings[i + 1] < ratings[i]:
          right[i] = right[i + 1] + 1
      res = 0
      for i in range(n):
        res += max(left[i], right[i])

      return res

      

