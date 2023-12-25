class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def unq(num1, num2):
            count = 0
            num2 = set(num2)
            for a in num1:
                if a in num2:
                    count += 1
            return count 

        return [ unq(nums1, nums2), unq(nums2, nums1) ]

        
