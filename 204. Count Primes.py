class Solution:
    def countPrimes(self, n: int) -> int:

        numbers = [ False for _ in range(n) ]

        for num, val in enumerate(numbers):
            if num == 0:
                 numbers[num] = True
                 numbers[-1] = True
                 continue
            if not val:
                i = 2
                while (num + 1) * i <= n:
                    numbers[(i * (num + 1)) - 1] = True
                    i += 1

        count = 0

        for num in numbers:
            if not num:
                count += 1

        return count


        
