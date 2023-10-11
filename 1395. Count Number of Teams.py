class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        dp = [0 for _  in range(n)]
        ldp = dp[:]
        for i in range(n):
            for j in range(i):
                if rating[j] > rating[i]:
                    dp[i] += 1 
                if rating[j] < rating[i]:
                    ldp[i] += 1 
        
        count = 0

        for i in range(n):
            for j in range(i):
                if rating[j] > rating[i]:
                    count += dp[j]
                elif rating[j] < rating[i]:
                    count += ldp[j]

        return count

        
        
