class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        p2 = p3 = p5 = 0 
        ugly = [1]

        while len(ugly) < n:
            
            new = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)

            if new == ugly[p2] * 2:
                p2 += 1
            if new == ugly[p3] * 3:
                p3 += 1      
            if new == ugly[p5] * 5:
                p5 += 1

            ugly.append(new)
        return ugly[-1]
                
