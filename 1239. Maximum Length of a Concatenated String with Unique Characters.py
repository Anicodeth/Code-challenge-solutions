class Solution:
    def __init__(self):
      self.maxi = 0 


    def maxLength(self, arr: List[str]) -> int:
      def backtrack(li, start):
        con = Counter(li)
        if len(con) != len(li):
          return
        if len(arr) <= start:
          return
     
        self.maxi = max(self.maxi, len(con))
 
        res = li + arr[start]
        for j in range(len(arr)):
          backtrack(res, start + j)

      for i in range(len(arr)):
        backtrack("",i)


      return self.maxi
