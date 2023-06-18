class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
      ranking = {}
      res = []

      temp = [-num for num in score]
      heapq.heapify(temp)

      n = len(score)

      medals = {
        1: "Gold Medal",
        2: "Silver Medal",
        3: "Bronze Medal"
      }

      for i in range(1,n + 1):
        top = heapq.heappop(temp)
        ranking[-top] = i

      for num in score:
        if ranking[num] in medals:
          res.append(medals[ranking[num]])
          continue
        else:
          res.append(str(ranking[num]))

      return res
        


