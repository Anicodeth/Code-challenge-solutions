        n = len(nums)
        dp = [1] * n

        for i in range(1,n):
            if nums[i - 1] < nums[i]:
                dp[i] = dp[i-1] + 1

        return max(dp)

        
