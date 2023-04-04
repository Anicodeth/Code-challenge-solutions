class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

      primes = set()
      number = set()

      def getPrimeFactors(num):
        i = 2
        top = ceil(sqrt(num))
        while(i <= top):
          while num % i == 0:
            primes.add(i)
            num = num / i
          i+=1

        if num > 1:
          primes.add(num)
     
      for num in nums:
        if num in number:
          continue
        getPrimeFactors(num)

      return len(primes)
