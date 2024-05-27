class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lets = []
        for c in s:
            if c.isalpha():
                lets.append(c)

        res = []
        for c in s:
            if c.isalpha():
                res.append(lets.pop())
            else:
                res.append(c)

        return "".join(res)
        
