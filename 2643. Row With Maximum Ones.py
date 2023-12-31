class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = [0, mat[0].count(1)]
        for i, row in enumerate(mat):
            local = mat[i].count(1)
            if res[1] < local:
                res = [i, local]

        return res

        
