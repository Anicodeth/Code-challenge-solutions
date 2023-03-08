class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack, cur = [], 0
        for i in s:
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur
