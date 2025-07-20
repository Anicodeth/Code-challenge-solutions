class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:

        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(reverse = True)

        selected = nums[:k]
        selected.sort(key = lambda x:x[1])

        return [ num for num, _ in selected]
        
