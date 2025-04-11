class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        
        for num in range(low, high + 1):
            strForm = str(num)
            n = len(strForm)

            if n % 2 != 0: continue

            first = 0
            for i in range(n//2): first += int(strForm[i])
            
            second = 0
            for i in range(n//2, n): second += int(strForm[i])

            count += (first == second)

        return count
