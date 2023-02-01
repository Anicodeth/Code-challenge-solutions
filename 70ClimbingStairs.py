class Solution:
    def climbStairs(self, n: int) -> int:
       f,s=1,1
       for _ in range(n-1):
           f,s=s,f+s
       return s
