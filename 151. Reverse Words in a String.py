class Solution:
    def reverseWords(self, s: str) -> str:
      words = s.split(" ")

      ans = []

      for i in range(len(words) -1 , -1, -1):
        if words[i] == '': continue
        ans.append(words[i].strip(' '))

      return " ".join(ans)
