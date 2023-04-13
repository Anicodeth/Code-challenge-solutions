class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
      seq = []
      def backtrack(li, start):
        if len(nums) <= start or (len(li) != 0 and li[-1] > nums[start]):
          return
     
        res = li + [nums[start]]
 
        if len(res) > 1 and res not in seq:
          seq.append(res)

        for j in range(1, len(nums)):
          backtrack(res, start + j)

      for i in range(len(nums)):
        backtrack([],i)


      return seq

        
      
