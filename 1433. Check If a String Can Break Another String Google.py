class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        s1, s2 = [*s1], [*s2]
        s1.sort()
        s2.sort()
        res1, res2 = True, True

        for i in range(len(s1)):
            if s1[i] < s2[i]:
                res1 = False
                break

        for i in range(len(s1)):
            if s2[i] < s1[i]:
                res2 = False
                break

        return res2 or res1        
        
