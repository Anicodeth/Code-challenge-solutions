class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        p2 = 0
        n = len(nums)
        res = 0

        for p1 in range(n):
            if nums[p1] == 0:
                while nums[p2] != 0:
                    p2 += 1
                res += p1 - p2 + 1
            elif nums[p1] != 0:
                p2 = p1

        return res
