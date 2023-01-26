class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:       
        p1=0
        p2=1

        while(p2<len(nums)):
            if(nums[p1]==nums[p2]):
                nums[p1]*=2
                nums[p2]=0
            p1+=1
            p2+=1

        zeros=nums.count(0)
        for _ in range(zeros):
            nums.remove(0)
        nums+=[0]*zeros
        
        return nums
