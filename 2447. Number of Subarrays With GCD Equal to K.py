class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
      n = len(nums)
      count = 0

      for i in range(n):
        curr = nums[i]
        for j in range(i,n):
          curr = gcd(curr, nums[j])

          if curr == k:
            count += 1
          elif curr < k:
            break

      return count





          
