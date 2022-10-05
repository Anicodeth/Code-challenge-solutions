class Solution:
    def isValid(self, s: str) -> bool:
        stalk=[]
        close={'}':'{',']':'[',')':'('}
        for c in s:
            if c in close:
                if stalk and stalk[-1]==close[c]:
                    stalk.pop()
                else:
                    return False
            else:
                stalk.append(c)

        return True if not stalk else False
