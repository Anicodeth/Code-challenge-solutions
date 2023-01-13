from collections import defaultdict
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        main=defaultdict(list)
        for r, e in enumerate(matrix):
            for c,v in enumerate(e):
                main[r-c].append(v)
                
        for i in main:
            if len(set(main[i]))!=1:
                return False
        return True
