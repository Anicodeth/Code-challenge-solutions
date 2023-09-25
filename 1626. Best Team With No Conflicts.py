class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]       
        pairs.sort()
        dp = [score for score, age in pairs]
        for i in range(len(pairs)):
            for j in range(i):
                if pairs[i][1] >=  pairs[j][1]:
                    dp[i] = max(dp[j] + pairs[i][0], dp[i] )

        return max(dp)
        
        
