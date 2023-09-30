class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.sort(key = lambda x: x[0])
        secondList.sort(key = lambda x: x[0])

        
        res = []
        for start1, end1 in firstList:
            for start2, end2 in secondList:
                if start2 <= end1:
                    newinterval = [max(start1,start2), min(end1, end2)]
                    if newinterval[1] >= newinterval[0]:
                        res.append(newinterval)




        return res

