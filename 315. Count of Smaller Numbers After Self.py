class Solution:
    def mergesort(self, arr):
      if len(arr) <= 1:
        return arr

      m = len(arr)//2

      left_half = self.mergesort(arr[:m])
      right_half = self.mergesort(arr[m:])

      return self.merge(left_half, right_half)

    def merge(self, left_half, right_half):
      p1 = p2 = 0
      merged = []

      while(p1 < len(left_half) and p2 < len(right_half)):

          if(left_half[p1] >= right_half[p2]):
              merged.append(right_half[p2])
              p2+=1
          elif(right_half[p2] >= left_half[p1]):
              merged.append(left_half[p1])
              p1+=1

      if p2 == len(right_half):
          for i in range(p1, len(left_half)):
              merged.append(left_half[i])
      elif p1 == len(left_half):
          for i in range(p2, len(right_half)):
              merged.append(right_half[i])

      return merged
    
    def binarysearch(self, arr, key):
      low = 0
      high = len(arr) - 1
      result = -1

      while low <= high:
          mid = (low + high) // 2

          if arr[mid] == key:
              result = mid
              high = mid - 1
          elif arr[mid] < key:
              low = mid + 1
          else:
              high = mid - 1

      return result
    
    def countSmaller(self, nums: List[int]) -> List[int]:

      sortednums = self.mergesort(nums)
      counts = []
      for num in nums:
        smaller = self.binarysearch(sortednums, num)
        counts.append(smaller)
        sortednums.pop(smaller)

      return counts
