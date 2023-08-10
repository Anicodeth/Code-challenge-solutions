class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
      dic = Counter(arr1)

      temp = []
      visited = set()

      for num in arr2:
        for _ in range(dic[num]):
          temp.append(num)
        visited.add(num)
      reject = []
      for num in dic:
        if num not in visited:
          for _ in range(dic[num]):
            reject.append(num)
      reject.sort()
      temp.extend(reject)
      return temp
