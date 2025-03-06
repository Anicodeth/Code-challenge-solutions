class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        positions = [ False for _ in range(len(grid)**2 + 1)]
        positions[0] = True 
        n = len(grid)

        repeated, noThere = 0, 0
        for i in range(n):
            for j in range(n):
                placed = positions[grid[i][j]]
                if placed:
                    repeated = grid[i][j]

                positions[grid[i][j]] = True

        for i, exists in enumerate(positions):
            if not exists:
                noThere = i

        return [repeated, noThere]
