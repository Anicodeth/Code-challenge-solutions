class Solution:
    def numDecodings(self, s: str) -> int:
        if  s[0] == "0":
            return 0
        tab = []
        test = False
        memo = [0 for _ in range(len(s))]
        def dp(i):
            if memo[i] > 0:
                return memo[i]
            if i <= 0:
                memo[0] = 1
                return 1
            if s[i] == "0":
                if int(s[i-1:i+1]) > 26 or s[i-1] == "0":
                    test = True
                    return 0
                else:
                    memo[i] = dp(i-2)
            elif int(s[i-1:i+1]) <= 26 and s[i-1] != "0":
                x = dp(i-1) + dp(i-2)
                memo[i] = x 
            else:
                memo[i] = dp(i-1)
            return memo[i]
        res = dp(len(s)-1)
        
        if test: return 0
        else: return memo[len(s)-1]
