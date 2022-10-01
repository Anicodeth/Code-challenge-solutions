class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,n in enumerate(nums):
            if i>0 and nums[i-1]==n:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                    sum = nums[i]+nums[l]+nums[r]
                    if sum>0:
                        r-=1
                    elif sum<0:
                        l+=1
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                        l+=1
                        while nums[l]==nums[l-1] and l<r:
                            l+=1
        return res 
