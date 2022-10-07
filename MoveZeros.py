class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pops=[]
        for i,n in enumerate(nums):
            if n==0:
                pops.append(i)
        

        for j in range(len(pops)-1,-1,-1):
           nums.append(nums.pop(pops[j]))
