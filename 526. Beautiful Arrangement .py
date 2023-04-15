class Solution:
    def countArrangement(self, n: int) -> int:
      self.count = 0
      arr = list(range(1,n+1))

      def backtrack(start):
          if start  == len(arr) and (arr[start - 1] % start == 0 or start % arr[start - 1] == 0):
            self.count += 1
            return

          for i in range(start, len(arr) + 1):

            arr[i - 1], arr[start - 1] = arr[start - 1], arr[i - 1]
            if arr[start - 1] % start == 0 or start % arr[start - 1] == 0:
              backtrack(start + 1)
            arr[i - 1], arr[start - 1] = arr[start - 1], arr[i - 1]

      backtrack(1)

      return self.count
