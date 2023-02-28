class Solution:
    def reverseString(self, s: List[str]) -> None:
        if not s:
          return 0
        else:
          last = s.pop(0)
          self.reverseString(s)
          s.append(last)
           
