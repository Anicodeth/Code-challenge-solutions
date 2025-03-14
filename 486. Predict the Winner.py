class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def recure(l, r):
            if l == r:
                return nums[l]
                
            left = nums[l] - recure(l + 1, r)
            right = nums[r] - recure(l, r - 1)

            return max(left, right)

        return recure(0, len(nums) - 1) >= 0
