class Solution:
    def frequencySort(self, s: str) -> str:
      freq = Counter(s)
      items = freq.items()
      order = sorted(items, key = lambda x: x[1], reverse = True)
      res = []
      
      for item in order:
        res.append(item[0] * item[1])
      
      return "".join(res)
