class Solution:
    def minSteps(self, n: int) -> int: 
      steps = 0
      prime = 2

      while n > 1:
        while n % prime == 0 :
          steps += prime
          n /= prime
        prime += 1

      return steps

        
