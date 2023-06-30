class Solution:
    def getSum(self, a: int, b: int) -> int:
      
      while b!=0:
        sumi = (a ^ b) & 0xFFFFFFFF
        carry = ((a&b) << 1) & 0xFFFFFFFF

        a = sumi
        b = carry

      max_int = 0x7FFFFFFF
      return a if a < max_int else ~(a ^ 0xFFFFFFFF)
