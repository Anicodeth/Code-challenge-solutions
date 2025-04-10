class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort() 
        dp = [set([num]) for num in nums]

        n = len(nums)
        for i in range(n):
            largest = []
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) > len(largest):
                    largest = dp[j]
                    
            for num in largest: dp[i].add(num)

        largest = -inf
        for nums in dp:
            if len(nums) > largest: largest = len(nums)

        for nums in dp:
            if len(nums) == largest:
                return list(nums)
