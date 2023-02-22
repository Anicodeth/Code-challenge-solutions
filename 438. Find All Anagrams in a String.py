from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagramlist=[]
        subdict = Counter(p)
        k=len(p)
        for i in range(len(s) - k+1):
          if Counter(s[i:i+k]) == subdict:
            anagramlist.append(i)
        return anagramlist
	
