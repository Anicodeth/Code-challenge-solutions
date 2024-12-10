class Solution:
    def maximumLength(self, s: str) -> int:
        counter = {}
        n = len(s)

        for i in range(n):
            for j in range(i + 1, n + 1):
                sliced = s[i:j]
                counter[sliced] = counter.get(sliced, 0) + 1

        items = list(counter.items())
        maxi = -1
        for item in items:
            if item[1] >= 3 and len(set([ c for c in item[0]])) == 1:
                maxi = max(maxi, len(item[0]))

        return maxi
