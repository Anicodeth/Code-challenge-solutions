class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
 
        for num in arr:
            last = dp.get(num - difference, 0)
            dp[num] = last + 1

        return max(dp.values())
