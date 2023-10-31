class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        i = 0
        n = len(s)

        while i < n:
            curr = ''
            if s[i].isdigit():
                
                while i < n and s[i].isdigit():
                    curr += s[i]
                    i += 1
                stack.append(('[', int(curr)))
            elif s[i].isalpha():
                
                while i < n and s[i].isalpha():
                    curr += s[i]
                    i += 1
                stack.append(('*', curr))
                i -= 1
            else:
                
                while stack[-1][0] != '[':
                    _, val = stack.pop()
                    curr = val + curr
                _, m = stack.pop()
                stack.append(('*', curr * m))

            i += 1

        pruned = [ num[1] for num in stack]


        return "".join(pruned)

        
