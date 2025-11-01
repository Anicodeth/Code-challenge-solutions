class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]
        n = len(intervals)

        for i in range(1, n):
            top = stack.pop()

            if top[1] >= intervals[i][0]:
                stack.append([top[0], max(top[1], intervals[i][1])])
            else:
                stack.append(top)
                stack.append(intervals[i])

        return stack
