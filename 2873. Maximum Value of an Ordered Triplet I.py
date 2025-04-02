class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = -inf

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    maxi = max(maxi, (nums[i] - nums[j]) * nums[k])

        return max(0, maxi)


