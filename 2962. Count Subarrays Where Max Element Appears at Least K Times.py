class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_ = max(nums)

        l = 0
        n = len(nums)
        countMax = 0
        res = 0

        for r in range(n):
            if nums[r] == max_: countMax += 1

            while countMax >= k:
                if nums[l] == max_: countMax -= 1
                l += 1

            res += l


        return res

