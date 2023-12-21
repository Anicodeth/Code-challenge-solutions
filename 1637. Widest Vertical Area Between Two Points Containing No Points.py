class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:x[0])

        maxi = 0
        n = len(points)

        for i in range(n - 1):
            diff = points[i + 1][0] - points[i][0]
            if diff > maxi:
                maxi = diff

        return maxi
