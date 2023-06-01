class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dp(state):
          if  state[0] >= len(triangle) or len(triangle[state[0]]) <= state[1]:
            return inf

          if state in memo:
            return memo[state]

          val = min(dp((state[0] + 1, state[1])), dp((state[0] + 1, state[1] + 1)))
          if val == inf: val = 0

          memo[state] = triangle[state[0]][state[1]] + val  
          return memo[state]

        return dp((0, 0))
          
