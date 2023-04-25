class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        P = [0]
        for x in nums: P.append(P[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in P:
            ans += count[x]
            count[x + goal] += 1

        return ans
