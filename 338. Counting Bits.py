class Solution:
    def checkbit(self, num, k):
      return num & (1<<k) != 0 
 
    def countBits(self, n: int) -> List[int]:
      ones = []
      for i in range(n+1):
        count = 0
        for j in range(64):
          if self.checkbit(i,j):
            count+=1

        ones.append(count)

      return ones


      
