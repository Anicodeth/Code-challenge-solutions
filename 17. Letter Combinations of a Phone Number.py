class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      if digits == "": return []
      dic = {
        "2":['a','b','c'],
        "3":['d','e','f'],
        "4":['g','h','i'],
        "5":['j','k','l'],
        "6":['m','n','o'],
        "7":['p','q','r','s'],
        "8":['t','u','v'],
        "9":['w','x','y','z'],
      }
      n = len(digits)
      res = []

      def dfs(curr, start):
        nonlocal n
        if start == n:
          res.append("".join(curr))
          return
          

        for c in dic[digits[start]]:
          dfs(curr + [c], start + 1)

      
      dfs([], 0)

      return res

      
