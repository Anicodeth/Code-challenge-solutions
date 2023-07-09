class Solution:
    def rob(self, nums: List[int]) -> int:
      seq1, seq2 = 0, 0
      for num in nums:
        temp = max(num + seq1, seq2)
        seq1 = seq2
        seq2 = temp
      return seq2
