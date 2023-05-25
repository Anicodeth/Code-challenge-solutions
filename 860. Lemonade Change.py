class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
      fives = 0
      tens = 0

      for paid in bills:
        if paid == 5:
          fives += 1

        elif paid == 10:
          if fives > 0:
            fives -= 1
          else:
            return False
          tens += 1

        elif paid == 20:
          while paid > 5:
            if paid > 10 and tens > 0:
              paid -= 10
              tens -= 1
            elif fives > 0:
              paid -= 5
              fives -= 1
            else:
              return False

      return True


            


