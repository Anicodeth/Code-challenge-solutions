class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        res = []
        positive = set(positive_feedback)
        negative = set(negative_feedback)
        scores = []

        s = len(student_id)

        for i in range(s):
            point = 0
            words = report[i].split(" ")
            for word in words:
                if word in positive:
                    point += 3
                elif word in negative:
                    point -= 1
            scores.append([point, student_id[i]])

        scores.sort(key = lambda x : (-x[0], x[1]))

        for i in range(k):
            res.append(scores[i][1])
        return res

        
