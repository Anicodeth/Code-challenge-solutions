class Solution:
    def countSeniors(self, details: List[str]) -> int:
      count = 0

      for num in details:
        age = int(num[11] + num[12])
        if age > 60 :
          count += 1

      return count
