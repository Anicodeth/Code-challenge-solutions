class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
      res = set()

      nums1 = set(nums1)
      nums2 = set(nums2)
      nums3 = set(nums3)
      array = [nums1, nums2, nums3]

      for i in range(len(array) - 1):
        for k in (array[i]):
          for j in range(i + 1, len(array)):
           if i!=j and k in array[j]:
             res.add(k)

      return list(res)

