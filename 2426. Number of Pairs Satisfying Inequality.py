from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        list1=SortedList()
        count=0
        for i,j in zip(nums1,nums2):
            count+=list1.bisect_right(i-j+diff)
            list1.add(i-j)
        return count
