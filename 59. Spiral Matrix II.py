class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        i = 0
        j = 0
        directions = ["R", "D", "L", "U"]
        command = 0
        val = 1
        mat = [[0 for _ in range(n)] for _ in range(n)]
        visited = set()
        for _ in range((n * n) + (n * 4 )):
            if i < 0 or j < 0 or i >= n or j >= n or (i, j) in visited:
                #Revert last move
                if command == 0:
                    j -= 1
                    i += 1
                elif command == 1:
                    i -= 1
                    j -= 1
                elif command == 2:
                    j += 1
                    i -= 1
                elif command == 3:
                    i += 1
                    j += 1
                command = (command + 1) % 4
                continue

            mat[i][j] = val 
            val += 1
            visited.add((i, j))
            if command == 0:
               j += 1
            elif command == 1:
               i += 1
            elif command == 2:
               j -= 1
            elif command == 3:
               i -= 1



        return mat

        
