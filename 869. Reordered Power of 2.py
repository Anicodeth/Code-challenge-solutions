class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        k = len(str(n))
        curr = 0
        i = 0
        
        while True:
            curr = 2 ** i
            if k == len(str(curr)) and Counter(str(n)) == Counter(str(curr)):
                return True
            if k < len(str(curr)):
                break
            i += 1

        return False
