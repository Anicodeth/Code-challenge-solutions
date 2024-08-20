class Solution:

    
    def clumsy(self, n: int) -> int:
        cal = []
        op = ['*', '//', '+', '-']
        i = 0
        
        while n:
            cal.append(str(n))
            n -= 1
            s = op[i % 4]
            cal.append(s)
            i += 1
        cal.pop()

        return eval("".join(cal))
            
