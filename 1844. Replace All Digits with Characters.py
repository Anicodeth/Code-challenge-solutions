class Solution:
    def replaceDigits(self, s: str) -> str:
        new = []
        n = len(s)

        for i in range(0, n - 1, 2):
            new.append(s[i])
            new.append(chr(ord(s[i]) + int(s[i+1])))    

        if n % 2 == 1: new.append(s[-1])

        return "".join(new)
        
        
