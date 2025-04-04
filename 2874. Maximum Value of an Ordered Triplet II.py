class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        mini = [nums[0]]
        maxi = [nums[0]]
        maxi2 = [0] * (len(nums) + 1)
        maxi2[-1] = nums[-1]

        for num in nums:
            if num > maxi[-1]: maxi.append(num)
            else: maxi.append(maxi[-1])

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > maxi2[i + 1]:
                maxi2[i] = nums[i]
            else:
                maxi2[i] = maxi2[i+1]

        gloMaxi = -inf

        for i in range(1, len(nums) - 1):
            gloMaxi = max(gloMaxi, (maxi[i + 1] - nums[i]) * maxi2[i + 1])

        return gloMaxi

        
