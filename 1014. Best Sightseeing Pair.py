class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi = 0
        current_score = values[0]
        for j in range(1, len(values)):
            maxi = max(maxi, current_score + values[j] - j)
            current_score = max(current_score, values[j] + j)
        
        return maxi
