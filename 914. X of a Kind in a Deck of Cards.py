class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
      dec = {}
      if len(deck) == 0:
        return False

      for card in deck:
        if card in deck:
          dec[card] = dec.get(card, 0) + 1
        else:
          dec[card] = 0
    
      values = list(dec.values())
      g = gcd(values[0], values[0])
      for i in range(1,len(values)):
        g = gcd(g, values[i])

      return g > 1
