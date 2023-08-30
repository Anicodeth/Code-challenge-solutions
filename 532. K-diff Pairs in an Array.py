class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
      diff = {}
      count  = 0
      paired = set()


      for num in nums:

        up = num + k
        down = num - k
        if up in diff and not (num, up) in paired:
          count += diff[up]
          paired.add((num, up))
          paired.add((up, num))
        if down in diff and not (num, down) in paired:
          count += diff[down]
          paired.add((num, down))
          paired.add((down, num))
          
        diff[num] = 1

      return count
          
