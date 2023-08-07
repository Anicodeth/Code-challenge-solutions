class Solution:
    def firstUniqChar(self, s: str) -> int:
      table = Counter(s)

      for i, c in enumerate(s):
        if table[c] == 1:
          return i

      return -1

