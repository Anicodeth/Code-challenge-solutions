class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)

        total = 0

        for i in range(n):
            dic = defaultdict(int)
            for j in range(i, n):
                dic[s[j]] += 1

                maxi = max(dic.values())
                mini = min(dic.values())

                total += maxi - mini

        return total

                

