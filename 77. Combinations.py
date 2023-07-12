class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
      comb = []
      def backtrack(index, curr):
        if len(curr) == k:
          comb.append(curr)

        for i in range(index + 1, n + 1):
          backtrack(i, curr + [i])

      for j in range(1, n + 1):
        backtrack(j, [j])

      return comb

        
