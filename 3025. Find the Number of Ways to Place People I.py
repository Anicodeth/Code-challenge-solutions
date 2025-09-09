class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0

        for i in range(n):
            for j in range(n):
                if i == j: 
                    continue
                Ax, Ay = points[i]
                Bx, By = points[j]

                if Ax <= Bx and Ay >= By and (Ax < Bx or Ay > By):
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        Cx, Cy = points[k]
                        if Ax <= Cx <= Bx and By <= Cy <= Ay:
                            valid = False
                            break
                    if valid:
                        ans += 1
        return ans
