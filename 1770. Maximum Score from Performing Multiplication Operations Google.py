class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
         m = len(multipliers) 
         @cache
         def dp(left, right, index):

            if index == m:
                return 0

            leftScore = (nums[left] * multipliers[index]) + dp(left + 1, right, index + 1)
            rightScore = (nums[right] * multipliers[index]) + dp(left, right - 1, index + 1)

            return max(leftScore, rightScore)
         return dp(0, len(nums) - 1, 0)

 

            



        
