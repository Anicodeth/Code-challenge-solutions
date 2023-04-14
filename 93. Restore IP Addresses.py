class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
      
      self.validips = set()
      
      def checksegment(segment):
        if int(segment) >= 0 and int(segment) <=255 and len(segment) == len(str(int(segment))):
          return True
        return False

      def parseip(curr,s, seg):
        if seg > 4 and s == '':
          self.validips.add(curr)
          return

        if seg > 4 or s == "":
          return
        
        if seg != 1:
          curr+= "."

        for i in range(3):
          if checksegment(s[:i+1]):
            parseip(curr + s[:i+1] , s[i+1:], seg + 1)

      parseip("", s , 1)
      return list(self.validips)
