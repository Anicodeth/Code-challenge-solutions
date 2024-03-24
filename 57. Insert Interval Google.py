class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        merged = []

        i = 0
        n = len(intervals)

        while i < n and intervals[i][0] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
            
        if not merged:
            merged.append(newInterval)
        elif merged[-1][1] < newInterval[0]:
            merged.append(newInterval)
        else:
            merged[-1][1] = max(merged[-1][1], newInterval[1])

        while i < n:
            if merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])

            i += 1

        return merged

        
