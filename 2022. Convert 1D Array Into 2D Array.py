class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            result[i] = original[i * n: (i + 1) * n]

        return result
            
