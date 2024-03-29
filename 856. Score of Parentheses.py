class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
            else:

                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                    continue

                sumi = 0
                while stack[-1] != '(':
                    sumi += stack.pop()

                stack.pop()
                stack.append(sumi * 2)

        return sum(stack)



        
