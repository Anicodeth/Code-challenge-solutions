class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        count = 0

        n = len(nums)
        found = False
        index = 0

        for i in range(1, n):

            if nums[i] < nums[i - 1]:
                count += 1
                if not found: 
                    index = i - 1
                    found = True

        if count == 0: return 0
        if nums[-1] > nums[0]: count += 1

        if count == 1: return (n - 1) - index

        return -1
        
