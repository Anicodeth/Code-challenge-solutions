class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prefix = {0: -1} 
        curr_sum = 0
        for i in range(n):
            curr_sum += nums[i]
            curr_sum %= k

            if curr_sum in prefix:
                if i - prefix[curr_sum] > 1:
                    return True
            else:
                prefix[curr_sum] = i

        return False


