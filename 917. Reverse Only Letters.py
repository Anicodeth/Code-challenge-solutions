class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        temp = []
        lets = []
        for c in s:
            if c.isalpha():
                temp += [None]
                lets.append(c)
            else:
                temp += [c]
        res = ""
        for c in temp:
            if not c:
                res += lets.pop()
            else:
                res += c

        return res
        
