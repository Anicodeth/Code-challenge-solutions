class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        res1 = set()
        res2 = set()

        for num in nums1:
            if num not in set2:
                res1.add(num)
        for num in nums2:
            if num not in set1:
                res2.add(num)

        return [list(res1), list(res2)]
        
