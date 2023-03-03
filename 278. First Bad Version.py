# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
      left = 0
      right = n 
      last = 0
      trace = False
      while left <= right:
        mid = (left+right)//2
        if isBadVersion(mid):
          last = mid
          right = mid - 1
        else:
          left = mid +1 

      while isBadVersion(last):
          last-=1
      return last+1
