from sortedcontainers import SortedList 

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
      nums = SortedList()
      count = 0

      for i, num in enumerate(instructions):

        greater = nums.bisect_right(num)
        less = nums.bisect_left(num)
        nums.add(num)
        count += min(less, i - greater)

      return count % (10**9 + 7)


      print(nums)

      


      
