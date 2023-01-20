class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        c=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if i==j:
                    continue
                elif nums[i]>nums[j]:
                    count+=1
            c.append(count)
        return c
