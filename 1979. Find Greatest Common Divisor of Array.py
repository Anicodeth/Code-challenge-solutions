class Solution:
    def findGCD(self, nums: List[int]) -> int:
      maxi = max(nums)
      mini = min(nums)

      gcd = 1

      for i in range(2, mini + 1):
        if maxi % i == 0 and mini % i == 0:
          gcd = i

      return gcd
