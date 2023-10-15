class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        points = []
        res = []
        for i, s in enumerate(score):
            points.append((s[k], i))

        points.sort(key = lambda x : -x[0])

        for p, i in points:
            res.append(score[i])

        return res

