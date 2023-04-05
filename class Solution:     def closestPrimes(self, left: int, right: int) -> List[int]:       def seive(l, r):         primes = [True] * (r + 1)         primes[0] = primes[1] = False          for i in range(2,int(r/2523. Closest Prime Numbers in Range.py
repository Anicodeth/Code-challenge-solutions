class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
      def seive(l, r):
        primes = [True] * (r + 1)
        primes[0] = primes[1] = False

        for i in range(2,int(r/2)+1):
          if primes[i]:
            for p in range(i*i, r+1, i):
              primes[p] = False
        pairs = []
        res = [-1,-1]
        global_min = local_min = inf

        for i in range(l, r+1):
           if primes[i]:
             if pairs:
               local_min = i - pairs[-1]
             pairs.append(i)

             if local_min < global_min:
               global_min = local_min
               res = [pairs[-2], i]
        return res

             


      return seive(left, right)
      

        
