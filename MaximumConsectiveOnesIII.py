class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        cntZeros = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                cntZeros += 1
            while cntZeros > k: 
                if nums[left] == 0: cntZeros -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
