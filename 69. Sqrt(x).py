class Solution:
    def mySqrt(self, x: int) -> int:
      if x==1: return 1
      start = 0
      end = x
      m=0
      
      while start <= end:
        m = (start+end)//2
        if m*m <= x:
          start =m + 1
        else:
          end = m -1

      return end
