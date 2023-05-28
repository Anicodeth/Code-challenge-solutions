class Solution:
    def romanToInt(self, s: str) -> int:
      roman = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
      }
      num = 0

      I = X = C = 0

      for r in s:
        if r == "I": I += 1
        elif r == "X": X += 1
        elif r == "C": C += 1

        num += roman[r]

        if I > 0 and (r == "V" or r == "X"): 
          num -= I * 2
          I = 0
        elif X > 0 and (r == "L" or r == "C"): 
          num -= X*roman['X']*2
          X = 0
        elif C > 0 and (r == "D" or r == "M"): 
          num -= C*roman['C']*2
          C = 0
      
      return num
