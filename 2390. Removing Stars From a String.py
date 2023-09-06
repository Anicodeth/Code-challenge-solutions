class Solution:
    def removeStars(self, s: str) -> str:
      stalk = []
      
      for c in s:
        if stalk and c == "*" and stalk[-1] != "*":
          stalk.pop()
        elif c != "*" and stalk and stalk[-1] == "*":
          stalk.pop()
          continue
        else:
          stalk.append(c)


      return "".join(stalk)

        
          
