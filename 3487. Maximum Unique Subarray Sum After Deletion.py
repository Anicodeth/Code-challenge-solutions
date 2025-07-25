class Solution:
    def maxSum(self, nums: List[int]) -> int:
        uniques = set(nums)
        count = 0
        sumi = 0
        for num in uniques:
            if num >= 0:
                count += 1
                sumi += num

        return sumi if count > 0 else max(uniques)
