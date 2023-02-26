class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      if s1 == s2: return True
      winsize = len(s1)
      ref = Counter(s1)
      p2=winsize
      for p1 in range(len(s2)-1):
        if ref == Counter(s2[p1:p2]):
          return True
          break
        p2+=1

      return False
        
