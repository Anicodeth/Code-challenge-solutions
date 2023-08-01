class Solution:

    def __init__(self, nums: List[int]):
      self.nums = list(nums)
      self.shuffled = nums
    def reset(self) -> List[int]:
      self.shuffled = self.nums
      self.nums = list(self.nums)
      return self.shuffled

    def shuffle(self) -> List[int]:

      for i in range(len(self.shuffled)):
        r = random.randrange(i, len(self.shuffled))
        self.shuffled[i], self.shuffled[r] = self.shuffled[r], self.shuffled[i]
      return self.shuffled
        
