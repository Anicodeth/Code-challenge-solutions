class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        seprate=[]
        for el in list(map(str,nums)):
            seprate+=list(el)
        return list(map(int,seprate))

        
