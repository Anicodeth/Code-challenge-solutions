class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        maxi = max(nums) 
        points = defaultdict(int)

        for num in nums:
            points[num] += num

        @cache
        def dp(num):
            if num == 0 or num == 1:
                return points[num]

            return max(points[num] + dp(num - 2), dp(num - 1))

        return dp(maxi)


        
