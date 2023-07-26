class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
      first = []
      second = []

      for c in s:
        if c == '#' and first: first.pop()
        else:
          if c != '#':
           first.append(c)

      for c1 in t:
        if c1 == '#' and second: 
          second.pop()
        else: 
          if c1 != '#':
            second.append(c1)

      return "".join(first) == "".join(second)
