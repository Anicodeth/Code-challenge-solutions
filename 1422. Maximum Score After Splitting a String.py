class Solution:
    def maxScore(self, s: str) -> int:
        preZeros = [0]
        n = len(s)

        for i in range(n):
            if s[i] == "0": preZeros.append(preZeros[-1] + 1)
            else: preZeros.append(preZeros[-1])
        curr = 0
        
        for j in range(n - 1, -1, -1):
            if s[j] == "1":  curr += 1

            preZeros[j] += curr

        res = []
        for i in range(n):
            if i == 0:
                continue
            res.append(preZeros[i])

        return max(res) if res else 0
