class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      num = str(int("".join(list(map(str, digits)))) + 1)
      res = []

      for c in num:
        res.append(int(c))

      return res
