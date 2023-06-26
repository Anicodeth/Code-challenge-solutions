class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
      answer = prefix = 0
      for i in range(len(nums)):
        prefix += nums[i]
        answer = max(answer, math.ceil(prefix / (i + 1)))
      return answer
        
