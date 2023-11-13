class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x: (str(bin(x)).count('1'), x))
        return arr
        
