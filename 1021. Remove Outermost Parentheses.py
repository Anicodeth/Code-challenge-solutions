class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0

        stack = []

        for c in s:
            if c =='(' and opened > 0:
                stack.append(c)

            elif c == ')' and opened > 1:
                stack.append(c)

            if c == '(': opened += 1
            else: opened -= 1 

        return "".join(stack)

            
        
