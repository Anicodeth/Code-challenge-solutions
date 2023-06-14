class Solution:
    def findTargetSumWays(self, nums, target):
        memo = {}
        def helper(nums, target, index, curr_sum, memo):
            if index == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0

            if (index, curr_sum) in memo:
                return memo[(index, curr_sum)]

            positive = helper(nums, target, index + 1, curr_sum + nums[index], memo)
            negative = helper(nums, target, index + 1, curr_sum - nums[index], memo)

            memo[(index, curr_sum)] = positive + negative

            return memo[(index, curr_sum)]
        return helper(nums, target, 0, 0, memo)

