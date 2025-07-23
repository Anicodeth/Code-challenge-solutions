class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        l = 0
        n = len(nums)
        maxi = nums[0]
        running = 0

        for r in range(n):
            while counter[nums[r]] != 0:
                counter[nums[l]] -= 1
                running -= nums[l]
                l += 1

            running += nums[r]
            counter[nums[r]] += 1
            maxi = max(maxi, running)

        return maxi



        
