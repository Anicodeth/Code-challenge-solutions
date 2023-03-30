class Solution:
    def findComplement(self, num: int) -> int:
      shift = 1
      for k in range(len(bin(num))-2):
        num = num ^ shift
        shift = shift<<1

      return num
        
