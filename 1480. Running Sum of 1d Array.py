class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
      run = [nums[0]]

      for i in range(1,len(nums)):
        run.append(nums[i]+run[i-1])
      
      return run

      
