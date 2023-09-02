class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = {}
        for num in nums1:
          dic[num[0]] = num[1]

        for num in nums2:
          dic[num[0]] = dic.get(num[0], 0) + num[1]

        res = []

        for tup in dic.items():
          res.append([tup[0], tup[1]])

        res.sort(key = lambda x : x[0])

        return res
