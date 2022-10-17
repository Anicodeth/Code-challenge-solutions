class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints) - k
        minSubArraySum = curr = sum(cardPoints[:size])
        
        for i in range(len(cardPoints) - size):
            curr += cardPoints[size + i] - cardPoints[i]
            minSubArraySum = min(minSubArraySum, curr)
            
        return sum(cardPoints) - minSubArraySum
