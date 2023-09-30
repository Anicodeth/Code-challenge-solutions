class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        res = []
        for start1, end1 in firstList:
            for start2, end2 in secondList:
                if start2 <= end1 and end2 >= start1:
                    newinterval = [max(start1,start2), min(end1, end2)]
                    res.append(newinterval)
        return res




