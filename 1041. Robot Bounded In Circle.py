class Solution:
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1

        for instr in instructions:
            if instr == 'R':
                dx, dy = dy, -dx
            elif instr == 'L':
                dx, dy = -dy, dx
            elif instr == 'G':
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
