class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        rank=[]
        size=range(len(points))
        def eculid(point1:List[int]) -> float:
            return sqrt(((point1[0]-0)**2)+((point1[1]-0)**2))
        
        for i in size:
            points[i].append(eculid(points[i]))

        for j in size:
            for p in size:
                if j==p:
                    continue
                if points[j][2]<points[p][2]:
                    temp=points[j]
                    points[j]=points[p]
                    points[p]=temp
        
        for o in size:
            if (k!=0) and (points[o][:2] not in rank):
                rank.append(points[o][:2])
                k-=1
        
        return rank
