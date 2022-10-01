class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.upper()
        s2=""
        for ch in s:
            if (ord(ch)>=65 and ord(ch)<=90) or ((ord(ch)>=48 and ord(ch)<=57)):
                s2+=ch
        l,r=0,len(s2)-1
        while r!=-1:
            if s2[l]==s2[r]:
                r-=1
                l+=1
            else:
                return False
        return True
