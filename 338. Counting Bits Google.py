class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        
        for num in range(n + 1):
            count = 0
            for i in range(32):
                shifted = 1 << i
                if num & shifted:
                    count += 1
            res.append(count)

        return res
