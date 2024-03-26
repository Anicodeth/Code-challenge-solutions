class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        total = sum(nums)
        target = total - x

        if target < 0 : return -1

        curr = 0

        l = 0 

        n = len(nums)
        maxi = -1
        for r in range(n):
            curr += nums[r]

            while curr > target:
                curr -= nums[l]
                l += 1

            if curr == target:
                maxi = max(maxi, r - l + 1)

        return (n - maxi) if maxi != -1 else -1

            
            
        
