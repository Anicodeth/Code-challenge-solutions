class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bits  = [[0,0] for _ in range(32)]

        def hamming(num):
            for i in range(32):
                bit = (num >> i) & 1
                if bit == 1 :
                    bits[i][0] += 1
                else:
                    bits[i][1] += 1


        for num in nums:    
            tup = hamming(num)

        d = 0
        for a,b in bits:
            d += (a * b)
        return d
        
