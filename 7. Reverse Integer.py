class Solution:
    def reverse(self, x: int) -> int:
      sign = x // abs(x) if abs(x) != 0 else 1
      x *= sign

      res = []

      while x != 0:
        rem = x % 10
        res.append(str(rem))
        x = x // 10
      if not res: res.append('0')
      ans  = sign * int("".join(res))
      if ans > (2**31) - 1 or ans < (-2**31): return 0
      return  ans
