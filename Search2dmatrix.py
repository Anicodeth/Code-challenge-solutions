class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols=len(matrix[0])
        for row in matrix:
            if row[cols-1]<target:
                continue
            for entry in row:
                if entry==target:
                    return True

        return False
