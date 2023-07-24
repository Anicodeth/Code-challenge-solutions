class Solution:
    def longestPalindrome(self, s: str) -> int:
      s = Counter(s)

      unused = 0
      pal = 0

      for c in s:
        if s[c] == 1:
          unused += 1
        elif s[c] % 2 == 0:
          pal += s[c]
        else:
          unused += 1
          pal += (s[c] - 1)

      if (pal % 2 == 1) or (pal % 2 == 0 and unused == 0):
        return pal
      else:
        return pal + 1
