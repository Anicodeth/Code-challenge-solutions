class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=floor(sqrt(c))
        s=0
        while(l<=r):
            s=(l*l)+(r*r)
            if(s>c):
                r-=1
            elif(s<c):
                l+=1
            else:
                return True
        return False
