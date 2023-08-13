class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
      def distance(p1, p2):
        return sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

      count = 0
      n = len(points)

      for i in range(n):
        dis = {}
        for j in range(n):
          if i != j:
            d = distance(points[i], points[j])
            dis[d] = dis.get(d, 0) + 1
            
        for d in dis.values():
          count += d * (d - 1)

      return count

