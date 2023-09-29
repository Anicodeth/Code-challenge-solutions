class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        p = 0
        res = []

        while p < n:
            start = end = nums[p]

            while p < n - 1 and nums[p] + 1 == nums[p + 1]:
                end = nums[p + 1]
                p += 1

            if start == end:
                res.append(str(start))
            else:
                res.append(f"{start}->{end}")
            p += 1 

        return res

        
