class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        heap = []

        def dp(number):
            if number == 1:
                return 1
            elif number in memo:
                return memo[number]
            elif number % 2 == 0:
                memo[number] = dp( number // 2 ) + 1
                return memo[number]
            elif number % 2 == 1:
                memo[number] = dp( 3 * number + 1) + 1  
                return memo[number]

        for number in range(lo, hi + 1):
            power = dp(number)
            heapq.heappush(heap, (power, number))   
        value = (0,0)
        while k != 0:  
            value = heapq.heappop(heap)
            k -= 1

        return value[1]
