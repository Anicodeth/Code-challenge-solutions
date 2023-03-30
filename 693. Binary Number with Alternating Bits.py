class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
      bits = len(bin(n)) - 2

      for k in range(bits - 1):
        p1 = n & (1 << k)
        p2 = n & (1 << k + 1)
        if ( p1 == p2 == 0 ) or (p1!=0 and p2!=0):
          return False


      return True
