class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)
        freq = Counter(nums)

        if n % 2 == 1: return False

        for value in freq.values():
            if value > 2:
                return False

        return True
        
