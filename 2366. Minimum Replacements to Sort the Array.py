class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        n = len(nums)
        prev = nums[-1]
        count = 0

        for i in range(n - 2, -1, -1):

            if nums[i] <= nums[i + 1]:
                continue
            #Number of elements
            bucks = ceil(nums[i] / nums[i + 1])
            count += bucks - 1

            nums[i] = nums[i] // bucks

        return count

                



