class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            if (num % 3) == 1 or (num % 3) == 2:
                res += 1

        return res
        
