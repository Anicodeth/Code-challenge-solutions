class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = [intervals[i] + [i] for i in range(len(intervals))]
        starts.sort(key = lambda x : x[0])

        def binary_search(end):
            l = 0
            r = len(starts) - 1
            ans  = -1

            while l <= r:
                m = (l + r) // 2

                if starts[m][0] >= end:
                    ans = starts[m][2]
                    r = m - 1
                else:
                    l = m + 1
            return ans

        res = []
        for start, end in intervals:
            right = binary_search(end)
            res.append(right)

        return res
