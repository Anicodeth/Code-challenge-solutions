class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        
        count = 0
        added = set()
        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if sqrt((i - x) ** 2 + (j - y) ** 2) <= r and (i, j) not in added:
                        added.add((i, j))
                        count += 1
        return count
        
