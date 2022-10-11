class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        size=range(len(nums))
        count=0
        for i in size:
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:                    
                    count+=1
        return count
