class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      mono = [] 
      maxi = 0

      for i in range(len(prices) - 1, -1, -1):
          if not mono:
            mono.append(prices[i])
          elif mono[-1] > prices[i]:
            local = mono[-1] - prices[i]
            if local > maxi:
              maxi = local
          else:
            mono.append(prices[i])

      
      return maxi

        
