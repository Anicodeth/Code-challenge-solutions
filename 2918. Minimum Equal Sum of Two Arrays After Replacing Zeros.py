class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        count1 = nums1.count(0)
        count2 = nums2.count(0)

        if sum1 + count1 > sum2 + count2 and count2:
            return sum1 + count1
        elif sum1 + count1 < sum2 + count2 and count1:
            return sum2 + count2
        elif sum1 + count1 == sum2 + count2:
            return sum1 + count1
        else:
            return -1
