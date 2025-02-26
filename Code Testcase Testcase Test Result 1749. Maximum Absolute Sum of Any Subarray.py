class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_ = max_ = minRunner = maxRunner = 0

        for num in nums:
            minRunner = min(num, minRunner + num)
            maxRunner = max(num, maxRunner + num)

            min_ = min(min_, minRunner)
            max_ = max(max_, maxRunner)

        return max(abs(min_), max_)
