class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()

        i = 0
        n = len(nums)

        while i < n:
            correct = nums[i] - 1
            if i != correct:
                if nums[i] == nums[correct]:
                    res.add(nums[i])
                    i += 1
                    continue
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        return list(res)


        
