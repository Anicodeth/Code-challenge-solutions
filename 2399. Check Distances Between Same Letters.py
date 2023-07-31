class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
      hashmap = {}

      for i, c in enumerate(s):
        if c in hashmap:
          hashmap[c] = i - hashmap[c] - 1
        else:
          hashmap[c] = i

      for i, num in enumerate(distance):
        if chr(i + 97) in hashmap and num != hashmap[chr(i + 97)]:
          return False

      return True
