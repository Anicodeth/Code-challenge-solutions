class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
      satisfaction.sort()
      memo = {}
      def dp(index, like):

        if index == len(satisfaction):
          return 0

        if (index, like) in memo:
          return memo[(index, like)]
        
        make = dp( index + 1, like + 1) + ((like + 1) * satisfaction[index])
        skip = dp( index + 1, like)

        memo[(index, like)] = max(make, skip)

        return memo[(index, like)]


      return dp(0,0)
