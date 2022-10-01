class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        count=0
        for j in range(m,n+m):
            nums1[j]=nums2[count]
            count+=1
            if count>n:
                break
        nums1.sort()
