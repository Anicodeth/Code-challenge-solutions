class Solution:
    def modifyString(self, s: str) -> str:
      s = [ c for c in s]
      off = 97

      for i, c in enumerate(s):
        if c != '?':
          continue
        left = ord(s[i-1]) if i != 0 else 0
        right = ord(s[i+1]) if i != len(s)-1 else 0

        invalid = {left, right}

        for j in range(off, off + 5):
          if j not in invalid:
            s[i] = chr(j)
            break
        
      return "".join(s)
