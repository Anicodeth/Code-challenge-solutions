class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        replica = [ 0 for _ in range(n)]

        for i, num in enumerate(nums):
            newIndex = (i + k) % n
            replica[newIndex] = num
       
        for i in range(n):
            nums[i] = replica[i]
