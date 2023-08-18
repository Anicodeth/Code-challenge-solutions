class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
      last= 0 
      layer = 0

      for num in target:
        layer += num - last if num > last else 0
        last = num

      return  layer
