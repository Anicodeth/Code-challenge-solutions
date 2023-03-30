class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
      sig = len(bin(max(x, y))) - 2
      num = x ^ y
      count =  0
      for k in range(sig):
        if num & (1<<k):
          count += 1

      return count
        
        



