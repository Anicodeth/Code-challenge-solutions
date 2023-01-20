class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        new=[]
        for num in nums:
            new.append((int(str(num)[::-1])))
        new+=nums
        return len(set(new))
