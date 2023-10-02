class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if stack and stack[-1][0] == c:
                stack.append((c, stack[-1][1] + 1))
            else:
                stack.append((c, 1))
            
            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()

        val = [c for c,v in stack]
        return "".join(val)


        
