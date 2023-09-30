class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}

        n = len(nums)

        for i in range(n):
            if nums[i] in dic and dic[nums[i]] >= 2:
                nums[i] = inf
            else:
                dic[nums[i]] = dic.get(nums[i], 0) + 1

        nums.sort()

        return sum(dic.values())

        
