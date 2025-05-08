class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops: return m * n

        m1 = m
        m2 = n

        for a, b in ops:
            m1 = min(a, m1)
            m2 = min(b, m2)

        return m1 * m2
