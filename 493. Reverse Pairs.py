class Solution:
    def __init__(self):
      self.count = 0
    def merge_sort(self,arr):
        if len(arr) <= 1:
            return arr
        m = len(arr) // 2
        left_half = self.merge_sort(arr[:m])
        right_half = self.merge_sort(arr[m:])
        return self.merge(left_half, right_half)

    def merge(self, left_half, right_half):
        p1 = p2 = 0
        merged = []

        while(p1 < len(left_half) and p2 < len(right_half)):
          if left_half[p1] > 2 * right_half[p2]:
            self.count += len(left_half) - p1
            p2 += 1
          else:
            p1 +=1


        p1 = p2 = 0

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
    def reversePairs(self, nums: List[int]) -> int:
      self.merge_sort(nums)
      return self.count
