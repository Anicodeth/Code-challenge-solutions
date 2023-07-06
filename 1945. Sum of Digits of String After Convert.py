class Solution:
    def getLucky(self, s: str, k: int) -> int:
        #97 122
        sumi = ""
        for c in s:
          sumi += str(ord(c) - 96)

        for _ in range(k):
          summ = 0
          for c in sumi:
            summ += int(c)

          sumi = str(summ)


        return int(sumi)
