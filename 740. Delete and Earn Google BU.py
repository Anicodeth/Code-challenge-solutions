class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        maxi = max(nums) 
        points = defaultdict(int)

        for num in nums:
            points[num] += num

        dp = [0 for _ in range(maxi + 1)]

        dp[0] = 0
        dp[1] = points[1]

        for i in range(2, maxi + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

        return dp[-1]


        
