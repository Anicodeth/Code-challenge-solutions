class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        first = set()
        second = set()

        prefix = [0]

        for i in range(len(A)):
            first.add(A[i])
            second.add(B[i])
            valid = 0
            
            if A[i] in second:
                valid += 1
            
            if B[i] in first:
                valid +=1

            if A[i] == B[i]: valid -= 1

            prefix.append(prefix[-1] + valid)

        return prefix[1:]

