class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0

        for _ in range(k ):
            ans += nums[-1]
            nums[-1] = nums[-1] + 1

        return ans

        
