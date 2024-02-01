class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        while ((numOnes or numZeros or numNegOnes) and k):
            if numOnes:
                res += 1
                numOnes -= 1
                k  -= 1
                continue
            elif numZeros:
                numZeros -= 1
                k  -= 1
                continue
            elif numNegOnes:
                res -= 1
                numNegOnes -= 1
                k  -= 1

        return res
        
