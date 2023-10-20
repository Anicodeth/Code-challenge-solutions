class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        table = Counter(nums)
        n = len(nums) // 2

        for num, count in table.items():
            if count == n:
                return num
