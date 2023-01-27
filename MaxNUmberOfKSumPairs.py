class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l,count=0,0
        r=len(nums)-1
        nums.sort()

        while(l<r):
            if (nums[l]+nums[r]==k):
                nums.pop(l)
                r-=1
                nums.pop(r)
                r-=1
                count+=1
            elif (nums[l]+nums[r]>k):
                r-=1
            elif (nums[l]+nums[r]<k):
                l+=1

        return count
            
