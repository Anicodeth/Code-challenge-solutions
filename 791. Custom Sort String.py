class Solution:
    def customSortString(self, order: str, s: str) -> str:
        table = Counter(s)
        res = []
        added = set()

        for c in order:
            if c in table:
                res.append(c * table[c])
                added.add(c)

        for c in table:
            if c not in added:
                res.append(c * table[c])


        return "".join(res)
        
