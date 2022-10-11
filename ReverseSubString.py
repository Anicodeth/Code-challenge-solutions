class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i!=')':
                stack.append(i)
            else:
                reverse=[]
                while stack[-1]!='(':
                    reverse.append(stack.pop())
                stack.pop()
                stack.extend(reverse)
        
        return "".join(stack)
