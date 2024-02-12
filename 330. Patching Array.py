class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach = 0
        patches = 0

        for num in nums:
            if n <= reach:
                break      
            while reach < num and num != reach + 1 and n > reach:
                reach += (reach + 1)
                patches += 1
            else:
                reach += num

        while reach < n:
                reach += (reach + 1)
                patches += 1


        return patches
        
