class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:          
        p1=0
        p2=p1+1
        gmax=0
        hasht=set()

        while p2<len(s):
          hasht.add(s[p1])
          localmax=len(hasht)
          if s[p2] in hasht:
            p1=p2
            p2+=1
            if localmax > gmax:
              gmax=localmax
          else:
              hasht.add(s[p2])
        return gmax

