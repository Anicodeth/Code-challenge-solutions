class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefix = [ 0 ]
        for num in arr:
            prefix.append(prefix[-1] + num)

        n = len(prefix)
        sumi = 0

        for i in range(1, n):
            for j in range(i):
                if ( i - j ) % 2 == 1:
                    sumi += prefix[i] - prefix[j]


        return sumi
