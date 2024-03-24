class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findIndex(nums, target, section):
            res = -1
            l, r = 0, len(nums) - 1
            
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    res = m
                    if section == "Start":
                        r = m - 1
                    else:
                        l = m + 1

            return res

        start = findIndex(nums, target, "Start")
        end = findIndex(nums, target, "End")

        return [start, end]

        
