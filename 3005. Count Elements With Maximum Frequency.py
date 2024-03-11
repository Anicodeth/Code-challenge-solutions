class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        sumi = 0
        largest = max(count.values())
        for _, value in count.items():
            if value == largest:
                sumi += value

        return sumi
