class Solution:
    def heightChecker(self, heights: List[int]) -> int:
      expected = heights[:]
      heights.sort()

      count = 0

      for i in range(len(expected)):
        if heights[i] != expected[i]:
          count+=1

      return count
