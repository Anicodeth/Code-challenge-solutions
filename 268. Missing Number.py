class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=dic.get(i,0)+1
        
        for i in range(len(nums)+1):
            if i not in dic:
                return i

        
