class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      pars = []
      def valid(values):
        stack = []
        for c in values:
          
          if c == '(':
            stack.append('(')
          elif c == ')' and stack:
            stack.pop()
          elif c == ')' and not stack:
            return False

        return False if stack else True
          
      def generate(curr):
        
        nonlocal pars
        if len(curr) == n * 2:
          
          if valid(curr):
            pars.append("".join(curr))

          return

        curr.append('(')
        generate(curr)
        curr.pop()
        curr.append(')')
        generate(curr)
        curr.pop()

      generate([])

      return pars


        
