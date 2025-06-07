class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        removed = set()

        for i, c in enumerate(s):
            if c.isalpha():
                heapq.heappush(heap, (ord(c), -i))
            else:
              if heap:
                _, index = heapq.heappop(heap)
                removed.add(-index)
                                

        n = len(s)
        res = []

        for i in range(n):
            if i in removed or s[i] == "*":
                continue

            res.append(s[i])

        return "".join(res)

            
        
                
