class Solution:
    def splitString(self, s: str) -> bool:
      def splitter(index, div, prev_value):
            if index == size:
                return div >= 2
            
            for i in range(index, size):
                num = int(s[index : i + 1])

                if prev_value == maxi or num == prev_value - 1:

                    if splitter(i + 1, div + 1, num):
                        return True
            return False
      maxi = math.inf
      size = len(s)

      return splitter(0, 0, maxi)
