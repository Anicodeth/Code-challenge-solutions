class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dis = defaultdict(list)
        for num in arr:
            diff = abs(x - num)
            dis[diff].append(num)

        values = list(dis.items())
        values.sort(key = lambda x : x[0])

        res = []

        for key, value in values:
            if len(res) < k:
              for num in value:
                  if len(res) < k:
                    res.append(num)

        res.sort()
        return res
                
        
        
        
