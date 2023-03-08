class Solution:
    def __init__(self):
      self.dic = defaultdict(list)
    def nth(self, k, s):
      if k == 0:
        return s
      else:
        ns =''
        for i in s:
          if i == '0': ns+='1'
          else: ns+='0'

        return  self.nth(k-1, (s + '1' + ns[::-1]))
    def findKthBit(self, n: int, k: int) -> str:
      return self.nth(n-1, '0')[k-1]
