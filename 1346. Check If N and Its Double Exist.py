class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen:
                return True

            seen.add(num)
        
        seen = set()
        for num in arr[::-1]:
            if num * 2 in seen:
                return True

            seen.add(num)

        return False
        
