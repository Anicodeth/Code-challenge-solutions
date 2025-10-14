class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []

        for c in s:
            if not stack:
                stack.append(c)
            elif stack[-1] in dic and c == dic[stack[-1]]:
                stack.pop()
            else:
                stack.append(c)

        if stack: return False

        return True 
