class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
      batteries.sort()
      on = batteries[-n:]
      backup = sum(batteries[:-n])
      maxi = 0

      for i in range(len(on) - 1):
         if backup // (i + 1) < on[i + 1] - on[i]:
                return on[i] + backup // (i + 1)
         backup -= (on[i + 1] - on[i]) * (i + 1)

      return on[-1] + backup // n



