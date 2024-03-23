class Solution:
    def myPow(self, x: float, n: int) -> float:

        memo = {}
        def powerFun(x, n):
            if n == 1:
                return x
            elif n == -1:
                return 1/x
            elif n == 0:
                return 1
            elif n in memo:
                return memo[n]

            right = n // 2
            left = n - right

            memo[n] = powerFun(x, right) * powerFun(x, left)

            return memo[n]

        return powerFun(x, n)

