class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        cats = set(["electronics", "grocery", "pharmacy", "restaurant"])
        res = []

        for i in range(n):
            if not code[i] or any(not (c.isdigit() or c.isalpha() or c == "_") for c in code[i]) or not isActive[i] or not (businessLine[i] in cats):
                continue

            res.append((code[i], businessLine[i]))

        res.sort(key = lambda x: (x[1], x[0]))
        res = [ val[0] for val in res]
        return res
        
