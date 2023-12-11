class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)
        table = {}

        for num in arr:
            table[num] = table.get(num, 0) + 1
            if table[num] / size > 0.25:
                return num

        
            
        
