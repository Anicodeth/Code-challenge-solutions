class Solution:
    def countPoints(self, rings: str) -> int:
      dic = defaultdict(set)

      for i in range(0, len(rings),2):
        dic[rings[i+1]].add(rings[i])
      count = 0
      for values in dic.values():
        if len(values) == 3:
          count += 1

      return count
