class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      t = 0
      b = 0

      res = []

      while len(nums1) != t and len(nums2) != b:
        if nums1[t] <= nums2[b]:
          res.append(nums1[t])
          t += 1
        else:
          res.append(nums2[b])
          b += 1
        
      if len(nums1) != t:
        res.extend(nums1[t:])
      elif len(nums2) != b:
        res.extend(nums2[b:])

      if len(res) % 2 == 1:
        return res[(len(res)//2)]   
      else:
        return (res[len(res)//2] + res[(len(res)//2) - 1])/2
