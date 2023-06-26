class Solution:
    def findWords(self, words: List[str]) -> List[str]:
      first = set("qwertyuiopQWERTYUIOP")
      second = set("asdfghjklASDFGHJKL")
      third = set("zxcvbnmZXCVBNM")

      keyboard = [first, second, third]
      res = []

      for word in words:
        for keys in keyboard:
          for i, c in enumerate(word):
            if c not in keys:
              break
            if i == len(word) - 1:
              res.append(word)

      return res
