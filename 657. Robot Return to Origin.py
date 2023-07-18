class Solution:
    def judgeCircle(self, moves: str) -> bool:
      movesDic  = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
      }
      start = [0, 0]

      for c in moves:
        start[0] += movesDic[c][0]
        start[1] += movesDic[c][1]

      return not start[0] and not start[1]
