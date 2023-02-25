class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

      l,r =0,0
      mini=+inf
      window = sum(nums[l:r+1]) 
      
      while (r < len(nums) and l <= r):
        
        if window >= target:
          window -= nums[l] 
          if mini > r-l+1:
            mini = r-l+1
          l+=1
        else:
          r+=1
          if r < len(nums):
            window += nums[r]
          

      return mini if mini!=+inf else 0
        


      
