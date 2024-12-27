class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        local = [-1, -1]
        Max = -1

        for i, val in enumerate(values):
            localMax = val + local[0] + (local[1] - i)
            Max = max(Max, localMax)

            if local[0] - (i - local[1]) < val:
                local = [val, i]
        
        return Max
        
