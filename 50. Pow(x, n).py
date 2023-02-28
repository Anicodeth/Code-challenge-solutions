class Solution:
    def __init__(self):
          self.dicpow = {}
    def myPow(self, x: float, n: int) -> float:
          if(n == 0):
            return 1
          if n in self.dicpow:
            return self.dicpow[n]
          if(abs(n)==1):     
              return x if n>0 else 1/x
          else:
            self.dicpow[n]=self.myPow(x,n//2)*self.myPow(x,(n//2)+n%2)
            return self.dicpow[n]

