class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(nums.count(val)):
            nums.remove(val)
