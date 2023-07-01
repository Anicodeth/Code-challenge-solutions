class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      dic = defaultdict(list)

      for i, num in enumerate(nums):
        if num in dic:
         for value in dic[num]:
          if abs(value - i) <= k:
            return True
        dic[num].append(i)

      return False
