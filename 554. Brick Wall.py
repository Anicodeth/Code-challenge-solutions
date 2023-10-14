class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        n = len(wall)

        points = {}

        for row in wall:
            point = 0
            for i in range(len(row) - 1):
                point += row[i]
                points[point] = points.get(point, 0) + 1
        lines =[p for p in points.values()]
        lines.sort()
        num  = n - lines[-1] if lines else n
        return num
